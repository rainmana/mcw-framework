# SoulWindow · Hearth Mode — Integration Note

**Status:** integration note · Evidence: L0

SoulWindow's Hearth mode is **an application whose design is informed by the MCW framework's failure taxonomy and repair operations**. Per Constitution [Article VI](../../docs/constitution.md#article-vi--anti-capture), that is the strongest claim this note makes: SoulWindow does not implement MCW (systems are initialization artifacts or optimization targets; they do not implement MCW), its prompts do not solve the MCW problem, its models have no MCW capability, and no claim of reduced degradation is made or available at the current evidence layer. The framework supplied vocabulary and design pressure; the application supplies nothing back but, potentially, observations (see [Honest returns](#honest-returns), below).

---

## Declared scope restriction (Article III)

This integration restricts the framework's constructs to a specific substrate: **one human and one AI companion in a local-first journaling game**, text modality, long-horizon sessions. Per [Article III](../../docs/constitution.md#article-iii--substrate-independence):

1. This is a **scope constraint, not a definitional revision** — all canonical terms are used exactly as frozen in [`docs/glossary.md`](../../docs/glossary.md) and pinned in [`governance/canon/`](../../governance/canon/).
2. Nothing observed inside Hearth **tests the general framework** — only this substrate-specific instance.
3. Substrate-specific findings will **not be presented as evidence for or against the general framework** without explicit generalizability analysis.

---

## What SoulWindow / Hearth is

**SoulWindow** ([github.com/clearically/SoulWindow](https://github.com/clearically/SoulWindow)) is a local-first journaling application built with Tauri and Rust. Journal entries, companion state, and interaction history live on the user's machine; nothing depends on a hosted service holding the record of the practice. An AI companion participates in the journaling rather than merely storing it.

**Hearth mode** is SoulWindow's long-form companion mode: journaling plays as a light game loop between the human and one companion, with session-opening exchanges, in-session beats, and closing rituals. Its design premise — taken from this framework's failure taxonomy — is that in a months-long two-party practice, the expensive failures are coordination failures, so the game loop makes coordination upkeep a first-class mechanic instead of invisible overhead.

---

## How the application consumes this repository

Hearth follows the downstream-consumer pattern described in [`governance/README.md`](../../governance/README.md):

- It **vendors** `governance/canon/*.txt`, `governance/canon_hashes.json`, and `prompts/mcw_initialization.txt` at a **pinned upstream commit** of this repository.
- Its CI **re-verifies the SHA-256 hashes** of the vendored snapshot files against `canon_hashes.json`, so upstream definitional drift fails the downstream build rather than silently propagating. The pinning test lives downstream; this repository remains the source of truth.
- [`concepts.v1.json`](concepts.v1.json) in this directory is the machine-readable export the application ingests. It is generated from the canon snapshots by [`generate_concepts.py`](generate_concepts.py) and records the upstream commit it was generated at; regenerate it only from a clean tree.

The vendored initialization prompt is used as exactly what the framework says such artifacts are: a preloaded IU bundle that biases early coordination. It is an initialization aid, not a coordination solution, and Hearth's in-play mechanics — not the prompt — carry the ongoing maintenance burden.

---

## Derivation table

Each Hearth mechanic is *informed by* a framework concept; the arrow reads "derived from," not "implements."

| Hearth mechanic (application) | ← Framework concept (this repository) |
|---|---|
| **Session sync exchange** — each session opens with both parties externalizing what changed off-turn since last time | [Asymmetric State Advancement](../../docs/glossary.md#asymmetric-state-advancement) / [Synchronization](../../docs/glossary.md#synchronization) |
| **Recap ritual cadence** — periodic scripted restatement of goals, threads, and assumptions | [Drift](../../docs/glossary.md#drift-silent-desynchronization) / [Re-grounding](../../docs/glossary.md#re-grounding) |
| **Beat ratification probes** — before a narrative beat is locked in, each party paraphrases it; divergent paraphrases block ratification | [False Alignment](../../docs/glossary.md#false-alignment) / [Disambiguation](../../docs/glossary.md#disambiguation) |
| **Layered decompressible memory** — journal summaries retain links back to the entries they compress, so lost distinctions can be re-expanded on demand | [Overcompression](../../docs/glossary.md#overcompression) / [Decompression](../../docs/glossary.md#decompression) |
| **Salience declaration** — the player can mark what matters most right now, and the companion restates its own weighting | [Re-weighting](../../docs/glossary.md#re-weighting) |
| **Constraint naming** — the companion names when a rule is shaping its behavior, even when the rule's content cannot be shared | [Constraint Opacity](../../docs/glossary.md#constraint-opacity) / Constraint Disclosure — a **declared extension**, per [failure–repair mapping](../../docs/failure_repair_mapping.md#proposed-extension-constraint-disclosure) |
| **Corrections-welcome norms** — the loop periodically re-authorizes clarifying questions and corrections in both directions | [Repair Suppression](../../docs/glossary.md#repair-suppression) / Repair-Norm Restoration — a **declared extension**, per [failure–repair mapping](../../docs/failure_repair_mapping.md#proposed-extension-repair-norm-restoration) |
| **Ordinal H/R/D/M touchstone** — an optional end-of-session self-rating on 0–3 ordinal scales, kept as a journal artifact, never scored as a performance metric | The four measurement proxies: [H](../../docs/glossary.md#mcw-health-h), [R](../../docs/glossary.md#repair-cost-r), [D](../../docs/glossary.md#drift-rate-d), [M](../../docs/glossary.md#misattribution-m) |

The two extension-derived rows inherit the extensions' status: proposed under [Article V](../../docs/constitution.md#article-v--extension-protocol) with registered falsification conditions, not canon. If the extensions are ever withdrawn upstream, the corresponding mechanics lose their derivation, not their existence.

---

## Honest returns

This integration makes **no empirical claims today** `[L0]`. The existence of a shipped mechanic is evidence of nothing beyond recognizability of the constructs it was derived from. No play data has been collected, no proxies have been scored by anyone but their own subject, and nothing in this directory upgrades any framework claim's evidence layer. If sustained play surfaces observations worth reporting, they would enter this repository as `[L1]` practitioner observations — positionality-biased, not generalizable — through normal governance (issues and pull requests under the [Article IV](../../docs/constitution.md#article-iv--epistemic-floor) floor), and would be subject to the same scrutiny as any other practitioner report.

## Falsification-shaped note

In the spirit of [Article V](../../docs/constitution.md#article-v--extension-protocol), this integration states what would count against the framework rather than for it. The framework's registered prediction is that shared coordination state decays without maintenance and that initialization artifacts cannot substitute for ongoing repair. Hearth is, incidentally, a long-duration natural probe of that prediction: **if long journaling play showed recurring re-grounding to be unnecessary despite good initialization** — sessions staying coordinated over long horizons with recap rituals skipped and no drift symptoms accumulating — **that would count against the framework's registered prediction**, and should be reported upstream as such, not quietly filed as a Hearth-specific quirk. A framework that only ever hears confirmations from its integrations is not being tested by them.

---

*This is an integration note, not a canonical framework document. Nothing in this directory amends, extends, or reinterprets canon; the frozen definitions live in [`docs/glossary.md`](../../docs/glossary.md) and [`governance/canon/`](../../governance/canon/).*
