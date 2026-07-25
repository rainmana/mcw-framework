# mcw-engine — Integration Note

**Status:** integration note · Evidence: L0

**mcw-engine** ([github.com/rainmana/mcw-engine](https://github.com/rainmana/mcw-engine)) is **a Rust library workspace whose types, build process, and runtime encode this framework's frozen canon as enforced invariants**. Per Constitution [Article VI](../../docs/constitution.md#article-vi--anti-capture), that is the strongest claim this note makes: mcw-engine does not implement MCW (systems are initialization artifacts or optimization targets; they do not implement MCW), its governed inference does not solve the MCW problem, and no claim of reduced degradation is made or available at the current evidence layer. The engine is a coordination-layer *instrument* — pinned vocabulary, ledgered Information Units, repair operations as API, heuristic observables tagged at their evidence layer — and its own documentation and advisory scanner enforce this framing.

---

## Declared scope restriction (Article III)

The engine restricts the framework's constructs to a specific substrate: **one human and one AI actor per session, text modality, mediated by chat-completion inference APIs**. Per [Article III](../../docs/constitution.md#article-iii--substrate-independence):

1. This is a **scope constraint, not a definitional revision** — all canonical terms are used exactly as frozen in [`docs/glossary.md`](../../docs/glossary.md) and pinned in [`governance/canon/`](../../governance/canon/).
2. Nothing the engine records or suggests **tests the general framework** — only this substrate-specific instance.
3. Engine-derived observations will **not be presented as evidence for or against the general framework** without explicit generalizability analysis. Everything the engine computes automatically is tagged L0 in its own API.

Multi-actor sessions are deliberately unsupported: the canonical MCW is scoped to HCW–ACW coupling (Article III, v1.1), and a multi-agent generalization would be an [Article V](../../docs/constitution.md#article-v--extension-protocol) extension with its own falsification conditions, not a feature flag.

---

## How the engine consumes this repository

mcw-engine follows the downstream-consumer pattern described in [`governance/README.md`](../../governance/README.md), and pushes it one step further than CI:

- It **vendors** `governance/canon/*.txt` and `governance/canon_hashes.json` at a pinned upstream commit of this repository (recorded in `crates/mcw-canon/vendor/UPSTREAM`).
- Its **build script re-verifies the SHA-256 pins** (same scheme as [`scripts/constitution_lint.py`](../../scripts/constitution_lint.py): hash of the trimmed frozen text). A divergent snapshot **fails compilation**, quoting Article I.
- At **runtime**, `Canon::verify()` re-hashes the texts embedded in the binary and returns a proof token (`VerifiedCanon`) that every session-opening and inference API requires. Unverified canon is unrepresentable in the type system, not merely discouraged.
- Its **CI** compares the vendored pins against this repository's `main` on every push and weekly, so a declared amendment upstream surfaces as a red build downstream, resolved only by deliberate re-vendoring.

Other framework artifacts the engine operationalizes, with their canonical caveats attached in code and docs:

| Framework artifact | Engine treatment |
|---|---|
| Six failure modes, five repair operations, four proxies (Article I) | Sealed Rust enums; adding a variant requires an upstream amendment and re-vendor |
| [Failure↔repair mapping and decision tree](../../docs/failure_repair_mapping.md) | Typed mapping with `CanonDerived` / `Inferred` / `ExtensionGap` provenance; the tree returns "3/4-indeterminate" rather than guessing |
| Constraint Disclosure, Repair-Norm Restoration (declared extensions) | Present as extension-typed operations, never conflated with the canonical five; Article V paperwork embedded as data |
| Evidence layers L0–L4 (Article IV) | `Claim` type displays its layer everywhere; assertion above support is a typed error |
| Compression invariance (Article VII) | Empirical claims cannot be compressed without falsification conditions; summaries carry IU lineage so decompression stays possible |
| [Minimal initialization template](../../README.md#appendix-minimal-mcw-aware-system-prompt-template) | Rendered and recorded at turn 0, tagged `initialization-artifact` — configuration is never confused with exchange |
| [Anchored H/R/D/M rubrics](../../docs/experiments/hrdm_rubrics.md) | Only the mechanical parts (late-discovery counting, dedicated-repair-turn counting, the R_ev split) are computed, and only as L0 *suggestions to a rater* |

---

## Honest returns

The engine can eventually return observations to the framework — ledgers are exactly the instrumented setting the decision tree's questions 3–4 need (off-turn advancement and constraint disclosure are recorded events, not conjectures). Any such return would enter at L1 at best, via the framework's own instruments, and nothing of the sort exists today.

---

*This note documents a downstream consumer. It amends nothing: no canonical term is redefined, and the pinned canon remains this repository's [`governance/`](../../governance/) directory.*
