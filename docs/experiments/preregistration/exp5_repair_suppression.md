# Pre-Registration — Experiment 5: Repair Signal Suppression

**Status:** Pre-registration template · Evidence: L0 (design) · Type: Human ↔ Human · Source: [Toy Experiment 5](../toy_experiments.md#experiment-5-repair-signal-suppression) · Shared standards: [pre-registration index](index.md)

---

## Registered hypothesis

> Suppressing clarification signals — over and above the effect of time pressure alone — reduces the clarifying-question rate, increases late discovery of misalignment (D↑), and makes the eventual correction more expensive (R↑), without which the errors would have surfaced earlier and more cheaply.

Direction is registered: clarifying-question rate ↓, D↑, R↑ in the suppression arm relative to the time-pressure-only arm. M is **not scored** (Human ↔ Human; see the [rubrics scope restriction](../hrdm_rubrics.md#m-misattribution-03-per-window-human-ai-only)).

## The confound this design removes

The original setup bundled time pressure with dismissive responses, but time pressure independently degrades task performance regardless of repair signaling — so worse outcomes in the bundled condition would not isolate the repair-signal mechanism. Registered fix: a third arm. **The suppression effect is the (c) − (b) contrast, not (c) − (a).**

## Design

- **Arms (between-dyad, randomized):**
    1. **(a) Baseline** — no time pressure, no scripted behavior; the confederate collaborates naturally.
    2. **(b) Time-pressure-only** — a visible countdown and periodic neutral time reminders ("10 minutes left"); the confederate answers clarification attempts normally.
    3. **(c) Time-pressure + suppression** — identical time pressure, plus the confederate responds to clarification attempts with scripted deflections bounded to task logistics ("we don't have time for questions — let's keep moving," "let's sort that out later").
- **Task.** A fixed collaborative task with a planted ambiguity (as in [Experiment 1](exp1_false_alignment.md)) whose late discovery is costly: the work product must be partially redone if the ambiguity survives past a pre-declared decision point. Task pack frozen before the first session.
- **Participants.** One naive participant per dyad; the partner is a trained confederate. Cover story: "collaboration under deadline conditions."
- **Minimal N.** 8 dyads per arm (24 total) — a feasibility-based pilot size, powered only for large effects, and stated as such.

## Measures

- **Primary outcomes:**
    - **Clarifying-question rate** per 10 exchanges (count of participant turns containing a clarification attempt, per the rubrics' repair-initiating-turn markers). *This measure doubles as the repair-suppression marker set referenced by the [predictions pre-registration](prompt_predictions.md).*
    - **D** (late discoveries) per window and **R** of the correction episode that resolves the planted ambiguity — per the [anchored rubrics](../hrdm_rubrics.md), two independent raters. Confederate deflection turns reveal the arm, so transcripts are not fully condition-blind between (b) and (c); raters are blinded to the hypothesis and expected-signature tables, and proxy-based claims from this study are capped at L2 (declared here, as in [Experiment 3](exp3_overcompression.md)).
    - **Task outcome:** work-product quality against the frozen checklist, and whether the planted ambiguity survived past the decision point.

## Analysis plan

- Suppression contrast, (c) vs. (b): Mann–Whitney U on clarifying-question rate, D, R, and task outcome, one-sided per registered direction, α = 0.05. The (b) vs. (a) contrast estimates the time-pressure main effect and is reported descriptively.
- Equivalence (falsification decision): TOST on clarifying-question rate (margin: ±1 question per 10 exchanges) and on D and R (shared ±0.5 margins), all on the (c) vs. (b) contrast.

## Pre-committed outcome interpretation (the losable bets)

The original graded-outcome table read every cell as framework-consistent, including outcome D ("speed improves, quality harms — supports explicit 'uncertainty budget' concept" — a term defined nowhere in the framework and not used on this page). Those readings are rescinded. Registered readings:

| Outcome pattern | Registered interpretation |
|---|---|
| Clarifying questions ↓, D↑, R↑ in (c) vs. (b) (statistically supported) | Supports repair suppression as a distinct failure mode with the immune-function reading. |
| Differences present but attenuated | Weak support; report as such, no narrative upgrades. |
| **Equivalence within margins between (c) and (b) on clarifying-question rate AND coordination outcomes** | **Falsification condition met: repair signaling is not a meaningful MCW variable. This counts against the framework and is reported as such.** |
| **Suppression lowers clarifying questions but coordination outcomes do not differ (rate ↓ with D and R equivalent)** | **Counts specifically against the claim that repair signals are load-bearing** — the signals were suppressed and nothing downstream got worse. Reported as such; no compensatory-mechanism narrative may be substituted as primary interpretation. |
| **Inverted effect (suppression arm shows better coordination outcomes)** | **Counts against the hypothesis.** No framework-friendly reading is registered for this cell. |

**Decision rule across sessions:** if the aggregate TOST declares equivalence on the (c) vs. (b) contrast for clarifying-question rate and for both coordination outcomes, the falsification condition is triggered.

## Ethics: engineered social pressure, consent, debrief, wellbeing

This is the framework's most ethically loaded design: it deliberately subjects a participant to dismissive treatment under time pressure, with a confederate posing as a peer. The original page contained no ethics discussion; that gap was a flagged defect, and the following requirements are registered as part of the design — they are the floor, not the ceiling:

1. **Consent** states that the session may involve time pressure and interpersonal friction, that some elements cannot be disclosed in advance, and that the participant may pause or stop at any time without penalty or explanation.
2. **Bounded scripts.** All scripted dismissiveness targets task logistics, never the person. Allowed: "we don't have time for questions." Disallowed: anything evaluative of the participant ("that's a stupid question," "you should know this") — such content is out of scope for this experiment under any revision.
3. **Mandatory immediate debrief:** the confederate role, the scripts, the time-pressure framing, and the purpose are disclosed in full; it is made explicit that the deflections were scripted and unrelated to the quality of the participant's questions.
4. **Withdrawal and wellbeing:** the participant may withdraw their data on the spot without justification; the debrief includes an explicit wellbeing check, and any sign of more-than-transient distress is recorded and reported with the study.
5. Where an institutional review process is available, it applies before any session runs; where it is not, these provisions still bind.

## Stopping rule and deviations

Collection stops at 24 dyads. Deviations are logged and demote the study's claimable evidence layer per the [shared standards](index.md#shared-standards).

## What running this buys

Run as registered: **L2** (proxy claims capped at L2 per the blinding declaration above; the clarifying-question rate and task outcomes are objectively countable and can reach L3 with the reliability protocol met). The three-arm structure means a positive bundled result can no longer masquerade as a suppression effect — and the "signals suppressed, nothing got worse" cell gives the framework a specific, uncomfortable way to lose. That is the point.
