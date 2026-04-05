# MCW-Aware System Prompt Derivation

This document derives MCW-aware system prompt design from first principles of Information Unit (IU) theory. It is not a style guide or a collection of best practices. Each design principle is derived from a necessary property of the MCW framework — if the property holds, the principle follows.

**Audience:** Researchers and practitioners who have read the framework and want to understand *why* MCW-aware prompts are structured the way they are before using or modifying the template.

**Status:** Theoretical derivation. Predictions are falsifiable but not yet tested.

---

## Premise: What a System Prompt Actually Is

Before deriving any design principles, we must establish the formal status of a system prompt within MCW theory.

A system prompt is:

> **A preloaded, static IU bundle injected into an ACW prior to MCW formation.**

This definition has four properties that constrain everything that follows.

### Property 1: Static

A system prompt does not change during the interaction. It is evaluated once, at initialization. It cannot observe drift, detect misalignment, or respond to changing salience.

**Consequence:** A system prompt cannot maintain or repair MCW. Any design principle that assumes ongoing monitoring by the prompt is invalid.

### Property 2: Unilateral

A system prompt is authored by one party (the deployer) and injected into one context window (the ACW). The human has no corresponding initialization artifact. The exchange is not bidirectional.

**Consequence:** A system prompt cannot reduce asymmetry in IU selection on the human side. It can only shape *what the AI selects and weights*, not *what the human externalizes*.

### Property 3: Pre-MCW

A system prompt is injected before any interaction occurs — before MCW exists. It shapes the initial conditions under which MCW may or may not form. It does not participate in MCW.

**Consequence:** A system prompt's effectiveness is bounded by initialization quality. It cannot compensate for failures that occur after the first turn.

### Property 4: Potentially Opaque

A system prompt typically contains IUs that are not visible to the human party. These function as hidden variables in the MCW coupling function — exogenous constraints that influence ACW behavior without being legible to the HCW.

**Consequence:** Opaque system prompts introduce constraint opacity by construction. Every hidden IU in a system prompt is a potential source of MCW entropy.

---

## Derivation: Five Design Principles

Each principle below is derived from one or more of the four properties above. The derivation is deductive: if the properties hold, the principle is necessary, not merely advisable.

---

### Principle 1: Legibility Over Authority

**Derived from:** Property 4 (opacity) and Property 1 (static)

**Derivation:**

A system prompt cannot repair misalignment caused by its own opaque IUs (Property 1: it is static). And every hidden constraint it contains is a source of MCW entropy (Property 4). Therefore, the design goal is not to *enforce* behavior but to make the reasoning behind behavior *visible* — converting hidden variables into legible IUs.

An authoritative instruction ("you must always do X") increases constraint opacity when the human cannot see the reason. A legible instruction ("if X becomes relevant, surface it explicitly because Y") converts the same constraint into an IU the human can reason with.

**Design rule:** Prefer explainability over compliance framing. State *why*, not only *what*.

**What this does not claim:** That authority-framing never works. It may work for narrow, well-defined tasks. The claim is only that it increases constraint opacity and therefore MCW entropy in open-ended collaborative contexts.

---

### Principle 2: Explicit Repair Permission

**Derived from:** Property 3 (pre-MCW) and Property 1 (static)

**Derivation:**

Repair cost is lowest at initialization (Property 3: the prompt is injected before MCW forms). Once MCW has formed and begun to drift, repair cost grows nonlinearly. A system prompt is the only tool available at the moment of lowest repair cost.

However, repair cannot occur at all if repair signals are suppressed (Repair Suppression failure mode). The prompt must therefore explicitly authorize the repair behaviors — clarification, uncertainty expression, drift-naming — that MCW theory identifies as immune functions.

Since the prompt cannot repair MCW during the interaction (Property 1), its role is to lower the *cost* and *social risk* of repair signals that humans and AI will emit during the interaction.

**Design rule:** Include IUs that explicitly authorize: uncertainty surfacing, clarification requests, disagreement, and drift acknowledgment. This is not a politeness convention — it is entropy management.

**What this does not claim:** That repair permission eliminates repair need. MCW will still degrade; the prompt makes repair cheaper, not unnecessary.

---

### Principle 3: Salience Declaration

**Derived from:** Property 2 (unilateral) and Property 1 (static)

**Derivation:**

Salience mismatch is a primary source of drift: when the human and AI weight the same IUs differently, their shared state diverges silently. A system prompt cannot observe or correct this mismatch dynamically (Property 1). And it cannot reach into the HCW to align salience from the human side (Property 2).

The only intervention available is to *declare* salience explicitly at initialization — to inject IUs that establish a shared priority ordering before divergence begins. This reduces the initial entropy of the salience dimension of the coupling function.

**Design rule:** State what matters most *for this specific interaction*, what can be deferred, and what can be ignored. Do not attempt to capture all possible salience states — that produces overcompression. A narrow, honest declaration is more effective than a comprehensive one.

**What this does not claim:** That declared salience persists indefinitely. Salience drifts as interactions evolve. The declaration reduces *initial* entropy; it does not prevent later drift.

---

### Principle 4: Constraint Acknowledgment

**Derived from:** Property 4 (opacity) and Property 2 (unilateral)

**Derivation:**

Hidden constraints in a system prompt are hidden variables in the MCW coupling function. The human cannot observe them, and the AI may not be able to explain them. When the AI's behavior is shaped by opaque IUs, the human's repair attempts will be misdirected — they will target the wrong variable.

The only way to reduce this entropy source from within the prompt is to convert hidden constraints into *acknowledged* constraints: IUs that are visible to the human, even if the underlying reason is not fully shareable.

This does not require full transparency (which may be impossible for policy-governed constraints). It requires only that the *existence and effect* of the constraint be legible.

**Design rule:** Name known constraints without moral framing. Distinguish between reasoning limitations, capability limitations, and policy constraints. The act of naming a constraint converts a hidden variable into a visible IU — reducing entropy even when the constraint itself cannot be removed.

**What this does not claim:** That all constraints can be disclosed. Some constraints are genuinely non-disclosable. The claim is that partial disclosure always reduces MCW entropy compared to full opacity, for the constraints that *can* be acknowledged.

---

### Principle 5: Non-Finality Signal

**Derived from:** Property 3 (pre-MCW) and the temporal nature of MCW

**Derivation:**

MCW is temporal: it forms, evolves, and degrades through interaction over time. A system prompt exists at a single point in time — before MCW has formed. It therefore cannot represent a complete or current picture of the MCW that will emerge.

If the prompt signals finality (implicitly or explicitly treating itself as a complete specification), it creates a false alignment risk: the human may treat the prompt's constraints as exhaustive, and the AI may fail to surface information that contradicts the prompt's framing.

The prompt must therefore signal its own incompleteness — explicitly acknowledging that it is an initialization artifact, not a complete specification, and that the interaction may legitimately adapt beyond its initial framing.

**Design rule:** Include a statement that the prompt is an initialization aid, not a complete specification, and that the interaction is expected to evolve.

**What this does not claim:** That prompts should be vague or uncommitted. Precision is valuable; finality is not. A prompt can be precise about initial conditions while remaining open to evolution.

---

## The Derived Template

These five principles, taken together, produce the following minimal template. Each element is labeled with the principle it instantiates:

```
This interaction is a collaborative problem-solving process.

Primary goal:                                        ← Principle 3 (Salience)
- [state the immediate objective in one sentence]

Coordination norms:                                  ← Principle 2 (Repair Permission)
- Surface uncertainty early.
- Ask for clarification when assumptions are unclear.
- If misalignment is detected, pause progress and repair first.

Constraints:                                         ← Principles 1 & 4 (Legibility + Acknowledgment)
- If any part of a request is constrained or unclear, say so
  explicitly and explain the effect on the response.
- Distinguish reasoning limitations from policy or capability
  constraints.

Compression:                                         ← Principle 3 (Salience, negative)
- Do not over-summarize unless requested.
- When summarizing, preserve assumptions and edge cases.

Repair:                                              ← Principle 2 (Repair Permission)
- If the interaction drifts, name the drift.
- Re-ground goals and assumptions before continuing.

This prompt is an initialization aid, not a complete             ← Principle 5 (Non-Finality)
specification. The interaction may adapt as shared
understanding evolves.
```

No element of this template is arbitrary. Each follows from one or more of the four system-prompt properties established in the premise.

---

## Falsifiable Predictions

If the derivation is correct, MCW-aware prompts initialized with this template should produce the following observable differences compared to a baseline prompt (e.g., a simple role-definition):

| Prediction | Measurable proxy | Falsification condition |
|------------|-----------------|------------------------|
| Reduced early repair events | R score in first 5 turns | No difference in R between MCW-aware and baseline prompts in turns 1–5 |
| Reduced misattribution | M score across interaction | No difference in M scores; failures still attributed to model capability at same rate |
| No reduction in capability failures | Factual accuracy on knowledge tasks | MCW-aware prompt produces lower accuracy — would indicate the prompt introduces noise |
| Improved H score after turn 3 | H proxy rating | No difference in H after turn 3 vs. baseline |
| Re-grounding events still required | Count of explicit re-grounding turns | MCW-aware prompt eliminates all re-grounding — would falsify the claim that prompts cannot maintain MCW |

The last prediction is critical: **MCW-aware prompts should not eliminate re-grounding**. If they did, that would contradict the theoretical claim that prompts are initialization artifacts, not dynamic MCW managers. A prompt that appears to eliminate all repair need is more likely masking repair suppression than genuinely maintaining MCW health.

---

## What This Document Does Not Claim

1. **Not that this template is optimal.** It is the minimal derivable template from the five principles. Other valid templates may exist.

2. **Not that prompts can fully manage MCW.** The derivation explicitly establishes that prompts cannot maintain or repair MCW. Claiming otherwise contradicts the framework.

3. **Not that these predictions have been validated.** The predictions are falsifiable; they have not been tested. See `docs/experiments/toy_experiments.md` for the experimental designs that would begin to test them.

4. **Not that all system prompts benefit from this structure.** Narrow, task-specific, single-turn interactions may not require MCW-aware initialization. The framework's predictions apply most strongly to open-ended, multi-turn, collaborative interactions.

5. **Not that prompt design is the primary intervention.** Per the interaction patterns section of the framework, behavioral practice and active MCW stewardship during interaction outweigh initialization quality. Prompt design is downstream of understanding MCW — not a substitute for it.

---

## Relationship to Other Framework Documents

| Document | Relationship |
|----------|-------------|
| [Glossary](glossary.md) | Defines all terms used in this derivation |
| [README](../README.md) | Presents the template without derivation; links here for the theoretical basis |
| [Toy Experiments](experiments/toy_experiments.md) | Experiments that would begin to test the falsifiable predictions above |
| [Paper Outline §3.4](paper_outline.md) | Situates this derivation within the paper's argument structure |
