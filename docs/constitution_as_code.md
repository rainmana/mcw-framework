# Constitution-as-Code: Gating MCW with Software Lifecycle Tooling

**Status:** Proposal · v0.1 · June 2026
**Relationship to the framework:** Governance instrument. This document does not
modify any canonical construct (see [Constitution](constitution.md), Article I). It
proposes a *process* for enforcing the Constitution as the framework is cited,
extended, forked, and challenged.

---

## Motivation

The [MCW Constitution](constitution.md) defines eight binding invariants whose entire
purpose is to keep cross-study comparison possible as the framework spreads. But a
constitution that is only prose is *aspirational*: nothing stops a contribution — a
pull request, a fork, an extension paper's companion repo — from silently redefining
a canonical term (Article I), citing a toy-experiment *design* as a *result*
(Article IV), or compressing a construct in a way that drops its falsification
condition (Article VII).

Software engineering solved an isomorphic problem decades ago. Codebases also have
invariants that must survive many contributors, and the discipline that protects them
is the **software development lifecycle (SDLC)**: version control, branch protection,
required reviews, templated change requests, automated checks, and explicit
definitions of "done." The Constitution's invariants are, structurally, *lint rules
for a scientific vocabulary.*

This document proposes treating them that way:

1. **A GitHub-native gating method** — what existing GitHub SDLC features can enforce today, with zero custom software.
2. **A gap analysis** — the invariants GitHub *cannot* check, and why.
3. **A GitHub App proposal** — a "Constitution Sentinel" that closes the gap with LLM-backed semantic checks, designed to respect the framework's own epistemic humility.

A guiding constraint, borrowed from the framework itself: **the enforcement tool must
not overclaim** (Article VI). A linter for an L0–L1 framework must not pretend to L4
certainty. Mechanical violations may hard-block; judgment calls escalate to a human.

---

## Part 1 — The GitHub-native gating method

Each Constitution Article maps to one or more existing GitHub controls. The table
below is the core deliverable: a control matrix.

| Article | Invariant | GitHub-native control(s) | Enforcement strength |
|---|---|---|---|
| **I — Definition Immutability** | Canonical terms fixed in glossary; departures must be declared | `CODEOWNERS` makes `docs/glossary.md` + `docs/constitution.md` require author review on any change; a "definition-change" PR label is required to touch the definitions block; a mechanical Action fails the PR if glossary definition anchors changed without the label | **Procedural** (the *fact* of change is gated; the *semantics* are not — see Part 2) |
| **II — Layering Invariant** | No construct at layer N without a layer N−1 equivalent | Issue template "Extension Proposal" forces a "Layer 0 plain-language statement" field; PR checklist requires a traceability claim | **Procedural only** |
| **III — Substrate Independence** | Restrictions to a substrate must be declared as scope, not definition | PR/issue template requires a "substrate scope" declaration field; label `scope:substrate-specific` | **Procedural only** |
| **IV — Epistemic Floor** | No claim above its evidence layer | Required `evidence:L0`–`evidence:L4` label on any PR/issue making an empirical claim; Action fails if an "empirical-claim" doc lacks an evidence-layer marker string | **Mechanical (presence) + Procedural** |
| **V — Extension Protocol** | Extensions declared, non-contradictory, falsifiable, traceable | "Extension Proposal" issue/PR template with four required fields (declaration, non-contradiction statement, falsification condition, lower-layer trace); Action fails if any field is empty | **Mechanical (completeness) + Procedural** |
| **VI — Anti-Capture** | MCW is not a product/system/model feature | Action scans changed prose for overclaim patterns ("implements MCW", "MCW-aware", "solves the MCW problem", "our \<system\> reduces MCW") and flags for review | **Mechanical (pattern) — high false-positive, advisory** |
| **VII — Compression Invariance** | Summaries must keep falsification conditions, evidence level, exclusion list | Action requires that any file tagged as a summary contains a falsification-condition marker, an evidence-layer marker, and a "what it is not" block | **Mechanical (presence only)** |
| **VIII — Scope Boundaries** | Extensions into adjacent layers need justification | PR template "adjacent-layer justification" field; label `scope:adjacent-layer` triggers required review | **Procedural only** |
| **Amendment Procedure** | Version bump + prior-text + rationale; some Articles unremovable | Action fails a PR that edits `constitution.md` without incrementing the version header and adding an "Amendment Rationale" section; CODEOWNERS forces author approval | **Mechanical + Procedural** |

### Concrete GitHub-native artifacts to add

- **`.github/CODEOWNERS`** — assign canonical files to the author:
  ```text
  /docs/glossary.md       @rainmana
  /docs/constitution.md   @rainmana
  ```
  Combined with branch protection's "require review from Code Owners," this makes
  Article I and the Amendment Procedure *procedurally* unbypassable.
- **Branch protection on `main`** — require a PR, require the governance status checks
  to pass, require Code Owner review, require linear history.
- **Issue Forms** (`.github/ISSUE_TEMPLATE/`):
  - `extension_proposal.yml` — Article V's four conditions as required fields.
  - `definition_change.yml` — Article I departure-declaration in the canonical form.
  - `empirical_claim.yml` — Article IV evidence-layer dropdown (L0–L4) + supporting data.
- **PR template** — a Constitution checklist:
  ```markdown
  ## Constitution compliance
  - [ ] No canonical term is redefined (Article I), OR a departure is declared below.
  - [ ] Any new construct traces to a Layer 0 statement (Article II).
  - [ ] Substrate restrictions are declared as scope, not definition (Article III).
  - [ ] Every empirical claim declares its evidence layer L0–L4 (Article IV).
  - [ ] Extensions are declared, non-contradictory, falsifiable, traceable (Article V).
  - [ ] No anti-capture overclaims (Article VI).
  - [ ] Summaries preserve falsification conditions + exclusions (Article VII).
  - [ ] Adjacent-layer extensions are justified (Article VIII).
  ### Declared departures (if any)
  > This work uses a modified definition of [term]. Canonical: [cite]. Modification: [...]. Rationale: [...].
  ```
- **Label taxonomy**: `article:I`…`article:VIII`, `evidence:L0`…`evidence:L4`,
  `type:extension`, `type:definition-change`, `scope:substrate-specific`,
  `scope:adjacent-layer`, `status:needs-departure-declaration`, `governance:blocked`.
- **Mechanical Actions** (`.github/workflows/constitution-lint.yml`):
  - glossary structural lint — every canonical construct still present; each has a
    "what it is not" exclusion block (Article VII / Article I structural floor).
  - anchor/link integrity between `constitution.md` and `glossary.md`.
  - amendment guard — editing `constitution.md` requires a version bump + rationale.
  - marker-presence checks — empirical docs carry an evidence-layer marker; summaries
    carry falsification + exclusion markers.
- **A governance Project board** — views grouped by Article, by evidence layer, and by
  status, so contributions are visibly gated rather than merged on vibes.

This much is buildable today with **only YAML and Markdown** — no service to operate.

---

## Part 2 — Gap analysis: what GitHub cannot do

Every "Procedural only" and "presence only" row above shares the same ceiling:
**GitHub can verify that a declaration *exists*; it cannot verify that the declaration
is *true*.** The Constitution's hardest invariants are semantic — they require reading
comprehension and judgment. Specifically:

| Gap | The semantic question GitHub can't answer | Article |
|---|---|---|
| **Undeclared redefinition** | The glossary text changed — but did the *meaning* change? If so, is the departure declaration adequate, or cosmetic? | I |
| **Fake traceability** | A "Layer 0 statement" field is filled — but does it actually compress *this* construct, or is it unrelated boilerplate? | II |
| **Overclaiming** | A claim is stated — does the supporting evidence actually reach the declared layer, or is an L1 anecdote dressed as L3? | IV |
| **Extension validity** | The four fields are filled — but is the extension genuinely non-contradictory and genuinely falsifiable, or falsifiable-in-name-only? | V |
| **Anti-capture in prose** | Pattern matching flags "implements MCW" — but misses "our architecture maintains shared understanding across turns," which is the same overclaim in disguise; and false-flags legitimate quoted critique | VI |
| **Compression fidelity** | A falsification-condition marker is present — but does the summary actually *preserve* the original condition, or did it keep the heading and gut the content? | VII |
| **Adjacent-layer justification** | A justification field is filled — does the coordination-layer lens actually add value, or is it scope creep with a paragraph stapled on? | VIII |

These are not edge cases; they are the *substance* of the Constitution. A vocabulary
collapses through plausible-looking contributions that pass every mechanical check
while quietly violating meaning. Mechanical gating raises the floor; it does not reach
the ceiling.

This is precisely the seam where an LLM-backed check earns its keep — and, fittingly,
it is itself a coordination problem between a human reviewer and an automated reader.

---

## Part 3 — Proposed GitHub App: "Constitution Sentinel"

### Concept

A GitHub App, installable on the canonical repo and on forks, that runs as a **required
status check** on pull requests and as an **issue triager**. It is backed by a language
model that loads the Constitution and glossary as ground truth and performs the
*semantic* checks from Part 2 that mechanical tooling cannot.

Working name: **Constitution Sentinel** (alt: *Canon Keeper*, *MCW Warden*). It is
deliberately *not* named or marketed as "MCW-aware" — per Article VI, a tool does not
implement MCW. It is a linter for a document, nothing more, and says so.

### What it checks (each maps to a Part 2 gap)

1. **Definition-drift detector.** On any diff to `glossary.md`/`constitution.md`,
   compare changed definitions against the canonical baseline and judge whether meaning
   changed. If it did and no adequate departure declaration is present → flag.
2. **Layer-trace verifier.** For new constructs, judge whether the provided Layer 0
   statement genuinely compresses the higher-layer construct (Article II).
3. **Epistemic-floor / overclaim detector.** For each empirical claim, judge whether
   the supporting data reaches the *declared* evidence layer; flag claims stated above
   their support (Article IV) — the framework's most important and most violated rule.
4. **Anti-capture scanner.** Read prose for capability-claim-dressed-as-coordination
   and product/marketing overclaims, including paraphrases pattern-matching misses
   (Article VI).
5. **Compression-invariance checker.** For summaries, judge whether falsification
   conditions, evidence level, and exclusion lists were *preserved in substance*
   (Article VII), not merely whether headings exist.
6. **Extension-protocol validator.** Judge declaration, non-contradiction,
   falsifiability, and traceability of proposed extensions (Article V).

### Design principles (so the tool obeys the framework it guards)

- **Mechanical violations hard-block; judgment calls escalate.** The App never fails a
  PR on a semantic verdict *alone*. A semantic flag posts an inline review comment and
  sets the check to "action required → human review," not "failed." Only mechanical
  rules (missing version bump, empty required field, missing exclusion block) hard-fail.
  This mirrors StoryLoom's *proportional gates* and prevents the linter from
  overclaiming certainty it does not have.
- **Every verdict is grounded and cited.** Output references the specific Article and
  quotes the offending text and the canonical text it conflicts with. No bare verdicts.
- **Reproducibility.** Model id and prompt version are pinned and recorded in the check
  output (Article IV/VII spirit: claims carry their provenance). Re-running on the same
  diff yields a comparable, auditable result.
- **Uncertainty is first-class.** Verdicts are `pass | flag | uncertain`, never a forced
  binary. `uncertain` routes to the human, who is the authority (the framework is L0–L1;
  the reviewer outranks the tool).
- **Self-non-claim.** The App's README must state: "This App enforces document
  invariants. It does not implement, embody, or measure MCW (Constitution Article VI)."

### Architecture sketch

```text
GitHub (PR / issue webhook)
        │
        ▼
Constitution Sentinel (GitHub App)
  ├── event router (pull_request, issues, issue_comment)
  ├── context loader  → pins canonical constitution.md + glossary.md at base ref
  ├── diff extractor  → changed docs, claims, summaries
  ├── semantic checker → LLM with Constitution as system context; per-Article prompts
  ├── verdict composer → Check Run (per-Article pass/flag/uncertain) + inline comments
  └── status setter    → commit status that branch protection can require
        │
        ▼
Pinned model API (provider-agnostic; model + prompt version recorded)
```

- **Config file** `.mcw/constitution.yml` in each repo: maps Articles → enabled checks
  → severity (`block` vs `advisory`), and pins the canonical source paths/refs. Forks
  can tune severity but cannot silently disable Article I or IV without it showing in
  the config diff (which CODEOWNERS gates).
- **State:** mostly stateless per-PR; optional store for verdict history/metrics.

### Phased rollout (build-vs-buy)

| Phase | Deliverable | Operating cost |
|---|---|---|
| **0** | GitHub-native only: CODEOWNERS, branch protection, issue forms, PR template, mechanical Actions (Part 1) | None — YAML/Markdown only |
| **1** | A CI job (GitHub Actions) that calls an LLM API on PR diffs and posts an **advisory** governance comment | API usage only; no service to host |
| **2** | Promote the semantic check to a **required** status check; add issue triage/labeling | API usage only |
| **3** | Package as a distributable **GitHub App** installable on forks, so the *ecosystem* can self-gate | Hosted App + API |

Phase 1 captures most of the value with no hosted infrastructure — a reusable workflow
that any fork can copy. Phase 3 is what actually serves the Constitution's deepest goal:
if forks and citing repos can install the same Sentinel, **definitional drift across the
ecosystem becomes measurable and resistible**, which is the entire point of having a
Constitution.

---

## Part 4 — Does the governance method itself work? (falsification)

In keeping with Article IV and Article V, the governance method makes a falsifiable
prediction about *itself*:

> **Hypothesis.** Constitution-as-code gating reduces undeclared invariant violations
> reaching `main` relative to ungated contribution.
>
> **Observable.** Track, per merged PR, the rate of (a) undeclared term redefinitions,
> (b) claims stated above their evidence layer, (c) summaries that dropped falsification
> conditions. Compare gated vs. ungated periods/forks.
>
> **Falsification.** If gating produces no measurable reduction in (a)–(c) — or if the
> review burden so suppresses contribution that the framework stops evolving — the
> method has failed and should be simplified back toward Phase 0, or abandoned.

Evidence layer of *this proposal*: **L0 — Illustration.** It is a design, not a result.
No gating run has been piloted. Stated explicitly per Article IV.

---

## Relationship to StoryLoom

This is the research-governance instance of the same philosophy used to build the
StoryLoom application (`rainmana/storyloom`): **proportional gates, evidence over vibes,
hard rules where the blast radius is large, human judgment where automation would
overclaim.** One project gates a codebase; this one gates a vocabulary. The shared move
is using ordinary SDLC tooling to make invariants enforceable instead of merely stated.
