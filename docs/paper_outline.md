# MCW Framework — Draft Paper Outline

**Working title:**
*The Meta-Context Window: A Coordination Framework for Human–AI Collaboration Failures*

**Intended venue:** CHI, CSCW, or arXiv preprint (cs.HC / cs.AI)

**Paper type:** Framework / Conceptual Contribution

**Target length:** 6–10 pages (short paper) or extended abstract (4 pages)

**Status:** Outline only. Evidence notes indicate what currently exists vs. what is still needed.

---

## Epistemic Posture

This paper is a **framework contribution**, not an empirical validation. The recognized genre at CHI/CSCW introduces:
- a new vocabulary for a previously unnamed phenomenon
- a falsifiable taxonomy of failure modes
- a designed experimental protocol

This posture allows rigorous claims without overclaiming results that do not yet exist. The abstract and introduction must make this framing explicit.

---

## Abstract (Draft)

Failures in human–AI collaboration are routinely attributed to model capability — hallucination, misunderstanding, misalignment. We propose that a significant and underexplored class of these failures is better explained as **coordination failures**: breakdowns in the shared context that emerges between a human and an AI during interaction.

We introduce the **Meta-Context Window (MCW)** — a formal construct describing the dynamically maintained coordination state that arises when a human cognitive system (HCW) and an artificial cognitive system (ACW) exchange Information Units (IUs) through a constrained channel. MCW is neither stored in the AI nor in the human; it exists only through active, bidirectional exchange.

We present: (1) a formal definition of MCW and its component constructs; (2) a taxonomy of six failure modes with observable early-warning signals; (3) a set of repair operations derived from information-theoretic principles; and (4) five lightweight, falsifiable toy experiments designed to probe coordination dynamics without requiring instrumented systems or benchmarks.

The MCW framework does not compete with alignment, safety, or prompt engineering approaches. It offers a complementary lens: a way to diagnose coordination failures that occur even when models are capable, prompts are well-formed, and intentions are good.

---

## 1. Introduction

**Key claim:** Many human–AI collaboration failures are coordination failures, not capability failures.

**Argument structure:**
1. Increasing model capability and context window size have not uniformly improved collaboration quality
2. Current tooling (RAG, prompt engineering, fine-tuning) optimizes the AI's context window in isolation
3. The human has a context window too — and it is not modeled
4. Together, human and AI form a coupled system whose emergent coordination state has no name, no repair protocol, and no diagnostic framework
5. MCW names that state and provides the beginnings of a systematic treatment

**Evidence available now:**
- Practitioner observation: expert AI users manage context instinctively, producing better outcomes — but this folk knowledge is tacit and non-transferable
- "Lost in the middle" and maximum effective context window research shows that ACW size ≠ ACW effectiveness
- Human–human communication research (repair theory, common ground) provides precedent for this class of failure

**Evidence still needed:**
- Controlled studies demonstrating MCW degradation independently of model capability
- Quantitative proxy metrics (repair cost, drift rate) correlated with outcome quality

---

## 2. Background and Related Work

**Key claim:** MCW is not captured by existing frameworks; it occupies a gap between HCI, CSCW, information theory, and AI alignment.

### 2.1 Human–Computer Interaction (HCI)
HCI focuses on usability, affordances, and task completion. MCW addresses coordination dynamics that persist even when interfaces are well-designed.

### 2.2 Computer-Supported Cooperative Work (CSCW)
CSCW studies shared artifacts and breakdowns in collaboration. MCW is actor-agnostic and minimal by design — applicable to human–human, human–AI, and AI–AI systems without presupposing social structure.

### 2.3 Common Ground Theory (Clark & Brennan, 1991)
Common ground describes the mutual knowledge, beliefs, and assumptions shared by communication partners. MCW extends this to non-human actors and formalizes it through IU exchange and information-theoretic degradation.

**Key distinction:** Common ground is a property of shared beliefs; MCW is a property of shared *coordination state* — which includes salience, timing, and repair capacity, not just propositional content.

### 2.4 Information Theory
Shannon entropy provides the mathematical grounding for MCW degradation. MCW does not attempt to formalize cognition in Shannon-theoretic terms, but borrows the intuition of information loss under constrained transmission.

### 2.5 Alignment, Safety, and Prompt Engineering
These approaches optimize *within* the ACW. MCW addresses the *between* — the coupling layer that is currently unmodeled.

**Evidence available now:**
- `docs/related_work.md` in this repository

**Evidence still needed:**
- Formal literature review (currently narrative)
- Explicit comparison to common ground theory, distributed cognition (Hutchins), and situated action (Suchman)

---

## 3. The MCW Framework

**Key claim:** MCW is a formally definable, measurable construct — not a metaphor.

### 3.1 The Three Context Windows

Define HCW, ACW, and MCW. Establish that:
- HCW is continuous, non-enumerable, advances between turns
- ACW is discrete, bounded, updates only on input
- MCW emerges from their coupling — it is not stored anywhere

### 3.2 Information Units (IUs)

Define IU as the minimal transferable element that can influence coordination state. Establish substrate-independence and representation-dependence.

Map IUs to existing AI concepts:

| AI Concept | IU Interpretation |
|------------|------------------|
| Tokens / embeddings | IU representations |
| RAG | IU retrieval and reinjection |
| Prompt engineering | IU bundling |
| Context drift | IU entropy accumulation |
| Expert performance | Better IU stewardship |

### 3.3 MCW as a Coupling Function

Present the formal definition:

> **MCW = f(HCW₁…HCWₙ, ACW₁…ACWₘ, T, C)**

Explain why MCW is not a sum or product. Introduce the five-stage IU flow model (selection → encoding → transmission → decoding → integration).

### 3.4 System Prompts as Initialization Artifacts

Establish that a system prompt is a static IU bundle — not an MCW participant. It biases early coordination but cannot maintain, monitor, or repair MCW.

**Evidence available now:**
- Full framework formalization in `README.md` and `docs/glossary.md`

**Evidence still needed:**
- Diagrams illustrating HCW/ACW/MCW relationships and IU flow
- Formal notation review by an information theorist

---

## 4. Failure Taxonomy

**Key claim:** MCW degrades through six identifiable, substrate-independent failure modes with observable early-warning signals.

| Failure Mode | Definition | Early Signal | Falsification |
|---|---|---|---|
| Drift | Silent context divergence | "That's not what I meant" arrives late | Interaction with explicit sync checkpoints shows equivalent drift |
| Asymmetric State Advancement | One actor advances off-turn without externalizing | Frustration at repetition; reset makes it worse | Off-turn reflection externalized immediately eliminates lag |
| False Alignment | Apparent agreement masks divergent interpretation | Confidence rises while accuracy drops | Verification checks expose misalignment before it compounds |
| Overcompression | Premature summarization destroys distinctions | Summary feels "off" but is unobjectionable | Delayed summarization preserves edge cases |
| Constraint Opacity | Hidden variables block repair | Repair attempts target wrong cause | Constraint disclosure reduces misattribution |
| Repair Suppression | Clarification signals are penalized or discouraged | Questions stop; errors recur | Explicit repair permission increases alignment over time |

**Evidence available now:**
- Failure taxonomy in `README.md`
- Toy experiment designs in `experiments/toy_experiments.md`

**Evidence still needed:**
- Observed instances from real interaction logs (with consent)
- Inter-rater reliability for failure mode classification

---

## 5. Repair Theory

**Key claim:** Repair is a first-class coordination primitive, not a social nicety — and can be formalized as a set of IU operations.

Present the five canonical repair operations:
- Re-grounding
- Decompression
- Re-weighting
- Disambiguation
- Synchronization

Establish that repair cost grows nonlinearly with MCW degradation — early repair is exponentially cheaper than late repair. This mirrors known patterns in biological immune response and information error correction.

**Evidence available now:**
- Repair operations in `README.md` and `docs/glossary.md`
- Qualitative observation from extended practitioner use

**Evidence still needed:**
- Empirical repair cost curves
- Comparison of repair cost pre- vs. post-MCW-aware interaction protocols

---

## 6. Toy Experiments

**Key claim:** MCW dynamics can be probed with lightweight, falsifiable experiments that require no instrumented systems or benchmarks.

### Design Philosophy
- Coordination over capability: hold task difficulty constant; vary coordination conditions
- Qualitative-first: early signals are experiential and behavioral
- Comparative: results are meaningful relative to a baseline
- Repair-aware: treat repair latency and cost as first-class outcomes

### Measurement Proxies (0–3 ordinal scales)
- **H** (MCW Health): perceived shared understanding
- **R** (Repair Cost): effort to realign
- **D** (Drift Rate): speed of divergence
- **M** (Misattribution): tendency to blame agent capability

### Experiment Summary

| # | Name | Type | Failure Mode | Hypothesis |
|---|------|------|--------------|-----------|
| 1 | False Alignment Injection | Human ↔ Human | False Alignment | Ambiguous agreement language increases H↓, R↑, D↑ |
| 2 | Asymmetric State Advancement | Human ↔ AI | Asymmetric Advancement | Off-turn reasoning without externalization causes phase lag (R↑, M↑) |
| 3 | Overcompression Damage | Human ↔ AI | Overcompression | Premature summarization produces late, hard-to-debug failure |
| 4 | Constraint Opacity Stress Test | Human ↔ AI | Constraint Opacity | Opaque constraints increase H↓, M↑ vs. disclosed constraints |
| 5 | Repair Signal Suppression | Human ↔ Human | Repair Suppression | Suppressed clarification accelerates drift; late correction is costly |

Full specifications, graded outcome interpretations, and cross-experiment analysis in `experiments/toy_experiments.md`.

**Evidence available now:**
- Complete experiment designs with hypotheses and graded outcomes

**Evidence still needed:**
- Pilot runs and recorded observations
- Inter-rater reliability for proxy scores

---

## 7. Limitations

**This section is critical for credibility with reviewers.**

1. **No quantitative validation yet.** Toy experiments are qualitative and observational. Claims are hypothesis-level, not evidence-level.
2. **Non-deterministic systems.** Both human cognition and LLM behavior involve emergent properties that resist controlled isolation. Independent variable control is genuinely difficult.
3. **Measurement proxies are ordinal.** H, R, D, M are coordination observables, not interval-scale metrics. Cross-study comparison is limited until instruments are validated.
4. **Coordination vs. capability confound.** Separating MCW failures from genuine model capability failures requires experimental designs not yet implemented.
5. **Single-interaction focus.** The framework currently addresses dyadic human–AI interaction. Multi-agent and organizational MCWs are theoretical extensions, not tested claims.
6. **Researcher positionality.** The framework was developed through practitioner experience. Formal replication by independent researchers is needed.

---

## 8. Future Work

- Pilot studies using the toy experiment protocols with diverse participants
- Quantitative proxy instrument development and validation
- Hugging Face Space test bed for systematic A/B comparison (MCW-aware vs. baseline prompts)
- Extension to multi-agent and organizational MCW dynamics
- Integration with existing common ground and distributed cognition theory
- Application to non-AI domains (human–human, organizational, policy)

---

## 9. Conclusion

**Key claim:** MCW provides a minimal, falsifiable framework for studying coordination failures in human–AI collaboration — a class of failure that current tooling and research systematically misattributes to capability.

Restate:
- The naming of MCW is itself the first repair operation: unnamed variables cannot be systematically reduced
- The framework is designed to fail quietly if not useful — experiments should produce null results if MCW is not a real factor
- The goal is not to replace existing approaches but to add a missing layer of analysis

---

## Artifact Checklist (pre-submission)

| Artifact | Status |
|---|---|
| README with full framework | ✅ Complete |
| Canonical glossary | ✅ Complete |
| Toy experiments with graded hypotheses | ✅ Complete |
| Related work positioning | ✅ Complete |
| Test bed documentation | ✅ Complete |
| CITATION.cff with ORCID | ✅ Complete |
| Paper outline | ✅ This document |
| Framework diagrams (HCW/ACW/MCW, IU flow) | ⬜ Needed |
| Pilot study observations | ⬜ Needed |
| System prompt derivation doc | ⬜ Planned |
| MCW Constitution | ⬜ Proposed |
| Hugging Face Space | ⬜ Planned |
| Formal literature review | ⬜ Needed |

---

*This outline is a living document. Section order and emphasis should be revisited after pilot studies and peer feedback.*
