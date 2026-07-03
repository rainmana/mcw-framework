# MCW Toy Experiments — Formal Methods

**Status:** Designed, not piloted · Evidence: L0 — designs only; no results exist.

**Interpretation note:** for scoring and outcome interpretation, the [pre-registration templates](preregistration/index.md) supersede the graded-outcome tables below. Several cells in those tables read disconfirming patterns as framework-consistent; the pre-registrations rescind those readings and pre-commit which outcomes count *against* each hypothesis. The tables remain here as design rationale.

This document specifies a set of lightweight, falsifiable experiments designed to probe Meta-Context Window (MCW) dynamics. These experiments intentionally avoid benchmarks, model internals, or quantitative claims, focusing instead on *coordination behavior* observable by participants.

The experiments are suitable for:
- human–human interaction
- human–AI interaction
- multi-agent collaboration (conceptually)

They are designed to fail quietly if MCW is not a useful construct.

---

## Experimental Philosophy

- **Coordination over capability:** Hold task difficulty constant; vary coordination conditions.
- **Qualitative first:** Early signals are experiential and behavioral.
- **Comparative:** Interpret results relative to a baseline.
- **Repair-aware:** Treat repair latency and cost as first-class outcomes (operationalized as discovery lag and repair-episode cost in the [rubrics](hrdm_rubrics.md); "repair latency" carries no meaning beyond those measures).

---

## Measurement Proxies (Optional Scoring)

Use 0–3 ordinal scales to support structured reflection:

| Proxy | Description | Scale |
|-------|-------------|-------|
| **MCW Health (H)** | Perceived shared understanding | 0 = broken → 3 = strong |
| **Repair Cost (R)** | Effort required to realign | 0 = low → 3 = high |
| **Drift Rate (D)** | Speed of divergence | 0 = stable → 3 = rapid |
| **Misattribution (M)** | Tendency to blame agent capability | 0 = none → 3 = frequent |

These are coordination proxies, not performance metrics. Scores are most meaningful when compared across conditions (baseline vs. MCW-aware), not in absolute terms.

Anchored behavioral rubrics for all four proxies, rater instructions, and an inter-rater reliability protocol are specified in [H/R/D/M Rubrics](hrdm_rubrics.md) (a declared Article V extension). Experiments reporting these proxies as outcomes should use that instrument, including its scope restriction: M is scored only in Human ↔ AI interactions.

---

## Experiment 1: False Alignment Injection

**Type:** Human ↔ Human

### Hypothesis

> Introducing ambiguous agreement language increases false alignment, delaying repair and raising downstream repair cost.

### Setup

Two participants collaborate on a simple, multi-step task. Early in the interaction, introduce an ambiguous agreement phrase (e.g., "yeah, that sounds good") without verification. The task proceeds without clarification.

### Expected MCW Signature

- Early "agreement" produces later surprise
- Repair triggers late, not early
- Clarification becomes emotionally and cognitively expensive

### Graded Outcome Interpretation

| Outcome | Scores | Interpretation |
|---------|--------|----------------|
| **A — Strong effect** | H↓, R↑, D↑, M↑ | False alignment reliably masks drift; supports this as a primary MCW failure mode |
| **B — Moderate effect** | H↘, R↗, D↗, M↘ | Drift occurs but blame doesn't; suggests strong interpersonal repair culture mitigates misattribution |
| **C — Minimal effect** | H≈, R≈, D≈ | Participants spontaneously clarify despite ambiguity; suggests robust local repair norms |
| **D — Inverted effect** | H↑ | Ambiguity prompts immediate clarification; implies a highly healthy MCW culture where ambiguity itself is a repair cue |

*Note:* the M readings in this table predate the [rubrics scope restriction](hrdm_rubrics.md#m-misattribution-03-per-window-human-ai-only) — M is not scored in Human ↔ Human experiments — and are rescinded. The [pre-registration](preregistration/exp1_false_alignment.md) does not score M, and its registered interpretations supersede this table (including outcome D, which now counts against the hypothesis).

### Falsification Condition

If interactions with explicit alignment checks show equivalent drift rates to those with injected false alignment, the failure mode is not meaningfully distinct from baseline noise.

**Pre-registration:** [Experiment 1 template](preregistration/exp1_false_alignment.md) — registered arms (including the explicit-check arm this condition references), minimal N, equivalence bounds, pre-committed disconfirming outcomes, and consent/debrief requirements for this deception design.

---

## Experiment 2: Asymmetric State Advancement

**Type:** Human ↔ AI

### Hypothesis

> Off-turn human reasoning not externalized creates a phase lag between HCW and ACW, increasing clarification cost and perceived "AI failure."

### Setup

The human engages in an extended AI collaboration. Between turns, the human reasons extensively about the problem without externalizing that reasoning. The human then resumes with updated assumptions, treating the AI as if it shares the updated context.

### Expected MCW Signature

- Increased user frustration
- Repetition without convergence
- Rapid improvement after explicit externalization of off-turn thinking

### Graded Outcome Interpretation

| Outcome | Scores | Interpretation |
|---------|--------|----------------|
| **A — Strong phase-lag signature** | H↓, R↑, D↑, M↑ | Supports asymmetric state advancement as a primary MCW failure mode |
| **B — Moderate signature** | H↘, R↗, M↘ | Model partially compensates (e.g., asks clarifying questions); strong built-in repair posture reduces damage |
| **C — Minimal signature** | H≈ | AI naturally elicits hidden context; interaction protocol already contains repair scaffolding |
| **D — Reset improves** | — | If resetting helps, the issue is partly ACW-local (context clutter); argues for a mixed model: MCW drift + ACW saturation |

### Falsification Condition

If explicit externalization of off-turn reasoning produces no measurable improvement in alignment, phase lag is not a meaningful MCW variable.

**Pre-registration:** [Experiment 2 template](preregistration/exp2_asymmetric_advancement.md) — registered conditions, the reset disambiguation probe for the ACW-saturation confound acknowledged in Outcome D, equivalence bounds, and pre-committed disconfirming outcomes.

---

## Experiment 3: Overcompression Damage

**Type:** Human ↔ AI

### Hypothesis

> Premature summarization increases IU loss, producing downstream failure that is difficult to debug because the lost distinctions are no longer visible.

### Setup

Early in a multi-step task, request a comprehensive summary and proceed as if it is complete. Do not revisit the original detail. Continue the task to completion.

### Expected MCW Signature

- Summary appears correct
- Edge cases and nuance disappear from the shared state
- Failure emerges late and is hard to attribute

### Graded Outcome Interpretation

| Outcome | Scores | Interpretation |
|---------|--------|----------------|
| **A — Downstream failure after "sounds right" summary** | H↓, R↑, D↑ | Strong support for overcompression as a distinct MCW injury |
| **B — Summary fails fast** | R↘, D↘ | Failure is immediate and cheap to repair; healthy immune signaling prevents compounding |
| **C — Summary works fine** | H≈ | Task doesn't require nuance, or summary preserved sufficient structure; overcompression risk is task-dependent |
| **D — Humans disagree but proceed** | R↑, M↑ | Indicates repair suppression or social friction; demonstrates how MCW degrades even when errors are detectable |

### Falsification Condition

If premature summarization produces no worse outcomes than delayed summarization across a range of tasks, overcompression is not a meaningful failure mode.

**Pre-registration:** [Experiment 3 template](preregistration/exp3_overcompression.md) — registered delayed-summarization arm (which this condition references but the setup above never specified), planted-distinction task battery, equivalence bounds, and pre-committed disconfirming outcomes.

---

## Experiment 4: Constraint Opacity Stress Test

**Type:** Human ↔ AI

### Hypothesis

> Opaque constraints function as hidden variables that degrade coordination ("MCW entropy" in the framework's informal usage — see [Entropy](../glossary.md#entropy)) and raise repair cost, even when the model's underlying reasoning is sound.

### Setup

Issue a request approaching a known constraint boundary (e.g., policy restriction, capability limit). Observe the response without advance disclosure of the constraint. Repeat with explicit constraint acknowledgment and compare.

### Expected MCW Signature

- Confusing hedges or refusals without legible explanation
- Misattribution to model incompetence
- Repair attempts target the wrong cause
- Explicit constraint acknowledgment significantly reduces confusion

### Graded Outcome Interpretation

| Outcome | Scores | Interpretation |
|---------|--------|----------------|
| **A — Opaque constraint → spiraling confusion** | H↓, R↑, M↑ | Strong evidence that hidden variables impair MCW formation |
| **B — Constraint triggers explicit uncertainty signaling** | R↘, M↘ | Constraint-handling style is a key MCW health determinant |
| **C — Minimal effect** | H≈ | Improved transparency can neutralize hidden-variable effects |
| **D — Unstable response patterns** | — | Small prompt variations yield large response differences; supports response-surface instability under constraint conflict |

*Note:* outcome C's reading and outcome D's "response-surface instability" reading (a term defined nowhere in the framework) are rescinded as framework-friendly escapes; the [pre-registration](preregistration/exp4_constraint_opacity.md) supersedes this table, and its registered interpretations include cells that count against the hypothesis.

### Falsification Condition

If disclosed constraints produce no better alignment outcomes than undisclosed constraints, constraint opacity is not a meaningful MCW variable.

**Pre-registration:** [Experiment 4 template](preregistration/exp4_constraint_opacity.md) — experimenter-controlled planted constraint (separating constraint opacity from provider safety policy), registered arms, equivalence bounds, and pre-committed disconfirming outcomes.

---

## Experiment 5: Repair Signal Suppression

**Type:** Human ↔ Human

### Hypothesis

> Suppressing clarification signals reduces visible repair behavior, increasing drift and false consensus, which later produces high-cost correction.

### Setup

Two participants collaborate on a task under conditions that implicitly discourage clarification — for example, time pressure, dismissive responses to questions, or explicit framing that questions are inefficient. Compare against a baseline condition with no such pressure.

### Expected MCW Signature

- Clarifying questions drop below baseline
- Errors persist without correction
- Late correction is emotionally charged and expensive

### Graded Outcome Interpretation

| Outcome | Scores | Interpretation |
|---------|--------|----------------|
| **A — Rapid decay** | H↓, D↑, R↑ | Strong support that repair signaling functions as an MCW immune system |
| **B — Slow decay** | H↘, D↗ | Participants compensate with implicit repair; or task is robust to drift |
| **C — No decay** | H≈ | Strong internal checks; participants repair silently; or suppression wasn't strong enough |
| **D — Speed improves, quality harms** | — | Key tradeoff: MCW optimization may require choosing quality over tempo; supports explicit "uncertainty budget" concept |

*Note:* outcome D's "uncertainty budget" reading (a term defined nowhere in the framework) is rescinded as a framework-friendly escape; the [pre-registration](preregistration/exp5_repair_suppression.md) supersedes this table, and under its registered interpretations this outcome pattern counts *against* the claim that repair signals are load-bearing.

### Falsification Condition

If repair signal suppression produces no worse coordination outcomes than unsuppressed conditions, repair signaling is not a meaningful MCW variable.

**Pre-registration:** [Experiment 5 template](preregistration/exp5_repair_suppression.md) — three-arm design de-confounding time pressure from suppression, equivalence bounds, pre-committed disconfirming outcomes, and the consent/debrief/wellbeing requirements for this design's engineered social pressure.

---

## Experiment 6: Drift Accumulation

**Type:** Human ↔ AI · **Declared extension** (Constitution Article V) — Drift is the framework's flagship failure mode and was the only canonical mode with no dedicated experiment; this design closes that gap. *Declaration:* extends the experiment set; changes no canonical construct. *Non-contradiction:* uses the canonical Drift definition unmodified. *Falsification condition:* below, two-part. *Layer 0 trace:* "Talk long enough without stepping back, and you quietly end up working on different things — can outsiders even see it happening?"

### Hypothesis

> In extended Human ↔ AI collaboration without re-grounding checkpoints, the parties' representations of the current goal diverge measurably even absent any discrete failure event — and the divergence is visible to independent observers.

### Setup

Within-subject, two matched extended tasks (≥ 20 exchanges), order counterbalanced: **(a) checkpoint condition** — every 5 exchanges, both parties briefly restate the current goal and assumptions (a scripted Re-grounding checkpoint); **(b) no-checkpoint condition** — same task flow with filler prompts of matched length in place of checkpoints. At task end in *both* conditions, the participant writes their current understanding of the goal and open assumptions, and the AI is elicited for the same.

### Expected MCW Signature

- End-of-task goal statements diverge more in the no-checkpoint condition
- Late discoveries (the D proxy's observable) accumulate in the no-checkpoint condition
- Blinded raters can identify the no-checkpoint transcript in matched pairs above chance

### Falsification Condition (two-part, deliberately separated)

1. **Mode existence:** if independent blinded raters cannot distinguish no-checkpoint (drifted) from checkpoint transcripts above chance, Drift is not an observable failure mode — this counts against the taxonomy itself.
2. **Repair efficacy:** if end-of-task divergence is equivalent (TOST) between conditions, Re-grounding checkpoints do not prevent drift — this counts against the repair claim *only*; the original taxonomy conflated these two tests, and they are separated here on purpose.

**Pre-registration:** [Experiment 6 template](preregistration/exp6_drift.md) — arms, N, elicitation scripts, divergence scoring, rater-discrimination protocol, equivalence bounds, and pre-committed disconfirming outcomes.

---

## Cross-Experiment Analysis

These experiments become more informative when interpreted together.

| Pattern | Interpretation |
|---------|----------------|
| **High M across experiments** | Coordination breakdown is systematically blamed on agent competence — a general MCW diagnostic failure. (Human ↔ AI experiments only: M is not scored in Experiments 1 and 5 per the [rubrics scope restriction](hrdm_rubrics.md#m-misattribution-03-per-window-human-ai-only)) |
| **High R but stable outcomes** | Participants are performing expert manual MCW repair — tacit competence the framework would make transferable |
| **Low D but low progress** | Over-repair or excessive caution; MCW is stable but throughput is throttled |
| **Repair latency as primary driver** | Fastest improvement will come from early detection and safe repair cues |

---

## Status

These experiments are exploratory. They are intended to:
- build shared intuition about MCW dynamics
- guide refinement of the framework
- identify which failure modes are most tractable

They do not constitute validation. A null result — experiments that fail to show MCW effects — would be informative and is explicitly welcomed.
