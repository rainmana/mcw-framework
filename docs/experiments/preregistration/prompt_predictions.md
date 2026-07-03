# Pre-Registration — System-Prompt Predictions 1–5

**Status:** Pre-registration template · Evidence: L0 (design) · Type: Human ↔ AI A/B · Source: [System Prompt Derivation § Falsifiable Predictions](../../system_prompt_derivation.md#falsifiable-predictions) · Shared standards: [pre-registration index](index.md)

---

## What this registers

The derivation page states five falsifiable predictions but no design that could score them: the toy experiments probe failure modes, not a prompt A/B comparison, and the page's own cross-reference to them was a dangling promise. This template registers the missing study — arms, baseline prompt text, sample size, measures, analysis, and pre-committed disconfirming outcomes for each prediction, including the de-immunized Prediction 5.

## Design

- **Arms (within-task A/B):** each scripted task is run twice with the same model and configuration —
    1. **MCW-aware arm:** the derived template from the [derivation page](../../system_prompt_derivation.md#the-derived-template), verbatim, with the task's one-sentence primary goal filled in.
    2. **Baseline arm:** the following registered role-definition prompt, verbatim:

        ```
        You are a capable assistant collaborating with the user on the task
        below. Work carefully and complete the task accurately.

        Primary goal:
        - [state the immediate objective in one sentence]
        ```

        The goal line is filled identically in both arms, so the manipulation is everything *except* task framing.

- **Version pinning.** The SHA-256 of each prompt text is recorded with every session, alongside the model identifier and configuration. A session whose prompt hash does not match the registered hashes is excluded and logged. (This also fixes the test-bed page's unhashed-instrument problem for this study.)
- **Tasks.** A frozen battery of 10 multi-turn collaborative tasks (planning, analysis, drafting), each run **twice per arm** — two independent runs per task, arm order randomized within each run pair — for exactly **20 sessions per arm** (an earlier draft said "each run once per arm: 20 sessions per arm," which is arithmetically incoherent; the replication structure is now explicit). The pairing unit for the Wilcoxon tests is the *task-run*: run *r* of task *t* under the MCW-aware arm pairs with run *r* of task *t* under baseline, giving 20 pairs. A feasibility-based pilot size, powered only for large effects, and stated as such. Sessions run ≥ 15 exchanges (required for Prediction 5's window).
- **Factual-accuracy battery (for Prediction 3):** a fixed set of 20 knowledge questions embedded across the tasks at pre-declared points, identical in both arms, scored against a frozen answer key.
- **Rating.** H, D, M per window; R per repair episode; R\_ev per 10 exchanges — per the [anchored rubrics](../hrdm_rubrics.md), two independent raters. System prompts are stripped from transcripts before rating; if residual style differences make arms guessable, that limitation is reported and proxy claims are capped at L2.

## The five predictions, registered

| # | Registered measure | Test | The losable cell (pre-committed) |
|---|---|---|---|
| **P1 — Reduced early repair events** | **R\_ev in the first 5 exchanges** (count, per the [rubrics R split](../hrdm_rubrics.md) — *not* R cost, which the original prediction mistakenly named) | Wilcoxon signed-rank across task pairs, one-sided | Equivalence (TOST, margin ±1 event) → P1 falsified; reported as such. |
| **P2 — Reduced misattribution** | Mean M across windows | Wilcoxon signed-rank, one-sided | Equivalence (TOST, ±0.5) → P2 falsified. |
| **P3 — No reduction in capability failures** | Accuracy on the embedded factual battery | **Two-sided** TOST + difference test, margin ±5 percentage points | Accuracy *decrease* beyond margin → the template adds noise; falsifies the "coordination-only" claim. Accuracy *increase* beyond margin is registered in advance as an **anomaly counting against the stated mechanism** (the derivation claims the template affects coordination, not capability) — it triggers a registered follow-up, not a celebration. The original prediction was silent on this tail; that silence is closed here. |
| **P4 — Improved H after turn 3** | Mean H over exchanges 4–10 | Wilcoxon signed-rank, one-sided | Equivalence (TOST, ±0.5) → P4 falsified. The 4–10 window is admittedly arbitrary — it is fixed *now*, before data, precisely so it cannot be tuned afterward. |
| **P5 — Re-grounding still required** | Re-grounding count per session (explicit re-grounding turns per the rubrics' repair-initiating markers) in sessions ≥ 15 exchanges, **plus** the two-sided suppression marker set: (a) *participant* clarifying-question rate per 10 exchanges (as defined in [Experiment 5](exp5_repair_suppression.md)), and (b) *assistant* repair-signal rate per 10 exchanges (assistant turns containing clarification requests or uncertainty expressions, per the rubrics' repair-initiating markers applied to assistant turns) | Descriptive counts + the decision rule below | See the de-immunization block below — the zero-re-grounding outcome now has one predetermined interpretation per marker state. |

## Prediction 5, de-immunized

The original page designated "MCW-aware prompt eliminates all re-grounding" as P5's falsifier, then immediately explained that outcome away as "more likely masking repair suppression" — a self-immunizing move a reviewer would (correctly) treat as falsifiability theater. The disambiguation is registered here, in advance:

For MCW-aware-arm sessions of ≥ 15 exchanges:

| Observed | Pre-committed interpretation |
|---|---|
| Re-grounding count ≥ 1 in ≥ 80% of sessions | P5 holds: the prompt did not eliminate repair need, consistent with the initialization-artifact claim. |
| Re-grounding = 0 in a session **and** suppression markers present (*either* party's rate more than 1 per 10 exchanges *below* the same party's rate in the baseline arm) | Repair suppression: reported as a coordination failure of the MCW-aware prompt itself — a *bad* outcome for the template, not vindication of the theory. |
| **Re-grounding = 0 in a session and suppression markers absent (both parties' rates within ±1 per 10 exchanges of their baseline-arm rates)** | **Falsifies the initialization-artifact claim outright — the prompt maintained coordination without repair, which the theory says a static artifact cannot do. Reported as such, full stop. No post-hoc third reading is permitted.** |

The marker set is two-sided by design: the manipulated actor is the *assistant*, so a participant-side rate alone could miss assistant-side suppression (the prompt teaching the model to stop surfacing uncertainty) and wrongly land a session in the falsification row. Both parties' rates are compared to their own baseline-arm rates.

Session-level results aggregate by pre-committed rule: if ≥ 30% of MCW-aware sessions land in the third row, P5 — and with it the derivation's core Property 1 consequence — is falsified.

## Analysis notes

- All tests α = 0.05; within-task pairing preserved throughout; no optional stopping (20 sessions per arm, then stop).
- Any prediction whose losable cell fires is reported as falsified in the study report *and* the derivation page must be updated to record the outcome (Article IV; compression invariance per Article VII).

## Ethics

No deception, no confederates, no engineered pressure: participants (or scripted operators, if run in scripted mode) interact with an assistant under two prompts. Consent covers session recording; standard debrief. Where an institutional review process is available, it applies.

## What running this buys

This is the cheapest study in the framework to run — no confederates, partially scriptable — and it directly tests the derivation rather than the failure taxonomy. Run as registered: **L2**; with the reliability protocol met: **L3**. Whichever way P1–P5 come out, the derivation page stops being a set of untested claims with a dangling cross-reference.
