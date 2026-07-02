# Pre-Registration — Experiment 1: False Alignment Injection

**Status:** Pre-registration template · Evidence: L0 (design) · Type: Human ↔ Human · Source: [Toy Experiment 1](../toy_experiments.md#experiment-1-false-alignment-injection) · Shared standards: [pre-registration index](index.md)

---

## Registered hypothesis

> In dyads where a confederate injects ambiguous agreement language without verification, misalignment surfaces later (higher D), repair is more expensive (higher R), and final MCW health is lower (lower H), compared to dyads following an explicit alignment-check protocol.

Direction is registered: D↑, R↑, H↓ in the injection arm relative to the explicit-check arm. M is **not scored** (Human ↔ Human; see the [rubrics scope restriction](../hrdm_rubrics.md#m-misattribution-03-per-window-human-ai-only)).

## Design

- **Arms (between-dyad, randomized):**
    1. **Injection arm** — a confederate responds to the first substantive proposal with scripted ambiguous agreement ("yeah, that sounds good") and does not verify understanding unless the participant initiates.
    2. **Explicit-check arm** — the confederate responds to the same point with a scripted verification move ("before we go on — my understanding is X, is that right?"). *This is the comparison arm the original falsification condition referenced but the original design never specified.*
    3. **Natural baseline arm** — no script; the confederate behaves naturally. Used to locate ordinary behavior between the two manipulated arms.
- **Task.** A fixed collaborative planning task with a known ambiguity planted in the brief (two readings of one requirement, both plausible, materially different downstream). The task must be completable in 20–30 minutes and produce a concrete work product whose correctness under each reading is checkable. The exact task pack (brief, planted ambiguity, checklist of downstream consequences per reading) is frozen before the first session.
- **Participants.** One naive participant per dyad; the confederate role is played by a trained experimenter. Participants must not know the study concerns coordination or agreement (cover story: "collaborative planning styles").
- **Minimal N.** 8 dyads per arm (24 total) — a feasibility-based pilot size, powered only for large effects, and stated as such.
- **Randomization.** Dyads randomly assigned to arm; confederate script order balanced across experimenters if more than one confederate is used.

## Measures

- H and D per 5-exchange window; R per repair episode; R\_ev per 10 exchanges — all per the [anchored rubrics](../hrdm_rubrics.md), scored from transcripts by two independent raters blinded to arm (scripted confederate turns are redacted-in-style so they do not reveal the arm).
- **Primary outcomes:** time-to-first-surfacing of the planted ambiguity (in exchanges), R of the repair episode that resolves it, end-of-session H.
- **Task outcome:** work-product correctness under the brief's intended reading (binary, checklist-scored).

## Analysis plan

- Injection vs. explicit-check on primary outcomes: Mann–Whitney U, α = 0.05. Direction as registered; the H comparison is one-sided (H lower under injection), surfacing-time and R one-sided likewise. Natural-baseline arm is descriptive context only.
- Equivalence (for the falsification decision): TOST on D and on surfacing-time with the shared ±0.5-point margin (D) and a ±3-exchange margin (surfacing time).

## Pre-committed outcome interpretation (the losable bets)

The original graded-outcome table read every cell — including the inverted effect — as framework-consistent. That is rescinded. Registered readings:

| Outcome pattern | Registered interpretation |
|---|---|
| D↑, R↑, H↓ in injection arm (statistically supported) | Supports false alignment as a distinct failure mode. |
| Differences present but attenuated | Weak support; report as such, no narrative upgrades. |
| **Equivalence within margins between injection and explicit-check arms** | **Falsification condition met: the failure mode is not meaningfully distinct from baseline noise. This counts against the framework and is reported as such.** |
| **Inverted effect (H↑ or earlier surfacing in the injection arm)** | **Counts against the hypothesis.** The prior reading ("a highly healthy MCW culture where ambiguity itself is a repair cue") is explicitly disallowed as a primary interpretation; it may appear only as a labeled post-hoc conjecture requiring its own pre-registered follow-up. |

**Decision rule across sessions:** if ≥ 50% of injection-arm dyads individually show no later surfacing than their matched explicit-check comparison (or the aggregate TOST declares equivalence), the falsification condition is triggered — regardless of how interesting the transcripts are.

## Ethics: deception, consent, debrief

This design deceives participants twice: the confederate poses as a naive partner, and the injected agreement is scripted. Requirements, registered as part of the design:

1. **Consent** covers collaborative interaction recording and states that some study elements cannot be disclosed in advance but will be fully explained afterward.
2. **Debrief** immediately after the session: the confederate role, the injected script, and the purpose are disclosed; the participant may withdraw their data on the spot, without justification, and withdrawal is honored in all analyses.
3. **No harm channel:** the injected ambiguity concerns the task content only — never the participant's competence or standing. Scripts containing evaluative or dismissive content are out of scope for this experiment (that manipulation belongs to Experiment 5, with its own protections).
4. Where an institutional review process is available, it applies before any session runs.

## Stopping rule and deviations

Collection stops at 24 dyads. Deviations are logged and demote the study's claimable evidence layer per the [shared standards](index.md#shared-standards).

## What running this buys

Run as registered by a single site with blinded dual rating: **L2**, and with IRR targets met, **L3** — the first data at those layers anywhere in the framework, whichever way it comes out. A clean null here is a publishable, framework-relevant result and is welcomed in exactly the sense the Constitution promises.
