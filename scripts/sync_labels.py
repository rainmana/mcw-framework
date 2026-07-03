#!/usr/bin/env python3
"""Sync the repository's GitHub labels from .github/labels.yml.

Part of Constitution-as-Code Phase 0 operations: the label taxonomy is
versioned in git (the source of truth), and this script pushes it to the
repository's label settings so the two cannot drift apart silently.

Deliberately non-destructive: labels present in the repo but absent from
labels.yml are left alone (report-only), so ad-hoc labels are never deleted
by automation. Creating and updating are idempotent.

Runs in CI via .github/workflows/labels-sync.yml with the built-in
GITHUB_TOKEN (permissions: issues: write). Requires PyYAML.

Usage:
  GITHUB_TOKEN=... GITHUB_REPOSITORY=owner/repo python scripts/sync_labels.py
"""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
LABELS_FILE = ROOT / ".github" / "labels.yml"
API = "https://api.github.com"


def request(method: str, url: str, token: str, body: dict | None = None):
    data = json.dumps(body).encode("utf-8") if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    if data is not None:
        req.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(req) as resp:
        payload = resp.read()
        return json.loads(payload) if payload else None


def existing_labels(repo: str, token: str) -> dict[str, dict]:
    labels: dict[str, dict] = {}
    page = 1
    while True:
        batch = request(
            "GET", f"{API}/repos/{repo}/labels?per_page=100&page={page}",
            token)
        if not batch:
            break
        for label in batch:
            labels[label["name"]] = label
        if len(batch) < 100:
            break
        page += 1
    return labels


def main() -> int:
    token = os.environ.get("GITHUB_TOKEN")
    repo = os.environ.get("GITHUB_REPOSITORY")
    if not token or not repo:
        print("GITHUB_TOKEN and GITHUB_REPOSITORY must be set",
              file=sys.stderr)
        return 2

    desired = yaml.safe_load(LABELS_FILE.read_text(encoding="utf-8"))
    if not isinstance(desired, list):
        print(f"{LABELS_FILE}: expected a list of labels", file=sys.stderr)
        return 2

    current = existing_labels(repo, token)
    created = updated = unchanged = 0

    for label in desired:
        name = label["name"]
        color = label.get("color", "ededed").lstrip("#")
        description = label.get("description", "")
        have = current.get(name)
        if have is None:
            request("POST", f"{API}/repos/{repo}/labels", token,
                    {"name": name, "color": color,
                     "description": description})
            print(f"created  {name}")
            created += 1
        elif (have.get("color", "").lower() != color.lower()
              or (have.get("description") or "") != description):
            encoded = urllib.parse.quote(name, safe="")
            request("PATCH", f"{API}/repos/{repo}/labels/{encoded}", token,
                    {"new_name": name, "color": color,
                     "description": description})
            print(f"updated  {name}")
            updated += 1
        else:
            unchanged += 1

    extra = sorted(set(current) - {l["name"] for l in desired})
    if extra:
        print(f"present in repo but not in labels.yml (left alone): "
              f"{', '.join(extra)}")

    print(f"done: {created} created, {updated} updated, "
          f"{unchanged} unchanged")
    return 0


if __name__ == "__main__":
    sys.exit(main())
