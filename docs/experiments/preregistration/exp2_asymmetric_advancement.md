# Pre-Registration — Experiment 2: Asymmetric State Advancement

**Status:** Pre-registration template · Evidence: L0 (design) · Type: Human ↔ AI · Source: [Toy Experiment 2](../toy_experiments.md#experiment-2-asymmetric-state-advancement) · Shared standards: [pre-registration index](index.md)

---

## Registered hypothesis

> In extended Human ↔ AI collaboration, off-turn human reasoning that is not externalized produces lower MCW health (H↓), costlier repair (R↑), more late discovery (D↑), and more misattribution of coordination failure to model capability (M↑), compared to the same participant externalizing the same off-turn reasoning.

Direction is registered: H↓, R↑, D↑, M↑ in the hidden condition relative to the externalized condition. M **is scored** — this is a Human ↔ AI design and falls inside the [rubrics scope restriction](../hrdm_rubrics.md#m-misattribution-03-per-window-human-ai-only).

The source page used the term "phase lag" without defining it. It is defined here operationally, in full: **phase lag is the number of exchanges between a scripted off-turn reasoning update and the first turn in which its content is externalized to the AI, right-censored at task end if it is never externalized.** The term carries no meaning on this page beyond that count.

## Design

- **Conditions (within-subject, two matched tasks):**
    1. **Hidden condition** — at each scripted off-turn pause, the participant works through a structured reasoning worksheet (re-examining assumptions, revising the plan) and is instructed to resume the conversation *without* telling the AI what changed, proceeding as if the AI already shares the update.
    2. **Externalized condition** — the same worksheet at the same pauses, but the participant is instructed to open the next turn with a 2–4 sentence summary of what changed off-turn. *This is the comparison condition the original falsification condition presupposed ("explicit externalization produces no measurable improvement") but the original design never specified — it described only the treatment.*
- **Disambiguation probe (registered, not optional).** The original outcome D ("reset improves") conceded that this design cannot separate MCW drift from ACW context saturation, then read both as framework-consistent via a "mixed model." That reading is rescinded. After both main tasks, the participant re-attempts the hidden-condition task in a **fresh-session reset arm**: a new AI context initialized with the original task brief only, with an explicit instruction *not* to externalize the accumulated off-turn reasoning, run for 10 exchanges (two scoring windows). If performance improves on reset alone — with nothing externalized — the improvement is attributable to the discarded context, not to hidden HCW/ACW divergence (terms per the [glossary](../../glossary.md)), and that supports the saturation explanation.
- **Tasks.** Two multi-step planning/analysis tasks (A and B), matched on structure, step count, and information load, each completable in 20–30 minutes (~15–20 exchanges), each with three scripted off-turn pauses at fixed exchange positions. The task pack (briefs, worksheets, pause positions, correctness checklists) is frozen before the first session.
- **AI system.** One fixed model and configuration for all sessions, recorded in the task pack, with no MCW-aware system prompt — that manipulation belongs to the system-prompt predictions template ([derivation](../../system_prompt_derivation.md#falsifiable-predictions)).
- **Participants.** Naive participants who know the per-task instructions differ but not the hypothesis or its direction.
- **Minimal N.** 12 participants (within-subject) — a feasibility-based pilot size, powered only for large effects, and stated as such. It yields 24 main-task transcripts, which also meets the rubric corpus floor for the reliability protocol.
- **Counterbalancing.** Condition order (hidden-first vs. externalized-first) crossed with task–condition pairing (A-hidden/B-externalized vs. the reverse): four cells, three participants each.

## Measures

- H, D, and M per 5-exchange window; R per repair episode; R\_ev per 10 exchanges — all per the [anchored rubrics](../hrdm_rubrics.md), scored by two independent raters. Raters receive the worksheets as the record of off-turn IUs: this is what makes the M anchors' "needed IU was never externalized" check and phase-lag scoring verifiable rather than guessed.
- **Blinding limitation (registered now, before any data):** transcripts cannot be fully condition-blinded, because the manipulation is legible in the turns themselves (the externalized condition contains the summaries). Raters are blinded to the hypothesis, the expected-signature tables, and the design pages, and rate from the anchors only. Because this limitation is registered here in advance, it is a stated property of the design, not a logged deviation.
- **Primary outcomes:** per-participant median R across repair episodes, end-of-task H, and mean M across windows, per condition.
- **Manipulation check:** phase lag per scripted update. Hidden-condition phase lags should be long or censored; externalized should be 0–1. A hidden-condition task in which more than one of the three updates is externalized within 2 exchanges is flagged non-compliant; analysis runs on all sessions, with a compliant-only sensitivity analysis registered here.
- **Probe outcomes:** H per window and R per episode in the two post-reset windows, compared against the final two pre-reset windows of the hidden-condition task.
- **Task outcome:** work-product correctness per the frozen checklist (binary).

## Analysis plan

- Hidden vs. externalized on primary outcomes: Wilcoxon signed-rank, α = 0.05, one-sided per the registered direction (H lower, R higher, M higher, D higher in the hidden condition).
- Equivalence (for the falsification decision): TOST on R and on end-of-task H with the shared ±0.5-point margin.
- Probe: Wilcoxon signed-rank on H, post-reset windows vs. final pre-reset windows, one-sided for improvement, α = 0.05.

## Pre-committed outcome interpretation (the losable bets)

The original graded-outcome table read every cell — including "reset improves" — as framework-consistent. That is rescinded. Registered readings:

| Outcome pattern | Registered interpretation |
|---|---|
| Hidden condition worse (H↓, R↑, M↑, statistically supported) and no reset-alone improvement in the probe | Supports asymmetric state advancement as a distinct failure mode. |
| Differences present but attenuated | Weak support; report as such, no narrative upgrades. |
| **Equivalence within the margin between hidden and externalized conditions on R and H** | **Falsification condition met: externalization produces no measurable improvement, and phase lag is not a meaningful MCW variable. This counts against the framework and is reported as such.** |
| **Externalized condition worse (H lower or R higher under externalization)** | **Counts against the hypothesis.** A rescue reading ("the summaries add overhead but the mechanism still holds") is disallowed as a primary interpretation; it may appear only as a labeled post-hoc conjecture requiring its own pre-registered follow-up. |
| **Reset-alone improvement in the probe (H improves post-reset with nothing externalized)** | **Supports the saturation (ACW-local) explanation and counts against the asymmetric-advancement interpretation.** The original "mixed model" reading is rescinded and disallowed as a primary interpretation. If the main contrast supports the hypothesis *and* the probe shows reset-alone improvement, both results are reported at equal prominence; the probe result is not absorbed into a mixed-model narrative. |

**Decision rule across sessions:** if ≥ 50% of participants individually show no worse end-of-task H and no higher median R in their hidden condition than in their externalized condition (or the aggregate TOST declares equivalence), the falsification condition is triggered — regardless of how vivid the frustration in individual transcripts looks.

## Ethics: consent and debrief

This design involves no confederate and no deception about the counterpart; the hidden condition asks the participant to withhold information from an AI system, which may produce mild, transient frustration. Requirements, registered as part of the design:

1. **Consent** covers recording of the sessions and worksheets.
2. **Debrief** after the session explains both conditions, the probe, and the purpose; the participant may withdraw their data on the spot, without justification, and withdrawal is honored in all analyses.
3. Where an institutional review process is available, it applies before any session runs.

## Stopping rule and deviations

Collection stops at 12 participants (24 main-task sessions plus 12 probe runs). Deviations are logged and demote the study's claimable evidence layer per the [shared standards](index.md#shared-standards).

## What running this buys

Run as registered with dual rating: **L2**, and with IRR targets met, **L3** — and the first M scores anywhere in the framework, since this is the first Human ↔ AI template. The probe means even a "positive" main result can be undercut by its own control arm, and the design accepts that. As with [Experiment 1](exp1_false_alignment.md), a clean null or a saturation-favoring probe result is a publishable, framework-relevant outcome and is welcomed in exactly the sense the Constitution promises.