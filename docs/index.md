# Meta-Context Window (MCW) Framework

**W. Alec Akin** · v0.2 · April 2026

---

> *Many failures in human–AI collaboration are coordination failures, not capability failures.*

The **Meta-Context Window (MCW)** is a formal construct describing the shared coordination state that emerges when a human cognitive system and an artificial cognitive system exchange information during interaction.

MCW is not stored in either party. It exists only through active, bidirectional exchange — and it can degrade silently, fail completely, or be deliberately repaired.

**Framework status:** Exploratory. Definitions and failure taxonomy are formalized. Toy experiments are designed but not yet piloted. No quantitative validation exists. Claims are hypothesis-level.

---

## Framework Documents

<div class="grid cards" markdown>

-   :material-vector-line:{ .lg .middle } **Diagrams**

    ---

    Five Mermaid diagrams: the three context windows, IU flow model, failure taxonomy, repair flow, and OSI layers of understanding.

    [:octicons-arrow-right-24: View diagrams](diagrams.md)

-   :material-book-alphabet:{ .lg .middle } **Glossary**

    ---

    Canonical bottom-up definitions for all framework terms — from entropy and IUs through failure modes and repair operations.

    [:octicons-arrow-right-24: Read the glossary](glossary.md)

-   :material-file-document-outline:{ .lg .middle } **Paper Outline**

    ---

    Draft methods-oriented outline for a short paper targeting CHI, CSCW, or arXiv, including evidence inventory and artifact checklist.

    [:octicons-arrow-right-24: Read the outline](paper_outline.md)

-   :material-flask-outline:{ .lg .middle } **Toy Experiments**

    ---

    Five falsifiable experiments with graded outcome interpretation, designed to probe coordination dynamics without instrumented systems.

    [:octicons-arrow-right-24: Read the experiments](experiments/toy_experiments.md)

-   :material-account-search:{ .lg .middle } **Related Work**

    ---

    Positioning relative to HCI, CSCW, information theory, cognitive science, and AI alignment research.

    [:octicons-arrow-right-24: Read the positioning](related_work.md)

-   :material-test-tube:{ .lg .middle } **Test Bed**

    ---

    Public Custom GPT instrument and planned Hugging Face Space for exploratory MCW experiments.

    [:octicons-arrow-right-24: Read about instruments](test_bed.md)

-   :material-math-compass:{ .lg .middle } **System Prompt Derivation**

    ---

    First-principles derivation of MCW-aware prompt design from IU theory, with falsifiable predictions and explicit non-claims.

    [:octicons-arrow-right-24: Read the derivation](system_prompt_derivation.md)

-   :material-scale-balance:{ .lg .middle } **Constitution**

    ---

    Eight binding invariants governing canonical term use, epistemic claims, extensions, and anti-capture rules for the MCW framework.

    [:octicons-arrow-right-24: Read the constitution](constitution.md)

</div>

---

## Core Claim

Current AI tooling optimizes the AI's context window (ACW) in isolation. The human has a context window too (HCW) — and together they form a coupled system whose emergent coordination state has no name, no repair protocol, and no diagnostic framework in current practice.

MCW names that state. The framework provides:

- a formal definition of shared coordination state
- a taxonomy of six failure modes with observable early-warning signals
- five canonical repair operations
- a set of falsifiable experiments

---

## Citation

```
W. Alec Akin. Meta-Context Window (MCW) Framework.
GitHub repository, 2026.
https://github.com/rainmana/mcw-framework
```

ORCID and machine-readable citation: [`CITATION.cff`](https://github.com/rainmana/mcw-framework/blob/main/CITATION.cff)
