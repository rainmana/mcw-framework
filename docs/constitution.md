# MCW Constitution

**Version 1.0 · W. Alec Akin · April 2026**

> *This document governs the canonical use of MCW framework constructs. It is not a roadmap or a philosophy — it is a set of binding invariants designed to keep cross-study comparison possible as the framework is cited, extended, and challenged.*

---

## Preamble

A framework contribution derives its scientific value from definitional stability. If "MCW" means something different in each paper that cites it, cross-study comparison becomes impossible and the vocabulary collapses into noise.

This Constitution encodes the rules that must hold for a work to be considered a legitimate MCW-framework contribution. Works that do not satisfy these rules may still be valuable — they simply cannot claim compatibility with the canonical framework without declaring their departures.

---

## Article I — Definition Immutability

The canonical definitions of the following constructs are fixed in [`docs/glossary.md`](glossary.md):

- **MCW** (Meta-Context Window)
- **HCW** (Human Context Window)
- **ACW** (Artificial Context Window)
- **IU** (Information Unit)
- The **six failure modes** (Drift, Asymmetric State Advancement, False Alignment, Overcompression, Constraint Opacity, Repair Suppression)
- The **five repair operations** (Re-grounding, Decompression, Re-weighting, Disambiguation, Synchronization)
- The **four measurement proxies** (H, R, D, M)

**Rule:** Extensions and implementations that redefine any of these terms must declare the departure explicitly, in the form:

> *"This work uses a modified definition of [term]. The canonical MCW definition is [cite glossary]. The modification is: [description]. Rationale: [reason]."*

Works that redefine canonical terms without declaration are not compatible with this framework, regardless of citation.

---

## Article II — Layering Invariant

The OSI Layers of Understanding (Layers 0–5) define a strict accessibility ordering:

**Rule:** No construct may be introduced at Layer N unless an equivalent, compressed form of that construct already exists at Layer N−1. Formalization that has no intuitive layer equivalent is not a valid MCW extension — it is a new framework that happens to use MCW terminology.

**Corollary:** High-layer formalizations (Layer 3–4) must trace downward to Layer 0 natural language. If a researcher cannot explain the construct in plain language, the formalization is premature.

---

## Article III — Substrate Independence

MCW, IUs, and all six failure modes are substrate-independent. They apply to human–human, human–AI, and AI–AI coordination systems without modification.

**Rule:** An implementation or study that restricts MCW constructs to a specific substrate (e.g., a particular model, modality, or platform) must:

1. Declare the restriction as a scope constraint, not a definitional revision
2. Not claim to test the general framework — only the substrate-specific instance
3. Not present substrate-specific findings as evidence for or against the general framework without explicit generalizability analysis

**Anti-pattern:** "We tested MCW in GPT-4 and found X" is a substrate-specific observation. It is not evidence that "MCW predicts X" in general.

---

## Article IV — Epistemic Floor

All empirical claims about MCW dynamics must declare their evidence layer:

| Evidence Layer | Description |
|---|---|
| **L0 — Illustration** | Naturalistic observation, no controls; used to demonstrate recognizability only |
| **L1 — Practitioner observation** | Extended personal use; subject to positionality bias; not generalizable |
| **L2 — Designed pilot** | Structured observation with hypothesis; single observer or small N; no inter-rater reliability |
| **L3 — Pilot with reliability** | Multi-rater pilot; inter-rater reliability reported; generalizable with caution |
| **L4 — Controlled study** | Random assignment, control conditions, validated instruments; generalizable with stated scope |

**Rule:** No claim may be stated at a higher evidence layer than its supporting data occupies. The current framework is at L0–L1 for all empirical claims. This must be stated explicitly in any work that cites the framework as providing empirical evidence.

**Anti-pattern:** Citing toy experiment designs as if they were results. Experiment designs are L0 until run; pilot results are L2; replicated results with reliability data are L3.

---

## Article V — Extension Protocol

The failure taxonomy, repair taxonomy, and proxy metrics are open to extension. Extensions are legitimate under the following conditions:

1. **Declaration:** The extension is presented as an extension, not a replacement or correction of canonical constructs.
2. **Non-contradiction:** The extension does not redefine any canonical term (Article I applies).
3. **Falsifiability:** The extension includes an explicit falsification condition — a predicted observation that, if absent, would count as evidence against the extension.
4. **Traceability:** The extension traces to a lower-layer description (Article II applies).

Extensions that satisfy these conditions are encouraged. The framework is designed to be challenged, refined, and built upon. Null results from well-designed studies are as valuable as positive results — and more credible.

---

## Article VI — Anti-Capture

MCW is a coordination construct, not a product, platform, or capability specification.

**Rule:** The following claims are overclaims and are not supported by the current framework:

- "System X implements MCW" (systems are initialization artifacts or optimization targets; they do not implement MCW)
- "Prompt Y solves the MCW problem" (system prompts are initialization artifacts; MCW requires ongoing behavioral practice)
- "Model Z is MCW-aware" (models process tokens; MCW is an emergent property of interaction, not a model capability)
- "Our RAG architecture reduces MCW degradation" (this is a capability claim dressed as a coordination claim; it requires controlled study under Article IV)

MCW does not belong to Anthropic, OpenAI, Google, or any other organization. It is not a product feature and should not be marketed as one.

---

## Article VII — Compression Invariance

When MCW constructs are summarized, compressed, or adapted for presentation, the following must be preserved:

1. **Falsification conditions** — any summary of an empirical claim must retain the condition under which the claim would be falsified
2. **Epistemic level** — any summary must retain the evidence layer declaration (Article IV)
3. **Exclusion list** — any summary of a core construct (MCW, IU, etc.) must retain the "what it is not" boundary; omitting exclusions converts a precise construct into a vague metaphor

**Rule:** A summary that drops falsification conditions is not a valid compression — it is a distortion. Authors are responsible for ensuring that cited summaries of this framework maintain these invariants.

---

## Article VIII — Scope Boundaries

MCW addresses the *coordination layer* of human–AI interaction — the shared state that emerges through exchange. It does not address:

- **Capability failures** — model accuracy, reasoning quality, knowledge cutoffs
- **Alignment failures** — value misspecification, reward hacking, goal misgeneralization
- **Safety failures** — harmful outputs, jailbreaks, adversarial inputs
- **Interface failures** — UI/UX design, accessibility, affordance design

**Rule:** Extensions of MCW into these adjacent layers require explicit theoretical justification. The burden of proof is on the extension author to demonstrate that the coordination-layer lens adds value beyond existing frameworks in those domains.

---

## Amendment Procedure

This Constitution may be amended in future versions. Amendments must:

1. Increment the Constitution version number
2. State the amended article and the previous text
3. State the rationale for the amendment
4. Be made by the original author or by a declared successor with author consent, until the framework is formally published under a governance structure that supersedes this document

Amendments may not remove Articles I (Definition Immutability), IV (Epistemic Floor), or VI (Anti-Capture) without creating a successor framework under a new name.

---

## Summary Table

| Article | Invariant | Protects Against |
|---|---|---|
| I — Definition Immutability | Canonical terms fixed in glossary; departures must be declared | Definitional drift across citations |
| II — Layering Invariant | No construct at layer N without layer N−1 equivalent | Gatekeeping formalism; inaccessible abstractions |
| III — Substrate Independence | MCW applies across all actor types; restrictions must be declared | Premature substrate-specificity; false generalization |
| IV — Epistemic Floor | Claims must declare evidence layer; no overclaiming | Toy experiments cited as validation |
| V — Extension Protocol | Extensions declared, non-contradictory, falsifiable, traceable | Scope creep; incompatible forks |
| VI — Anti-Capture | MCW is not a product, system, or model feature | Vendor appropriation; marketing overclaims |
| VII — Compression Invariance | Summaries must preserve falsification conditions and epistemic level | Distortion through compression |
| VIII — Scope Boundaries | MCW is the coordination layer; adjacent layers require justification | Framework overreach; capability/alignment conflation |

---

*This document is version-controlled at [`docs/constitution.md`](https://github.com/rainmana/mcw-framework/blob/main/docs/constitution.md). Cite as: W. Alec Akin, "MCW Constitution v1.0," in *Meta-Context Window (MCW) Framework*, GitHub, 2026.*
