# Meta-Context Window (MCW) Framework

**W. Alec Akin** · Early-stage framework · v0.2 · April 2026

> *Many failures in human–AI collaboration are coordination failures, not capability failures.*

This repository presents the **Meta-Context Window (MCW)** — a formal construct describing the shared coordination state that emerges when a human cognitive system and an artificial cognitive system exchange information during interaction. MCW provides vocabulary, a failure taxonomy, and a set of falsifiable experiments for studying a class of breakdown that current tooling and research systematically misattributes to model capability.

**Framework status:** Exploratory. Definitions and failure taxonomy are formalized. Toy experiments are designed but not yet piloted. No quantitative validation exists. Claims are hypothesis-level.

---

## Quick Navigation

| Document | Description |
|----------|-------------|
| [Glossary](docs/glossary.md) | Canonical definitions for all framework terms |
| [Paper Outline](docs/paper_outline.md) | Draft outline for a methods-oriented short paper |
| [System Prompt Derivation](docs/system_prompt_derivation.md) | First-principles derivation of MCW-aware prompt design from IU theory |
| [Toy Experiments](docs/experiments/toy_experiments.md) | 5 falsifiable experiments with graded outcome interpretation |
| [Related Work](docs/related_work.md) | Positioning relative to HCI, CSCW, information theory, and alignment research |
| [Test Bed](docs/test_bed.md) | Public Custom GPT instrument and planned Hugging Face Space |
| [CITATION.cff](CITATION.cff) | Citable reference with ORCID |

---

## Problem Statement

Increasing AI model capability and context window size have not uniformly improved human–AI collaboration quality. Tooling advances — retrieval-augmented generation, prompt engineering, fine-tuning — primarily optimize the AI's internal context. They treat coordination failures as capability problems and prescribe capability solutions.

This framework proposes that a significant class of failures cannot be addressed through ACW-only optimization because the failure is not *in* either actor — it is *between* them. The shared coordination state that emerges through interaction has no formal name, no repair protocol, and no diagnostic framework in current practice. MCW names that state and provides the beginnings of a systematic treatment.

---

## Core Constructs

### Human Context Window (HCW)

The bounded set of information a human actively holds during an interaction: working memory, attention, intent, unspoken assumptions, and emotional salience. The HCW is non-enumerable and advances continuously — including between conversational turns, without externalization.

### Artificial Context Window (ACW)

The bounded computational context an AI system maintains during an interaction: active tokens, embeddings, retrieved information, and attention patterns. The ACW is enumerable and formally bounded. It updates only when new input is provided.

### Meta-Context Window (MCW)

> **The MCW is the dynamically maintained shared state of meaning, salience, intent, and continuity that emerges through ongoing interaction between one or more HCWs and one or more ACWs.**

More formally, MCW is a **coupling function**:

```
MCW = f(HCW₁…HCWₙ, ACW₁…ACWₘ, T, C)
```

Where **T** is time and interaction history, and **C** is communication channel constraints (bandwidth, latency, modality, noise).

MCW is not a sum or product of its components. It captures lossy transfer, salience weighting, interpretation, and drift — dynamics that simple aggregation cannot represent.

**Key properties:**

| Property | Description |
|----------|-------------|
| Emergent | Does not exist in either party alone; arises from interaction |
| Bidirectional | Neither party owns it; both can degrade or repair it |
| Temporal | Exists in time, not in storage; decays without maintenance |
| Lossy | Not all internal state is transmitted; omission and distortion are inherent |
| Repairable | With explicit effort, degraded MCW can be restored |

**What MCW is not** — see [Glossary § MCW](docs/glossary.md#meta-context-window-mcw) for the full exclusion list. In brief: MCW is not the AI's context window, not chat history, not memory, not RAG, not UI/UX, not prompt quality, and not alignment or ethics. It is the *transport and synchronization layer* through which those things operate.

### Information Units (IUs)

> **An Information Unit is the minimal transferable element of information that can influence coordination state between actors.**

IUs are substrate-independent (text, speech, symbols, signals) but representation-dependent (tokens for AI, concepts for humans). They are composable, context-sensitive, and lossy under transfer.

IUs are not tokens, facts, beliefs, or values. They are coordination-relevant informational elements. See [Glossary § IU](docs/glossary.md#information-unit-iu) for full definition and exclusions.

**MCW as IU dynamics:** MCW forms when IUs are exchanged and begin to mutually constrain interpretation. It degrades when IU entropy rises — through omission, overcompression, misweighting, or suppression. It is repaired through explicit IU operations.

---

## Failure Taxonomy

MCW degrades through six identified failure modes. These are substrate-independent — they apply to human–human, human–AI, and AI–AI interaction.

| Failure Mode | Description | Key Danger |
|---|---|---|
| **Drift** | Silent, unacknowledged context divergence | Feels like progress until it suddenly doesn't |
| **Asymmetric State Advancement** | One actor's window advances off-turn without externalization | Resets worsen rather than repair the gap |
| **False Alignment** | Apparent agreement masks divergent interpretation | Suppresses repair signals that would otherwise trigger correction |
| **Overcompression** | Premature summarization destroys IU distinctions | Lost nuance is no longer visible to either party |
| **Constraint Opacity** | Hidden variables block legible coordination | Repair is systematically misdirected |
| **Repair Suppression** | Clarification signals are penalized or discouraged | Functionally equivalent to immune suppression |

Each failure mode has identifiable early-warning signals and graded observable outcomes. Full specifications and experimental designs in [experiments/toy_experiments.md](experiments/toy_experiments.md). Full definitions in [docs/glossary.md](docs/glossary.md).

---

## Repair Theory

MCW repair is treated as a first-class coordination primitive, not a social nicety. Five canonical IU repair operations are defined:

| Operation | Description |
|-----------|-------------|
| **Re-grounding** | Reintroduce foundational IUs; restate goals and assumptions |
| **Decompression** | Expand compressed IU bundles back into component distinctions |
| **Re-weighting** | Adjust IU salience; clarify what matters most |
| **Disambiguation** | Split overloaded IUs; surface divergent interpretations |
| **Synchronization** | Align IU timelines; externalize off-turn state changes |

A key implication of repair theory: repair cost grows nonlinearly with MCW degradation. Early repair is exponentially cheaper than late repair — a pattern that mirrors biological immune response and information-theoretic error correction.

---

## System Prompts as Initialization Artifacts

A system prompt is a preloaded, static IU bundle injected into an ACW prior to MCW formation. It biases early coordination but:

- does not participate in MCW (MCW requires bidirectional, temporally adaptive exchange)
- cannot monitor for drift
- cannot detect or repair misalignment
- introduces hidden variables (constraint opacity) when opaque

> A system prompt is an initialization artifact, not a coordination solution.

MCW-aware interaction requires ongoing behavioral practice, not configuration. Improving a system prompt is *downstream* of understanding MCW — not a substitute for it. A minimal template derived from IU theory is included in the full README appendix below; full derivation is in [docs/paper_outline.md § 3.4](docs/paper_outline.md).

---

## OSI Layers of Understanding

The framework is designed to be accessible at multiple levels of formality. No prior background is required to engage at any layer:

| Layer | Audience | Framing |
|-------|----------|---------|
| 0 — Intuition | Anyone | "Are we on the same page?" |
| 1 — Concepts | Generalists | MCW as shared coordination state; IUs as coordination atoms |
| 2 — Formalization | STEM-adjacent | Entropy, IU flow model, coupling function |
| 3 — Models | Researchers | Entropy flows, phase transitions, drift metrics |
| 4 — Implementation | Builders | Simulations, test beds, experiment protocols |
| 5 — Application | Domain specialists | Case studies across biology, organizations, AI, policy |

**Invariant rule:** No concept appears at a higher layer unless it already exists at a lower layer in compressed form. This prevents semantic drift and gatekeeping.

---

## Experimental Design

Five toy experiments are designed to probe MCW dynamics without requiring instrumented systems or benchmarks:

| # | Experiment | Type | Failure Mode Targeted |
|---|---|---|---|
| 1 | False Alignment Injection | Human ↔ Human | False Alignment |
| 2 | Asymmetric State Advancement | Human ↔ AI | Asymmetric Advancement |
| 3 | Overcompression Damage | Human ↔ AI | Overcompression |
| 4 | Constraint Opacity Stress Test | Human ↔ AI | Constraint Opacity |
| 5 | Repair Signal Suppression | Human ↔ Human | Repair Suppression |

Experiments use four optional coordination proxies on 0–3 ordinal scales: **H** (MCW Health), **R** (Repair Cost), **D** (Drift Rate), **M** (Misattribution). These are not performance metrics — they are coordination observables.

Each experiment includes a stated hypothesis, graded outcome interpretation, and explicit falsification conditions. If MCW is not a useful construct, these experiments should fail quietly.

Full specifications: [docs/experiments/toy_experiments.md](docs/experiments/toy_experiments.md)

---

## Experimental Instruments

### Custom GPT Test Bed (Live)

A public Custom GPT implementing an MCW-aware initialization prompt is available for exploratory one-shot testing and prompt A/B comparison:

**MCW Framework Test Bed** — https://chatgpt.com/g/g-697ec249edc48191b24805ddd3297230-meta-context-window-mcw-framework-test-bed

This instrument is not a canonical MCW implementation. Results are not logged or aggregated. Findings should be treated as exploratory.

### Hugging Face Space (Planned)

A versioned, reproducible test environment is planned. It will support systematic baseline vs. MCW-aware prompt comparison with exportable result snapshots. See [docs/test_bed.md](docs/test_bed.md).

---

## Related Work

MCW is positioned as complementary to — not competitive with — existing research traditions. See [docs/related_work.md](docs/related_work.md) for full discussion of positioning relative to:

- Human–Computer Interaction (HCI)
- Computer-Supported Cooperative Work (CSCW)
- Common Ground Theory (Clark & Brennan, 1991)
- Information Theory (Shannon)
- Cognitive Science and distributed cognition
- AI alignment, safety, and prompt engineering

MCW's primary contribution is a shared vocabulary for reasoning about coordination breakdowns that are otherwise misattributed to intelligence or capability failures.

---

## Limitations

This framework is **early-stage and exploratory**. The following limitations are explicit and not minimized:

1. **No quantitative validation.** Toy experiments are designed but not yet piloted. Claims are hypothesis-level.
2. **Non-deterministic systems.** Both human cognition and LLM behavior involve emergent properties that resist controlled isolation.
3. **Ordinal measurement proxies.** H, R, D, M are coordination observables, not validated interval-scale metrics.
4. **Capability/coordination confound.** Separating MCW failures from genuine model capability failures requires experimental designs not yet implemented.
5. **Dyadic focus.** The framework currently addresses two-actor interaction. Multi-agent extensions are theoretical.
6. **Practitioner origin.** The framework was developed through extended practitioner experience. Independent replication is needed.

---

## Background

The MCW construct arose from a broader inquiry into how information travels across systems — and from the observation that entropy-management failures produce structurally similar patterns across domains as different as biology, organizations, software, and human–AI interaction.

The formal concept of Information Units emerged from this cross-domain view: a substrate-agnostic unit capturing replication cost, mutation rate, transmission channel, persistence, and context-dependence, against which coordination failures across any system could be analyzed on shared axes.

MCW was identified as the missing layer in human–AI collaboration: current tooling obsessively optimizes the ACW while ignoring the HCW and the emergent coupling between them. This layer had no name, no formal description, and no repair protocol. Naming it is the first step toward systematic improvement.

---

## Repository Structure

```
mcw-framework/
├── README.md                        ← This document
├── CITATION.cff                     ← Citable reference with ORCID
├── docs/
│   ├── glossary.md                  ← Canonical term definitions
│   ├── paper_outline.md             ← Draft methods-oriented paper outline
│   ├── related_work.md              ← Positioning vs. adjacent fields
│   └── test_bed.md                  ← Experimental instrument documentation
└── experiments/
    └── toy_experiments.md           ← 5 experiments with graded hypotheses
```

---

## Appendix: Minimal MCW-Aware System Prompt Template

The following template is derived from IU theory and is provided as a practical starting point. It is not an MCW solution — it is an initialization aid that reduces early entropy and makes repair explicit.

```
This interaction is a collaborative problem-solving process.

Primary goal:
- [state the immediate objective in one sentence]

Coordination norms:
- Surface uncertainty early.
- Ask for clarification when assumptions are unclear.
- If misalignment is detected, pause progress and repair first.

Constraints:
- If any part of a request is constrained or unclear, say so explicitly
  and explain the effect on the response.
- Distinguish reasoning limitations from policy or capability constraints.

Compression:
- Do not over-summarize unless requested.
- When summarizing, preserve assumptions and edge cases.

Repair:
- If the interaction drifts, name the drift.
- Re-ground goals and assumptions before continuing.

This prompt is an initialization aid, not a complete specification.
The interaction may adapt as shared understanding evolves.
```

---

## Citation

> W. Alec Akin. *Meta-Context Window (MCW) Framework*. GitHub repository, 2026. https://github.com/rainmana/mcw-framework

A machine-readable citation entry with ORCID is available in [`CITATION.cff`](CITATION.cff).

---

## Contributing

This repository is intended to be forked, challenged, extended, and used experimentally. Critique, alternative implementations, and replication attempts are welcomed. If MCW is not a useful construct, experiments designed under this framework should demonstrate that clearly — and that outcome is valuable.
