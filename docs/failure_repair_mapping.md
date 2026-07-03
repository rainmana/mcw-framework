# Failure-Mode ↔ Repair-Operation Mapping

**Status:** Mixed — the mapping table documents existing canon and its gaps (documentation, not amendment); the two proposed repair operations are **declared extensions** (Constitution [Article V](constitution.md#article-v-extension-protocol)); the decision tree is a working classification instrument · Evidence: L0 throughout.

The canon defines six failure modes and five repair operations and has never published the mapping between them. That silence produced a real inconsistency (an undeclared sixth operation appeared in Diagram 4 to cover the gap) and left the 6-vs-5 non-bijection as unexplained debt. This page makes the mapping explicit, resolves the non-bijection by proposing two extension operations with full Article V paperwork, and supplies the discriminant criteria the taxonomy previously lacked.

---

## The exhaustive mapping

| Failure mode | Repair operation | Basis |
|---|---|---|
| [Overcompression](glossary.md#overcompression) | [Decompression](glossary.md#decompression) | **Canon-derived:** the glossary defines Decompression as "reverses overcompression" |
| [False Alignment](glossary.md#false-alignment) | [Disambiguation](glossary.md#disambiguation) | **Canon-derived:** the glossary defines Disambiguation as "addresses false alignment" |
| [Asymmetric State Advancement](glossary.md#asymmetric-state-advancement) | [Synchronization](glossary.md#synchronization) | **Canon-derived:** the glossary defines Synchronization as "close asymmetric state advancement" |
| [Drift](glossary.md#drift-silent-desynchronization) | [Re-grounding](glossary.md#re-grounding) | **Inferred:** no glossary text names the pairing; restating goals, assumptions, and scope is the natural repair for silent divergence. Inference, not canon. |
| [Constraint Opacity](glossary.md#constraint-opacity) | **Constraint Disclosure** *(proposed extension, below)* | **Gap under canon:** no canonical operation performs disclosure |
| [Repair Suppression](glossary.md#repair-suppression) | **Repair-Norm Restoration** *(proposed extension, below)* | **Gap under canon:** no canonical operation operates on the repair channel itself |

**[Re-weighting](glossary.md#re-weighting)** (adjust IU salience) has no designated failure mode: it is a general-purpose operation applicable wherever salience mismatch is the underlying cause — most often inside Drift and Overcompression repairs. **Re-grounding** likewise doubles as the universal fallback and escalation move. The mapping is therefore many-to-many at the edges; the table gives the *primary* pairing per mode.

### Why the existing five do not suffice

The alternative to proposing new operations was documenting that the five cover everything. That case fails on inspection:

- Every canonical operation *operates on IUs already in (or recoverable from) the exchange*: re-introducing them (Re-grounding), expanding them (Decompression), re-ranking them (Re-weighting), splitting them (Disambiguation), or transporting off-turn ones (Synchronization). Constraint Opacity's defining feature is an IU that was **never in the exchange and is not recoverable from it** — a hidden rule. No amount of operating on exchanged IUs discloses it; only the constrained party can.
- Repair Suppression is a failure of the **repair channel itself**. Applying any first-order repair operation through a suppressed channel is precisely what the mode prevents; the channel must be restored before the five operations are usable at all.

An earlier version of Diagram 4 papered over the second gap with an undeclared "Repair permission" box — removed as an Article I/V violation. The two proposals below are the declared, governed version of the same instinct.

---

## Proposed extension: Constraint Disclosure

*Targets: Constraint Opacity.*

- **Declaration.** A sixth repair operation is proposed as an Article V extension of the repair taxonomy: **Constraint Disclosure** — naming the existence and behavioral effect of a constraint that is shaping one party's behavior, even when the constraint's content cannot be fully shared. *Example: "Part of what you're asking is restricted for me — I can't say why, but it means my answers on X will be partial."*
- **Non-contradiction.** Extends, does not modify, the canonical five (which remain exactly five in the glossary; this operation lives here as a declared extension). Consistent with the Constraint Opacity definition, whose "key danger" is that repair is systematically misdirected — disclosure is the act that un-misdirects it.
- **Falsification condition.** Constraint Disclosure predicts that naming a constraint's existence *after opaque behavior has appeared* reduces subsequent wrong-cause repair and misattribution relative to continued opacity. The direct test is a **mid-interaction disclosure arm** extending [Experiment 4](experiments/preregistration/exp4_constraint_opacity.md) — disclosure delivered at the first constraint-shaped response, versus never — which is **not yet registered**; until it (or an equivalent design) is, this operation's falsification condition is stated but untriggerable, matching the discipline applied to Repair-Norm Restoration below. Experiment 4's registered arms vary *pre-briefing* disclosure, before any opaque behavior has appeared: they test the underlying awareness mechanism (knowing an unnamed constraint exists reduces misattribution) and bear on this operation as supporting evidence, but equivalence there would falsify the pre-briefing mechanism, not this repair operation. No result may be double-counted across the two.
- **Layer 0 trace.** "Tell them a rule is shaping what you do — even if you can't tell them the rule."

## Proposed extension: Repair-Norm Restoration

*Targets: Repair Suppression.*

- **Declaration.** A seventh repair operation is proposed as an Article V extension: **Repair-Norm Restoration** — explicitly re-authorizing the signals that trigger repair (clarifying questions, uncertainty expressions, restatement requests) after they have been discouraged, ignored, or penalized. *Example: "I may have shut down questions earlier — please do interrupt me whenever something is unclear; I'd rather fix it now."*
- **Non-contradiction.** Extends the canonical five; consistent with the Repair Suppression definition (the mode is about signals being discouraged; the operation is the explicit reversal of that discouragement). Distinct from Re-grounding: restating goals does not re-license questions.
- **Falsification condition.** Repair-Norm Restoration predicts that explicit re-authorization, delivered after a suppression episode, raises the clarifying-question rate back toward baseline and improves downstream coordination relative to continued suppression. The natural test is a fourth arm extending [Experiment 5](experiments/preregistration/exp5_repair_suppression.md) — suppression followed by scripted re-authorization vs. suppression maintained. That arm is **not yet registered**; until it (or an equivalent design) is, this extension's falsification condition is stated but untriggerable, and the operation must not be presented as validated. No rate recovery and no outcome difference would falsify the operation, and would be reported as such.
- **Layer 0 trace.** "Say out loud that questions are welcome again — and mean it."

**Governance note:** both operations are extensions, not canon. The glossary's canonical count remains five, and the constitution-lint enforces exactly five glossary repair operations; if these extensions earn adoption into canon after being tested, that adoption is an Article I amendment with the full procedure, not a silent promotion.

---

## Discriminant decision tree

The taxonomy previously offered no procedure for telling overlapping modes apart — Constraint Opacity and Repair Suppression in particular produce identical surface signals (dropped clarifications, confusing refusals). The tree below classifies an observed breakdown by *primary* mode at detection time. Apply the questions in order; the first "yes" classifies. Co-occurrence is real (False Alignment famously lets Drift compound), so secondary labels are permitted — but the primary label comes from the tree, not from narrative preference.

1. **Is there a discrete compression artifact** — a summary or restatement after which a previously present distinction is absent from the shared state? → **Overcompression.** (The artifact is the evidence; point to it.)
2. **Is there an explicit agreement or ratification moment** whose parties demonstrably held divergent interpretations at the time? → **False Alignment.** (Requires locating the agreement token *and* the divergence; an unratified misreading repaired on the spot is ordinary grounding, not a mode.)
3. **Did one party's state advance outside the exchange** — off-turn reasoning, tool use, externally acquired information — without being externalized? → **Asymmetric State Advancement.** (In instrumented settings, verifiable against worksheets or logs; in the wild, look for references to never-exchanged content.)
4. **Is a party's *task-content* behavior shaped by a rule or constraint the other party cannot see — producing repair attempts that target the wrong cause?** → **Constraint Opacity.** (The discriminant is what the rule *does*, not whether it is hidden: a hidden rule whose effect is specifically to deflect, penalize, or discourage repair signals is **Repair Suppression** — question 5 — regardless of its hiddenness. Experiment 5's scripted confederate deflections are the registered example: a hidden instruction, but its target is the repair channel, so it classifies as Repair Suppression, not Constraint Opacity. Discriminant vs. Repair Suppression restated: under Constraint Opacity repair attempts still *occur* and misfire; under Repair Suppression they *decline*. Verifiable where the constraint is auditable: system prompts, policies, experimenter-planted rules.)
5. **Are repair signals declining or being penalized** — clarifying-question rate falling against baseline, questions deflected or punished? → **Repair Suppression.** (Discriminant vs. Constraint Opacity: the *channel* is degrading; no hidden rule is required. Measured, not felt: the rate is countable per the [rubrics](experiments/hrdm_rubrics.md).)
6. **Otherwise** — gradual, unacknowledged divergence with none of the above discrete events → **Drift.** Drift is deliberately the *residual* diagnosis: it is defined by the absence of a localizable event, and the tree makes that explicit instead of letting it absorb everything.

Two honesty notes. First, the tree is an instrument at L0 — its inter-coder reliability is untested, and the [rubrics'](experiments/hrdm_rubrics.md) IRR protocol applies to it in the same way if it is ever used for coding claims above L2. Second, questions 3 and 4 depend on evidence (logs, prompt audits) that natural settings often lack; where that evidence is unavailable, the honest output is "3/4-indeterminate," not a guess.

---

## Reconciling Diagram 2's stage risks with the canonical modes

[Diagram 2](diagrams.md#diagram-2-iu-flow-model) annotates the five IU-flow stages with per-stage risks — Omission, Overcompression, Noise/Latency, Misinterpretation, Drift — three of which appear nowhere else in the framework. That second, unreconciled failure vocabulary was flagged as canon debt. The reconciliation:

| Diagram 2 stage risk | Relation to the canonical six |
|---|---|
| **Omission** (Selection) | Not a canonical mode — a *stage-level contributing process*. Chronic omission of off-turn state becomes [Asymmetric State Advancement](glossary.md#asymmetric-state-advancement); deliberate omission of constraints becomes [Constraint Opacity](glossary.md#constraint-opacity). The term is retired as a mode-name and retained only as a stage-risk description. |
| **Overcompression** (Encoding) | The canonical mode itself, manifesting at its home stage. |
| **Noise / Latency** (Transmission) | Not a mode — a *channel property* (the C of the coupling function). It raises the probability of every mode; it is not itself a coordination failure. |
| **Misinterpretation** (Decoding) | Not a mode — a *surface event*. If ratified by apparent agreement it becomes [False Alignment](glossary.md#false-alignment); if surfaced and repaired promptly it is ordinary grounding traffic. Retired as a mode-name. |
| **Drift** (Integration, "weighting mismatch") | The canonical mode — but its Diagram 2 placement (Stage 5) conflicted with Diagram 3's classification (channel/hidden-variable). Resolution: Drift is not stage-specific. It is an *accumulation phenomenon* across all five stages, which is exactly why the decision tree treats it as the residual diagnosis. Diagram 3 now carries it under a cross-stage accumulation branch. |

Diagram 3's remaining stage assignments are heuristics about where each mode primarily *manifests*, not claims about mechanism: Asymmetric State Advancement sits under Selection because the failure is the non-selection of off-turn IUs for externalization; Repair Suppression sits there because the suppressed party stops selecting repair IUs. The diagrams page now says this instead of asserting the assignments bare.
