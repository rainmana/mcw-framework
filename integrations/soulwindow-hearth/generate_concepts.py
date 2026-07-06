#!/usr/bin/env python3
"""Generate concepts.v1.json — the machine-readable concept export that
SoulWindow's Hearth mode ingests.

Reads governance/canon_hashes.json plus each pinned snapshot file in
governance/canon/ and writes concepts.v1.json next to this script. Each
concept carries its frozen SHA-256 (verified against the snapshot text
before export, using the same hashing convention as
scripts/constitution_lint.py: UTF-8 bytes of the stripped frozen text) and
the verbatim snapshot file text.

Usage:
  python3 integrations/soulwindow-hearth/generate_concepts.py [upstream_commit]

If upstream_commit is omitted, `git rev-parse HEAD` of this repository is
recorded. Stdlib only.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
HASHES_FILE = ROOT / "governance" / "canon_hashes.json"
OUT_FILE = HERE / "concepts.v1.json"


def main() -> None:
    if len(sys.argv) > 1:
        upstream_commit = sys.argv[1]
    else:
        upstream_commit = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()

    pins = json.loads(HASHES_FILE.read_text(encoding="utf-8"))["pins"]

    concepts = []
    for term, pin in pins.items():
        snapshot_path = pin["snapshot"]
        text = (ROOT / snapshot_path).read_text(encoding="utf-8")
        digest = hashlib.sha256(text.strip().encode("utf-8")).hexdigest()
        if digest != pin["sha256"]:
            sys.exit(f"error: snapshot {snapshot_path} does not match its "
                     f"frozen sha256 for '{term}'; refusing to export from "
                     f"a diverged tree (Constitution Article I).")
        concepts.append({
            "term": term,
            "category": pin["category"],
            "snapshot_path": snapshot_path,
            "frozen_sha256": pin["sha256"],
            "definition_text": text,
        })

    concepts.sort(key=lambda concept: concept["term"])

    payload = {
        "_generated_by": "integrations/soulwindow-hearth/generate_concepts.py",
        "upstream_commit": upstream_commit,
        "concepts": concepts,
    }

    with OUT_FILE.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True,
                  ensure_ascii=False)
        handle.write("\n")


if __name__ == "__main__":
    main()
