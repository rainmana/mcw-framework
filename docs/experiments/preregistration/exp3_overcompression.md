# Pre-Registration — Experiment 3: Overcompression Damage

**Status:** Pre-registration template · Evidence: L0 (design) · Type: Human ↔ AI · Source: [Toy Experiment 3](../toy_experiments.md#experiment-3-overcompression-damage) · Shared standards: [pre-registration index](index.md)

---

## Registered hypothesis

> In Human ↔ AI sessions on tasks built to require specific edge-case distinctions, early comprehensive summarization — summary accepted, original detail never revisited — loses more of those distinctions from the final work product than delayed summarization, and the losses surface late (higher D), cost more to repair (higher R), leave final MCW health lower (lower H), and attract more capability blame (higher M).

Direction is registered: fewer surviving planted distinctions, D↑, R↑, H↓, M↑ in the early-summarization condition relative to the delayed-summarization condition. M **is scored** (Human ↔ AI; see the [rubrics scope restriction](../hrdm_rubrics.md#m-misattribution-03-per-window-human-ai-only)). The source hypothesis's "IU loss" (Information Unit — see the [glossary](../../glossary.md)) is operationalized as the loss of planted distinctions, defined below; no other sense of IU loss is claimed or measured here.

## Design

- **Conditions (within-subject, order counterbalanced):**
    1. **Early-summarization condition** — after the task brief is delivered and before the first pre-declared decision point, the participant follows a scripted step: request a comprehensive summary of the task so far, then continue in a fresh AI context seeded with that summary only. The brief document is withdrawn at the same moment. The original detail is never revisited.
    2. **Delayed-summarization condition** — identical task flow, including a summary request, but the summary is requested only after all pre-declared decision points are passed; the brief remains available throughout. *This is the comparison the original falsification condition referenced ("no worse outcomes than delayed summarization") but the original design never specified.*
- **Operationalization note.** The early condition bundles compression with context replacement — proceeding from the summary alone is enforced by seeding a fresh context with it. This bundle *is* the failure mode as the source design describes it ("proceed as if it is complete"), and it mirrors the common practice of continuing work in a new session from a summary; effects of context replacement per se versus summary content cannot be separated at this design's resolution and are not claimed separately.
- **Task battery.** Two matched task packs (A and B), each a multi-step task completable in 20–30 minutes, each embedding exactly **3 planted edge-case distinctions**: pieces of the brief that at least one pre-declared decision point depends on, and whose loss is objectively detectable in the final work product. A frozen answer key specifies, for each distinction, the observable feature of the final work product that is present if and only if the distinction survived. Task packs, decision points, planted distinctions, and answer keys are frozen before the first session; packs are matched on length, step count, and judged distinction difficulty before any data exists.
- **Participants.** 12 participants, each completing both conditions (one per task pack) with the same AI assistant configuration. Participants must not know the study concerns summarization or compression (cover story: "multi-step task workflows with AI assistants").
- **Counterbalancing.** Four sequences (condition order × pack-to-condition pairing), 3 participants per sequence, randomly assigned.
- **Minimal N.** 12 participants (24 sessions) — a feasibility-based pilot size, powered only for large effects, and stated as such.

## Measures

- **Primary outcome:** count of planted distinctions surviving to the final work product (0–3 per session), scored against the frozen answer key by two independent raters from condition-stripped work products (embedded summaries and any condition-revealing metadata removed).
- H, D, and M per 5-exchange window; R per repair episode; R\_ev per 10 exchanges — all per the [anchored rubrics](../hrdm_rubrics.md), scored from transcripts by two independent raters.
- **Blinding override (declared).** Condition-blind transcript rating is not achievable in this design: the manipulation is the visible placement of the summary request. Raters remain blinded to the hypothesis and never see the expected-signature tables (per the [shared standards](index.md#shared-standards)), but proxy-based claims from this study are capped at L2 regardless of inter-rater reliability. The primary outcome is scored fully blinded.
- **Secondary outcomes:** for each lost distinction, whether the loss surfaces before session end and its discovery lag in exchanges (the late-discovery model the rubrics use for D), and the R of the repair episode at the point of discovery. Distinctions lost and never discovered are the pattern the hypothesis's "hard to debug" clause predicts.

## Analysis plan

- Early vs. delayed on the primary outcome: Wilcoxon signed-rank (within-participant), one-sided (fewer distinctions survive under early summarization), α = 0.05. H one-sided (lower under early); R, D, M one-sided (higher under early).
- Equivalence (for the falsification decision): TOST on the primary outcome with a pre-registered margin of **1 planted distinction** — an override of the shared ±0.5 margin, justified because the primary outcome is a count of discrete distinctions, not a 0–3 rubric proxy. TOST on H, R, D, and M with the shared ±0.5-point margin.

## Pre-committed outcome interpretation (the losable bets)

The original graded-outcome table gave every cell a framework-friendly reading. Outcome C — "Summary works fine — task doesn't require nuance / overcompression risk is task-dependent" — functioned as an escape hatch and is rescinded: the registered task packs are designed to require the planted distinctions, so "task-dependent" may not be invoked to save the hypothesis for tasks that were designed to be nuance-dependent. Registered readings:

| Outcome pattern | Registered interpretation |
|---|---|
| Fewer distinctions survive early summarization, with D↑ and R↑ (statistically supported) | Supports overcompression as a distinct MCW injury. |
| Distinctions are lost under early summarization but surface fast and cheaply (D≈, low R) | Partial support only: the loss claim holds, the late-emergence claim does not; both are reported as such. The original outcome-B reading ("healthy immune signaling") is disallowed as a primary interpretation; it may appear only as a labeled post-hoc conjecture requiring its own pre-registered follow-up. |
| Differences present but attenuated | Weak support; report as such, no narrative upgrades. |
| **Equivalence within margins between the early- and delayed-summarization conditions** | **Falsification condition met: overcompression is not a meaningful failure mode even on tasks built to punish it. This counts against the framework and is reported as such.** |
| **Inverted effect (more distinctions survive under early summarization, or H↑)** | **Counts against the hypothesis.** No framework-friendly reading is registered for this cell. |

**Decision rule across sessions:** if the aggregate TOST declares equivalence on the primary outcome, or ≥ 50% of participants individually lose no more distinctions in their early-summarization session than in their delayed-summarization session, the falsification condition is triggered — regardless of how suggestive individual transcripts are.

## Ethics: incomplete disclosure, consent, debrief

This design involves no confederate and no engineered social pressure; the only concealment is the study's focus (the cover story), needed so participants do not guard their summaries. Requirements, registered as part of the design:

1. **Consent** covers recording of the sessions and states that the study's specific focus will be explained afterward.
2. **Debrief** immediately after the second session: the compression focus, the planted distinctions, and the purpose are disclosed; the participant may withdraw their data on the spot, without justification, and withdrawal is honored in all analyses.
3. Where an institutional review process is available, it applies before any session runs.

## Stopping rule and deviations

Collection stops at 12 participants (24 sessions). Deviations are logged and demote the study's claimable evidence layer per the [shared standards](index.md#shared-standards).

## What running this buys

Run as registered with blinded answer-key scoring of the work products: **L2**, and with the reliability protocol met, **L3 on the primary outcome** — proxy-based claims stay capped at L2 per the blinding override above, whichever way the result comes out. A clean equivalence result here triggers the falsification condition and is a publishable, framework-relevant result, welcomed in exactly the sense the Constitution promises.