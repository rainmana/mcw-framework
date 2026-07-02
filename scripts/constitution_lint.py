#!/usr/bin/env python3
"""constitution-lint: Phase 0 mechanical checks for the MCW Constitution.

Implements the mechanical layer specified in docs/constitution_as_code.md:

  1. Glossary structural lint  — every canonical construct present exactly
     once; six failure modes and five repair operations (no more, no fewer);
     Definition blocks present; exclusion blocks on core constructs; a
     Layer 0 gloss on every canonical entry (Article II floor).
  2. Link/anchor integrity     — every internal link in docs/ resolves to an
     existing file, and every fragment resolves to a real heading anchor.
  3. Amendment guard           — the frozen fields of canonical glossary
     entries (per the glossary change policy) are pinned as plain-text
     snapshots in governance/canon/ plus SHA-256 hashes in
     governance/canon_hashes.json. Any divergence fails. Updating the pin
     requires the `[definition-change]` commit marker or the
     `type:definition-change` PR label. Edits to docs/constitution.md
     require a version bump plus an "Amendment Rationale" section, or the
     `[non-normative]` commit marker for formatting/link-only changes.
  4. Evidence-marker presence  — every docs page carries an evidence-layer
     marker: an inline `[L0]`..`[L4]` tag or an `Evidence: Ln` status line
     (Article IV floor).
  5. Anti-capture scan         — ADVISORY ONLY: Article VI overclaim
     patterns produce warnings, never failures (pattern matching cannot
     read meaning; a human outranks this check).

Honesty note (single-maintainer degenerate case): in a one-person repo,
Code Owner review is self-review. These mechanical checks are the only
non-self reviewer this repository currently has. They verify that
declarations exist — they cannot verify that declarations are true.

Usage:
  python scripts/constitution_lint.py           # check (CI mode)
  python scripts/constitution_lint.py --update  # regenerate canon pins
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
GLOSSARY = DOCS / "glossary.md"
CONSTITUTION_REL = "docs/constitution.md"
GOVERNANCE = ROOT / "governance"
CANON_DIR = GOVERNANCE / "canon"
HASHES_FILE = GOVERNANCE / "canon_hashes.json"

# Canonical constructs (Constitution Article I) plus the Evidence Layers
# entry, which restates Article IV and is pinned so it cannot drift silently.
CANONICAL: dict[str, list[str]] = {
    "core": [
        "Information Unit (IU)",
        "Human Context Window (HCW)",
        "Artificial Context Window (ACW)",
        "Meta-Context Window (MCW)",
    ],
    "failure_mode": [
        "Drift (Silent Desynchronization)",
        "Asymmetric State Advancement",
        "False Alignment",
        "Overcompression",
        "Constraint Opacity",
        "Repair Suppression",
    ],
    "repair_op": [
        "Re-grounding",
        "Decompression",
        "Re-weighting",
        "Disambiguation",
        "Synchronization",
    ],
    "proxy": [
        "MCW Health (H)",
        "Repair Cost (R)",
        "Drift Rate (D)",
        "Misattribution (M)",
    ],
    "meta": [
        "Evidence Layers (L0–L4)",
    ],
}

# Sections that must contain a "What ... not" exclusion block (Article VII).
EXCLUSION_REQUIRED = {
    "Meta-Context Window (MCW)",
    "Information Unit (IU)",
    "Evidence Layers (L0–L4)",
}

# Categories whose entries carry an explicit "**Definition:**" label.
DEFINITION_REQUIRED_CATEGORIES = {"core", "failure_mode", "repair_op"}

# Amendable fields per the glossary change policy: lines starting with these
# prefixes are NOT part of the frozen definition text.
AMENDABLE_PREFIXES = (
    "**Type:**",
    "**Layer 0 gloss:**",
    "*Example:*",
    "**Early signals:**",
    "**Key danger:**",
    "*Status:",
)

EVIDENCE_TAG_RE = re.compile(r"\s*`?\[L[0-4]\]`?")
PAGE_MARKER_RE = re.compile(
    r"\[L[0-4]\]|Evidence(?:\s+layer)?[^.:\n]{0,60}:\s*\**\s*L[0-4]"
)
# Pages exempt from the per-page evidence marker: the Constitution is a
# normative document, not an empirical one.
MARKER_ALLOWLIST = {"constitution.md"}

# Article VI overclaim patterns — advisory. The two governance documents are
# excluded because they quote the banned patterns in order to define them.
OVERCLAIM_PATTERNS = [
    r"\bimplements\s+MCW\b",
    r"\bis\s+MCW-aware\b",
    r"solves?\s+the\s+MCW\s+problem",
    r"reduces?\s+MCW\s+degradation",
]
OVERCLAIM_ALLOWLIST = {"constitution.md", "constitution_as_code.md"}

DEFINITION_CHANGE_MARKER = "[definition-change]"
NON_NORMATIVE_MARKER = "[non-normative]"
DEFINITION_CHANGE_LABEL = "type:definition-change"

errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


# --------------------------------------------------------------------------
# Markdown helpers
# --------------------------------------------------------------------------

def slugify(value: str, separator: str = "-") -> str:
    """Replicates python-markdown's toc slugify (what MkDocs uses)."""
    value = unicodedata.normalize("NFKD", value)
    value = value.encode("ascii", "ignore").decode("ascii")
    value = re.sub(r"[^\w\s-]", "", value).strip().lower()
    return re.sub(rf"[{separator}\s]+", separator, value)


def strip_fences(text: str) -> list[tuple[int, str]]:
    """Return (lineno, line) pairs with fenced code blocks removed."""
    out = []
    in_fence = False
    fence_re = re.compile(r"^\s*(```|~~~)")
    for i, line in enumerate(text.splitlines(), start=1):
        if fence_re.match(line):
            in_fence = not in_fence
            continue
        if not in_fence:
            out.append((i, line))
    return out


def heading_anchors(text: str) -> set[str]:
    """All anchor ids MkDocs generates for a page, including _1 suffixes."""
    anchors: set[str] = set()
    for _, line in strip_fences(text):
        m = re.match(r"^#{1,6}\s+(.*?)\s*$", line)
        if not m:
            continue
        title = re.sub(r"[`*_]", "", m.group(1))
        base = slugify(title) or "section"
        anchor = base
        n = 0
        while anchor in anchors:
            n += 1
            anchor = f"{base}_{n}"
        anchors.add(anchor)
    return anchors


def glossary_sections(text: str) -> dict[str, str]:
    """Map '### Heading' -> section body (until next ### or ##)."""
    sections: dict[str, str] = {}
    current = None
    body: list[str] = []
    for _, line in strip_fences(text):
        m = re.match(r"^###\s+(.*?)\s*$", line)
        if m:
            if current is not None:
                sections.setdefault(current, "\n".join(body))
            current = m.group(1)
            body = []
            continue
        if re.match(r"^##\s+", line):
            if current is not None:
                sections.setdefault(current, "\n".join(body))
            current = None
            body = []
            continue
        if current is not None:
            body.append(line)
    if current is not None:
        sections.setdefault(current, "\n".join(body))
    return sections


def frozen_text(section_body: str) -> str:
    """Extract the frozen fields of a glossary section per the change policy.

    Drops amendable lines (Type, Layer 0 gloss, Example, Early signals,
    Key danger, Status), strips inline evidence tags (amendable annotations),
    and normalizes whitespace.
    """
    kept: list[str] = []
    for line in section_body.splitlines():
        stripped = line.strip()
        if not stripped or stripped == "---":
            continue
        if any(stripped.startswith(p) for p in AMENDABLE_PREFIXES):
            continue
        kept.append(stripped)
    text = " ".join(kept)
    text = EVIDENCE_TAG_RE.sub("", text)
    return re.sub(r"\s+", " ", text).strip()


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


# --------------------------------------------------------------------------
# Check 1: glossary structural lint
# --------------------------------------------------------------------------

def check_glossary_structure(gloss_text: str) -> dict[str, str]:
    sections = glossary_sections(gloss_text)
    all_terms = [t for terms in CANONICAL.values() for t in terms]

    for term in all_terms:
        count = len(re.findall(
            rf"^###\s+{re.escape(term)}\s*$", gloss_text, flags=re.M))
        if count == 0:
            err(f"glossary: canonical term missing: '{term}'")
        elif count > 1:
            err(f"glossary: canonical term defined {count} times: '{term}'")

    n_modes = len(re.findall(r"^\*\*Type:\*\* MCW failure mode\s*$",
                             gloss_text, flags=re.M))
    if n_modes != 6:
        err(f"glossary: expected exactly 6 failure modes, found {n_modes}")
    n_ops = len(re.findall(r"^\*\*Type:\*\* IU repair operation\s*$",
                           gloss_text, flags=re.M))
    if n_ops != 5:
        err(f"glossary: expected exactly 5 repair operations, found {n_ops}")

    for category, terms in CANONICAL.items():
        for term in terms:
            body = sections.get(term)
            if body is None:
                continue  # missing already reported
            if "**Layer 0 gloss:**" not in body:
                err(f"glossary: '{term}' lacks a Layer 0 gloss (Article II)")
            if (category in DEFINITION_REQUIRED_CATEGORIES
                    and "**Definition:**" not in body):
                err(f"glossary: '{term}' lacks a **Definition:** block")
            if term in EXCLUSION_REQUIRED and not re.search(
                    r"\*\*What .{0,40}not", body):
                err(f"glossary: '{term}' lacks its 'what it is not' "
                    f"exclusion block (Article VII)")
    return sections


# --------------------------------------------------------------------------
# Check 2: link and anchor integrity
# --------------------------------------------------------------------------

LINK_RE = re.compile(r"(?<!\!)\[([^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")


def check_links() -> None:
    pages = sorted(DOCS.rglob("*.md"))
    anchor_cache = {p: heading_anchors(p.read_text(encoding="utf-8"))
                    for p in pages}
    for page in pages:
        text = page.read_text(encoding="utf-8")
        rel = page.relative_to(ROOT)
        for lineno, line in strip_fences(text):
            for m in LINK_RE.finditer(line):
                target = m.group(2)
                if re.match(r"^(https?:|mailto:)", target):
                    continue
                if target.startswith("#"):
                    if target[1:] not in anchor_cache[page]:
                        err(f"{rel}:{lineno}: broken same-page anchor "
                            f"'{target}'")
                    continue
                path_part, _, fragment = target.partition("#")
                resolved = (page.parent / path_part).resolve()
                if not resolved.exists():
                    err(f"{rel}:{lineno}: broken link target '{target}'")
                    continue
                if fragment and resolved.suffix == ".md":
                    anchors = anchor_cache.get(resolved)
                    if anchors is None:
                        anchors = heading_anchors(
                            resolved.read_text(encoding="utf-8"))
                    if fragment not in anchors:
                        err(f"{rel}:{lineno}: broken anchor '#{fragment}' "
                            f"in '{path_part}'")


# --------------------------------------------------------------------------
# Check 3: amendment guard (canon pinning + constitution version guard)
# --------------------------------------------------------------------------

def compute_pins(sections: dict[str, str]) -> dict[str, dict[str, str]]:
    pins: dict[str, dict[str, str]] = {}
    for category, terms in CANONICAL.items():
        for term in terms:
            body = sections.get(term)
            if body is None:
                continue
            text = frozen_text(body)
            pins[term] = {
                "category": category,
                "sha256": sha256(text),
                "snapshot": f"governance/canon/{slugify(term)}.txt",
                "text": text,
            }
    return pins


def write_pins(pins: dict[str, dict[str, str]]) -> None:
    CANON_DIR.mkdir(parents=True, exist_ok=True)
    manifest = {}
    for term, pin in sorted(pins.items()):
        (ROOT / pin["snapshot"]).write_text(pin["text"] + "\n",
                                            encoding="utf-8")
        manifest[term] = {k: pin[k] for k in ("category", "sha256",
                                              "snapshot")}
    HASHES_FILE.write_text(
        json.dumps({
            "_comment": (
                "Frozen canonical definition text, pinned. Regenerate with "
                "scripts/constitution_lint.py --update. Changing these pins "
                "requires the [definition-change] commit marker or the "
                "type:definition-change PR label (Constitution Article I; "
                "glossary change policy)."),
            "pins": manifest,
        }, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8")


def check_pins(pins: dict[str, dict[str, str]]) -> None:
    if not HASHES_FILE.exists():
        err("amendment guard: governance/canon_hashes.json missing; run "
            "scripts/constitution_lint.py --update")
        return
    manifest = json.loads(HASHES_FILE.read_text(encoding="utf-8"))["pins"]
    for term, pin in pins.items():
        pinned = manifest.get(term)
        if pinned is None:
            err(f"amendment guard: no pin recorded for '{term}'; run "
                f"--update and carry the {DEFINITION_CHANGE_MARKER} marker")
            continue
        if pinned["sha256"] != pin["sha256"]:
            err(f"amendment guard: frozen definition text of '{term}' "
                f"diverges from its pin. If this is a declared amendment, "
                f"run scripts/constitution_lint.py --update and carry the "
                f"{DEFINITION_CHANGE_MARKER} commit marker (or the "
                f"{DEFINITION_CHANGE_LABEL} PR label); otherwise revert "
                f"(Constitution Article I).")
        snap = ROOT / pin["snapshot"]
        if not snap.exists():
            err(f"amendment guard: snapshot file missing: {pin['snapshot']}")
        elif snap.read_text(encoding="utf-8").strip() != pin["text"]:
            err(f"amendment guard: snapshot {pin['snapshot']} does not match "
                f"the glossary; run --update")
    for term in manifest:
        if term not in pins:
            err(f"amendment guard: pinned term '{term}' no longer found in "
                f"the glossary (Article I: canonical terms may not be "
                f"removed without a successor framework)")


def git(*args: str) -> str:
    return subprocess.run(["git", *args], cwd=ROOT, check=True,
                          capture_output=True, text=True).stdout


def check_pr_guards() -> None:
    """PR-only guards: marker required to change pins; version bump +
    rationale required to change the Constitution."""
    event_name = os.environ.get("GITHUB_EVENT_NAME", "")
    event_path = os.environ.get("GITHUB_EVENT_PATH", "")
    if event_name != "pull_request" or not event_path:
        return
    try:
        event = json.loads(Path(event_path).read_text(encoding="utf-8"))
        base_sha = event["pull_request"]["base"]["sha"]
        labels = {l["name"] for l in event["pull_request"].get("labels", [])}
    except (KeyError, json.JSONDecodeError, FileNotFoundError) as exc:
        warn(f"amendment guard: could not read PR event payload ({exc}); "
             f"PR-only guards skipped")
        return
    try:
        changed = set(git("diff", "--name-only",
                          f"{base_sha}...HEAD").splitlines())
        messages = git("log", "--format=%B", f"{base_sha}..HEAD")
    except subprocess.CalledProcessError as exc:
        warn(f"amendment guard: git diff against PR base failed ({exc}); "
             f"PR-only guards skipped")
        return

    marker_present = (DEFINITION_CHANGE_MARKER in messages
                      or DEFINITION_CHANGE_LABEL in labels)
    pin_paths = {"governance/canon_hashes.json"} | {
        f"governance/canon/{slugify(t)}.txt"
        for terms in CANONICAL.values() for t in terms}
    if (changed & pin_paths) and not marker_present:
        err(f"amendment guard: this PR changes pinned canon "
            f"({', '.join(sorted(changed & pin_paths))}) without the "
            f"{DEFINITION_CHANGE_MARKER} commit marker or the "
            f"{DEFINITION_CHANGE_LABEL} label. Declare the amendment "
            f"(Article I / Amendment Procedure) or revert.")

    if CONSTITUTION_REL in changed:
        new_text = (ROOT / CONSTITUTION_REL).read_text(encoding="utf-8")
        try:
            old_text = git("show", f"{base_sha}:{CONSTITUTION_REL}")
        except subprocess.CalledProcessError:
            old_text = ""
        ver_re = re.compile(r"\*\*Version\s+([0-9][0-9.]*)")
        old_ver = ver_re.search(old_text)
        new_ver = ver_re.search(new_text)
        bumped = bool(old_ver and new_ver
                      and old_ver.group(1) != new_ver.group(1))
        if bumped:
            if "Amendment Rationale" not in new_text:
                err("amendment guard: constitution version bumped without "
                    "an 'Amendment Rationale' section (Amendment Procedure "
                    "items 2-3)")
        elif NON_NORMATIVE_MARKER not in messages:
            err(f"amendment guard: docs/constitution.md edited without a "
                f"version bump. Amendments require a version increment plus "
                f"an 'Amendment Rationale' section; formatting/link-only "
                f"changes must carry the {NON_NORMATIVE_MARKER} commit "
                f"marker.")


# --------------------------------------------------------------------------
# Check 4: per-page evidence markers  ·  Check 5: anti-capture scan
# --------------------------------------------------------------------------

def check_page_markers() -> None:
    for page in sorted(DOCS.rglob("*.md")):
        rel = page.relative_to(DOCS).as_posix()
        if rel in MARKER_ALLOWLIST:
            continue
        text = page.read_text(encoding="utf-8")
        if not PAGE_MARKER_RE.search(text):
            err(f"docs/{rel}: no evidence-layer marker found. Add an inline "
                f"[L0]..[L4] tag at the claim site or an 'Evidence: Ln' "
                f"status line (Article IV).")


def check_overclaims() -> None:
    for page in sorted(DOCS.rglob("*.md")):
        rel = page.relative_to(DOCS).as_posix()
        if rel in OVERCLAIM_ALLOWLIST:
            continue
        text = page.read_text(encoding="utf-8")
        for lineno, line in strip_fences(text):
            for pattern in OVERCLAIM_PATTERNS:
                if re.search(pattern, line, flags=re.I):
                    warn(f"docs/{rel}:{lineno}: possible Article VI "
                         f"overclaim (pattern: {pattern}): {line.strip()!r} "
                         f"— advisory only; a human decides.")


# --------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--update", action="store_true",
                        help="regenerate governance/canon pins from the "
                             "current glossary")
    args = parser.parse_args()

    gloss_text = GLOSSARY.read_text(encoding="utf-8")
    sections = check_glossary_structure(gloss_text)
    pins = compute_pins(sections)

    if args.update:
        write_pins(pins)
        print(f"wrote {HASHES_FILE.relative_to(ROOT)} and "
              f"{len(pins)} snapshots under governance/canon/")
        return 0

    check_pins(pins)
    check_pr_guards()
    check_links()
    check_page_markers()
    check_overclaims()

    in_actions = bool(os.environ.get("GITHUB_ACTIONS"))
    for w in warnings:
        print(f"::warning::{w}" if in_actions else f"WARNING: {w}")
    for e in errors:
        print(f"::error::{e}" if in_actions else f"ERROR: {e}")
    print(f"\nconstitution-lint: {len(errors)} error(s), "
          f"{len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
