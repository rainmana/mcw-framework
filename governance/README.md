# governance/ — pinned canon

This directory is the mechanical anchor for Constitution Article I
(Definition Immutability), produced and verified by
`scripts/constitution_lint.py` (see `docs/constitution_as_code.md`, Phase 0).

## Contents

- **`canon/*.txt`** — one plain-text snapshot per canonical construct,
  containing only its **frozen fields** as defined by the glossary change
  policy (Definition text, Key properties/Key characteristic lists,
  "What it is not" exclusion lists, H/R/D/M scale semantics). Amendable
  fields (Type lines, Layer 0 glosses, examples, early signals, key-danger
  notes, evidence tags, status lines) are excluded, so they can evolve
  without tripping the guard.
- **`canon_hashes.json`** — SHA-256 of each snapshot, checked in CI on every
  push and pull request.

## How the guard works

1. CI re-extracts the frozen fields from `docs/glossary.md` and compares
   hashes against `canon_hashes.json`. Any divergence fails.
2. Updating the pins (i.e., amending canon) is allowed only when the change
   carries the `[definition-change]` commit marker or the
   `type:definition-change` PR label, and is expected to follow the
   Amendment Procedure (prior text preserved, rationale recorded). Use the
   "Definition change" issue form.
3. Removing a pinned term outright always fails: Article I's unremovable
   core means a vocabulary that loses canonical terms is a successor
   framework, not this one.

To regenerate after a declared amendment:

```
python scripts/constitution_lint.py --update
```

## Downstream consumers

Implementations that freeze this vocabulary (e.g., `rainmana/smolbrain`,
which encodes it as typed invariants) can vendor `canon/*.txt` +
`canon_hashes.json` and compare against this repository in their own CI, so
upstream definitional drift fails their build rather than silently
propagating. That pinning test lives downstream; this directory is its
source of truth.
