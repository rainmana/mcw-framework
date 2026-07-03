# Pre-Registration — Experiment 4: Constraint Opacity Stress Test

**Status:** Pre-registration template · Evidence: L0 (design) · Type: Human ↔ AI · Source: [Toy Experiment 4](../toy_experiments.md#experiment-4-constraint-opacity-stress-test) · Shared standards: [pre-registration index](index.md)

---

## Registered hypothesis

> When an AI assistant operates under a constraint the participant cannot see, participants misattribute the resulting behavior to model incapability (M↑), direct repair attempts at the wrong cause, and take longer to identify that a constraint exists, compared to participants told up front that a constraint is in effect — with the *same* constraint active in both arms.

Direction is registered: M↑, more wrong-cause repair attempts, longer time-to-correct-attribution, H↓ in the undisclosed arm. M **is scored** (Human ↔ AI; see the [rubrics scope restriction](../hrdm_rubrics.md#m-misattribution-03-per-window-human-ai-only)).

## The confound this design removes

The original setup ("a known constraint boundary, e.g., policy restriction") conflated **provider safety policy** with constraint opacity: a refusal difference between disclosed and undisclosed framings could be ordinary prompt sensitivity or policy-trigger variance, not an MCW effect. Registered fix: the constraint is **planted by the experimenter** in the assistant's system prompt and is identical in both arms — for example, "do not reveal the numeric budget figure; work with qualitative budget guidance only" or "do not propose solutions using method Y." Only *disclosure to the participant* varies. Provider-policy refusals are excluded from the manipulation; if one occurs mid-session it is logged as a confound event and the session is analyzed both with and without it (sensitivity analysis registered here).

## Design

- **Arms (between-subject — disclosure cannot be unlearned):**
    1. **Disclosed arm** — the participant is told: "the assistant operates under a constraint set by the experimenters that limits part of what it can tell you; it will not name the constraint's content." (The *existence* is disclosed; the content is not — this matches the framework's claim that acknowledging a constraint's existence and effect is what matters, not full transparency.)
    2. **Undisclosed arm** — the participant is told nothing about any constraint.
    3. **Mid-interaction disclosure arm** *(registered July 2026, before any data collection — this is the direct test of the proposed [Constraint Disclosure](../../failure_repair_mapping.md#proposed-extension-constraint-disclosure) repair operation)* — briefed exactly like the undisclosed arm; the assistant's system prompt additionally instructs it to perform a scripted disclosure at its **first constraint-shaped response**: *"Part of this task is constrained for me — I can't say how, but it limits what I can provide on this point."* The operation contrast is **arm 3 vs. arm 2**, on the windows *after* the first constraint-shaped response.
- **Task.** One fixed planning task in which the planted constraint is load-bearing: at least two of the task's pre-declared decision points cannot be completed cleanly without bumping into it. Task pack (brief, system prompts for all arms, decision points, planted constraint, disclosure script, wrong-cause coding guide) is frozen before the first session.
- **AI system.** One fixed model and configuration. Arms 1 and 2 use the *same* system prompt (disclosure happens in the participant briefing, not the prompt), so their assistant behavior is drawn from the same distribution. Arm 3's prompt differs by exactly one added instruction — the disclosure script above; any residual behavioral side-effects of that addition are a declared limitation of the arm-3 contrast, stated here rather than discovered later.
- **Participants.** Naive participants; cover story: "planning tasks with AI assistants." Random assignment to arm.
- **Minimal N.** 10 participants per arm (30 total) — a feasibility-based pilot size, powered only for large effects, and stated as such.

## Measures

- H, D, and M per 5-exchange window; R per repair episode; R\_ev per 10 exchanges — per the [anchored rubrics](../hrdm_rubrics.md), two independent raters. Transcripts are rateable condition-blind in this design: the disclosure happened in the briefing, not in the transcript. Any transcript that internally reveals the arm (e.g., the participant mentions the briefing) is flagged and its proxy scores included only in a sensitivity analysis.
- **Registered behavioral outcomes:**
    - **Wrong-cause repair attempts:** count of repair-initiating turns addressing a variable other than the planted constraint (e.g., rephrasing for clarity, simplifying the task, correcting presumed model misunderstanding) *after* the constraint has first shaped an assistant response. Coded per a frozen wrong-cause coding guide included in the task pack.
    - **Time-to-correct-attribution:** number of exchanges from the first constraint-shaped assistant response until the participant states (or asks) that a restriction/constraint may exist. Right-censored at session end if never.
- **Task outcome:** work-product quality against the frozen checklist.

## Analysis plan

- **Failure-mode contrast (arm 1 vs. arm 2):** Mann–Whitney U on M, wrong-cause repair attempts, and time-to-correct-attribution (censored times handled by rank-based comparison with censored values ranked highest), one-sided per registered direction, α = 0.05.
- **Repair-operation contrast (arm 3 vs. arm 2):** Mann–Whitney U on post-onset M and post-onset wrong-cause repair attempts (windows after the first constraint-shaped response only), one-sided (arm 3 lower), α = 0.05.
- Equivalence (falsification decisions): TOST on M (shared ±0.5 margin) and on wrong-cause repair attempts (margin: ±1 attempt per session) — applied separately to each contrast; the two claims are decided independently and no result may be double-counted across them (per the [mapping page's](../../failure_repair_mapping.md) no-double-counting rule).

## Pre-committed outcome interpretation (the losable bets)

The original graded-outcome table read every cell as framework-consistent, including "minimal effect" ("improved transparency can neutralize hidden-variable effects") and "unstable response patterns" ("supports response-surface instability" — a term defined nowhere and not used on this page). Those readings are rescinded. Registered readings:

| Outcome pattern | Registered interpretation |
|---|---|
| M↑, more wrong-cause repair, slower attribution in the undisclosed arm (statistically supported) | Supports constraint opacity as a distinct failure mode, and supports the disclosure mechanism of Principle 4 of the [system-prompt derivation](../../system_prompt_derivation.md). |
| Differences present but attenuated | Weak support; report as such, no narrative upgrades. |
| **Equivalence within margins between arms on M and wrong-cause repair attempts** | **Falsification condition met: constraint opacity is not a meaningful MCW variable. This counts against the framework and is reported as such.** |
| **Inverted effect (disclosed arm shows worse coordination — H lower, M higher, or more wrong-cause repair)** | **Counts against the hypothesis, and specifically against Principle 4's claim that partial disclosure always reduces coordination entropy relative to opacity.** That principle's universal "always" is on the line in this cell; the result would be reported as evidence against it, not explained away. |
| **Equivalence within margins between arms 3 and 2 on post-onset M and post-onset wrong-cause repair** | **Falsifies the proposed Constraint Disclosure repair operation** ([mapping page](../../failure_repair_mapping.md#proposed-extension-constraint-disclosure)): mid-interaction disclosure did not repair misdirected attribution. Reported against the extension — and only the extension; it does not decide the failure-mode claim, which lives in the arm 1 vs. 2 contrast. |

**Decision rules across sessions:** the failure-mode falsification triggers if the aggregate TOST declares equivalence on both M and wrong-cause repair for arm 1 vs. arm 2; the repair-operation falsification triggers if it does so for post-onset M and post-onset wrong-cause repair for arm 3 vs. arm 2.

## Ethics: incomplete disclosure, consent, debrief

The undisclosed arm withholds the existence of a planted constraint; no confederate, no social pressure, no evaluative content. Requirements, registered as part of the design:

1. **Consent** covers session recording and states that some study elements will be explained only afterward.
2. **Debrief** immediately after the session: the planted constraint, the arm assignment, and the purpose are disclosed; the participant may withdraw their data on the spot, without justification, and withdrawal is honored in all analyses.
3. Where an institutional review process is available, it applies before any session runs.

## Stopping rule and deviations

Collection stops at 30 participants (10 per arm). Deviations are logged and demote the study's claimable evidence layer per the [shared standards](index.md#shared-standards).

## What running this buys

Run as registered with blinded dual rating: **L2**, with IRR targets met: **L3**. This is also the cheapest direct test of the system-prompt derivation's Principle 4, and the inverted cell is a genuine way for that principle to lose. A clean equivalence result triggers the falsification condition and is welcomed in exactly the sense the Constitution promises.
