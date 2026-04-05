# MCW Toy Experiments — Formal Methods

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
- **Repair-aware:** Treat repair latency and cost as first-class outcomes.

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

### Falsification Condition

If interactions with explicit alignment checks show equivalent drift rates to those with injected false alignment, the failure mode is not meaningfully distinct from baseline noise.

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

---

## Experiment 4: Constraint Opacity Stress Test

**Type:** Human ↔ AI

### Hypothesis

> Opaque constraints function as hidden variables that increase MCW entropy and raise repair cost, even when the model's underlying reasoning is sound.

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

### Falsification Condition

If disclosed constraints produce no better alignment outcomes than undisclosed constraints, constraint opacity is not a meaningful MCW variable.

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

### Falsification Condition

If repair signal suppression produces no worse coordination outcomes than unsuppressed conditions, repair signaling is not a meaningful MCW variable.

---

## Cross-Experiment Analysis

These experiments become more informative when interpreted together.

| Pattern | Interpretation |
|---------|----------------|
| **High M across experiments** | Coordination breakdown is systematically blamed on agent competence — a general MCW diagnostic failure |
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
