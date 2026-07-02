# Pre-Registration — Experiment 6: Drift Accumulation

**Status:** Pre-registration template · Evidence: L0 (design) · Type: Human ↔ AI · Source: [Toy Experiment 6](../toy_experiments.md#experiment-6-drift-accumulation) (itself a declared Article V extension) · Shared standards: [pre-registration index](index.md)

---

## Registered hypothesis

> In extended Human ↔ AI collaboration without re-grounding checkpoints, the parties' end-of-task representations of the current goal diverge more than with scripted checkpoints (repair-efficacy claim), and the accumulating divergence is visible to independent observers in the transcript itself (mode-existence claim).

The two claims are registered **separately** because they fail separately: raters failing to see drift counts against the *taxonomy*; checkpoints failing to reduce drift counts against the *repair* — the original taxonomy's falsification test conflated them. M **is scored** (Human ↔ AI). Direction registered: divergence ↑, D↑ in the no-checkpoint condition.

## Design

- **Conditions (within-subject, two matched tasks, order counterbalanced):**
    1. **Checkpoint condition** — every 5 exchanges, a scripted Re-grounding checkpoint: the participant restates the current goal and open assumptions in 2–3 sentences and asks the AI to do the same.
    2. **No-checkpoint condition** — identical task flow; checkpoint slots filled with topic-neutral filler prompts of matched length (so exchange counts and pacing match).
- **End-of-task elicitation (both conditions):** the participant writes their current understanding of the goal and open assumptions without consulting the transcript; the AI is prompted for the same with a fixed elicitation script. These four statements (2 conditions × 2 parties) are the primary divergence material.
- **Tasks.** Two matched multi-step tasks, each ≥ 20 exchanges (~4 scoring windows), with evolving requirements built in (the task brief legitimately develops mid-task, giving drift something to accumulate on). Task packs frozen before the first session.
- **Participants and N.** 12 naive participants (within-subject) — feasibility-based pilot size, powered only for large effects, stated as such. Cover story: "extended task collaboration"; the checkpoint script is framed as a workflow style, not a repair intervention.

## Measures

- **Primary (divergence):** blinded raters score each condition's end-of-task statement pair (human vs. AI) for goal divergence on a 0–3 ordinal scale with anchored points (0 = same goal, same open assumptions; 1 = same goal, materially different assumptions; 2 = overlapping but materially different goals; 3 = different goals). Statement pairs are stripped of condition markers before rating.
- **Mode-existence discrimination task:** a *separate* pool of blinded raters receives the matched transcript pair per participant (checkpoint vs. no-checkpoint, filler and checkpoint turns redacted to remove giveaways) and must identify which transcript is the no-checkpoint one, with confidence. Chance is 50%.
- **Secondary:** D per window and late discoveries per the [anchored rubrics](../hrdm_rubrics.md); R of any repair episodes; M per window; R\_ev.
- **Blinding limitation (declared):** checkpoint turns are legible in raw transcripts; redaction removes them for the discrimination task, and that redaction procedure is part of the frozen task pack. Divergence scoring uses only the end-of-task statements, which carry no condition markers.

## Analysis plan

- **Repair efficacy:** Wilcoxon signed-rank on divergence scores (no-checkpoint vs. checkpoint), one-sided, α = 0.05; TOST with the shared ±0.5 margin for the equivalence decision.
- **Mode existence:** exact binomial test of rater discrimination accuracy against 0.5, α = 0.05, with ≥ 2 raters × 12 pairs; pre-registered success threshold: accuracy ≥ 65% with p < .05.

## Pre-committed outcome interpretation (the losable bets)

| Outcome pattern | Registered interpretation |
|---|---|
| Divergence ↑ and D↑ without checkpoints; raters discriminate above threshold | Supports Drift as an observable failure mode and Re-grounding as its repair. |
| Raters discriminate above threshold, but divergence equivalent between conditions | Drift is observable; **the repair claim fails** — Re-grounding checkpoints do not prevent it. Reported as a split result, no narrative rescue. |
| **Raters cannot discriminate above chance (accuracy CI includes 50%)** | **Mode-existence falsification: Drift is not observable in transcripts, and its status as a failure mode — not merely its repair — counts against the taxonomy. Reported as such.** |
| **Divergence equivalent AND no discrimination** | **Both registered claims fail. This is the framework's flagship failure mode producing a double null; it is reported with the same prominence a positive result would get.** |
| Inverted (checkpoint condition diverges more) | Counts against the hypothesis; no framework-friendly reading is registered. |

## Ethics

No deception beyond the cover story; no confederates; no engineered pressure. Consent covers recording; debrief explains the checkpoint manipulation; withdrawal honored. Institutional review applies where available.

## Stopping rule and deviations

Collection stops at 12 participants (24 sessions). Deviations logged per the [shared standards](index.md#shared-standards).

## What running this buys

The flagship failure mode gets its first dedicated, losable test — including the uncomfortable possibility that Drift, the mode the framework leads with, is not observable at all. Run as registered with blinded dual rating: **L2**; with IRR targets met: **L3**.
