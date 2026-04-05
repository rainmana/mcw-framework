# MCW Test Bed & Experimental Instruments

This document describes the experimental instruments used to explore and validate the Meta-Context Window (MCW) framework. These instruments are intentionally lightweight, qualitative, and accessible.

They are designed to:
- enable rapid experimentation
- support informal replication
- gather subjective coordination signals
- avoid premature formalization

---

## Design Principles

All MCW test beds follow these principles:

- **Low ceremony**: experiments should be runnable without specialized infrastructure.
- **Qualitative first**: early validation focuses on coordination quality, not benchmarks.
- **Comparative**: results are meaningful only relative to a baseline.
- **Non-authoritative**: instruments explore behavior; they do not define correctness.

---

## Custom GPT Test Bed (Public)

A public Custom GPT has been created as an initial MCW test instrument:

**Meta-Context Window (MCW) Framework Test Bed**
https://chatgpt.com/g/g-697ec249edc48191b24805ddd3297230-meta-context-window-mcw-framework-test-bed

### Purpose

This Custom GPT implements an MCW-aware system prompt and exposes model selection to the user. It is intended for:
- one-shot comparisons
- prompt A/B testing
- informal qualitative evaluation
- early intuition-building

### Notes and Limitations

- This test bed is **not** a canonical implementation of MCW.
- Results are **not** logged or aggregated.
- The environment is constrained by the hosting platform.
- Findings should be treated as exploratory.

Despite these limitations, early results suggest that MCW-aware initialization can improve perceived clarity and reduce repair latency even in single-turn interactions.

---

## Hugging Face Spaces (Planned)

For more formal and reproducible experimentation, a Hugging Face Space is planned.

A Space will allow:
- versioned experiment configurations
- consistent baselines
- optional result export
- broader community replication

### Planned Minimal Features

- UI toggle: baseline prompt vs MCW-aware prompt
- Task input field
- Model selection (where available)
- Optional self-report checklist (e.g., uncertainty surfaced, assumptions stated)
- Exportable result snapshot (JSON/text)

The initial goal is **instrumentation**, not performance optimization.

---

## Relationship to the MCW Framework

These test beds should be understood as *experimental probes*, not proofs.

They exist to:
- surface coordination patterns
- identify failure modes
- inform further refinement of MCW theory

Results from these instruments may guide future work, including formal user studies or quantitative modeling, but they do not themselves constitute validation.

---

## Status

- Custom GPT test bed: **live (exploratory)**
- Hugging Face Space: **planned**

Contributions, forks, and alternative implementations are encouraged.
