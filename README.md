# Meta-Context Window (MCW) Framework

## Motivation

As AI systems become more capable, a growing class of failures persists even when models are powerful, prompts are well-formed, and tasks are reasonable.

These failures are often described as:

* hallucinations
* misunderstanding
* lack of reasoning
* alignment problems
* “the model not getting it”

The MCW framework proposes that **many of these failures are better explained as coordination breakdowns**, not capability failures.

In particular, MCW focuses on what happens when:

* humans and AI operate with **different internal context windows**
* information is **lost, compressed, misweighted, or delayed**
* repair is **implicit, suppressed, or too costly**

---

## Core Claim (Minimal and Testable)

> **Many failures in human–AI collaboration arise from degraded shared context, not from lack of intelligence or knowledge.**

MCW offers a way to:

* name this failure mode
* reason about it systematically
* design interactions that reduce it

---

## What Is a Meta-Context Window (MCW)?

### Informal definition

A **Meta-Context Window** is the *shared coordination state* that emerges when two or more actors exchange information over time.

It is not stored in any single mind or model.

It exists only insofar as:

* information is exchanged
* interpreted
* integrated
* repaired when necessary

---

### Formal definition

> **MCW is the evolving coordination state induced by the exchange of Information Units (IUs) between actors operating under constrained context windows.**

Key implications:

* MCW is **emergent**
* MCW can **degrade**
* MCW can be **repaired**
* MCW quality is **independent of raw intelligence**

---

## What MCW Is *Not*

To avoid overreach, MCW explicitly does **not** claim to be:

* a theory of intelligence
* a theory of consciousness
* a replacement for alignment or safety research
* a model of internal cognition
* a claim that all failures are coordination failures

MCW is a **lens**, not a universal explanation.

---

## Information Units (IUs)

MCW is grounded in a simple abstraction: **Information Units**.

### Definition

> **An Information Unit (IU) is the minimal transferable element of information that can influence coordination state between actors.**

Examples:

* a stated assumption
* a goal
* a constraint
* a clarification
* a summary
* a correction

IUs are:

* **substrate-independent** (text, speech, symbols, prices, signals)
* **representation-dependent** (tokens for AI, concepts for humans)
* **context-sensitive**
* **composable**
* **lossy under transfer**

---

### What IUs Are Not

IUs are not:

* tokens
* facts
* beliefs
* values
* meanings in isolation

They are coordination-relevant informational elements.

---

## How MCW Degrades

From an information-theoretic perspective, MCW degradation corresponds to **increasing uncertainty about shared IU state**.

Common failure modes include:

* **Omission** – relevant IUs are not externalized
* **Overcompression** – multiple IUs are collapsed too early
* **Misweighting** – salience differs between actors
* **Constraint opacity** – hidden variables affect responses
* **Phase lag** – one actor advances context off-turn

These failures compound over time if not repaired.

---

## Repair as a First-Class Operation

MCW treats repair not as a social nicety, but as a **core coordination primitive**.

Canonical repair operations include:

* **Re-grounding** – restating goals and assumptions
* **Decompression** – expanding summaries back into components
* **Re-weighting** – clarifying what matters most
* **Disambiguation** – splitting overloaded terms
* **Synchronization** – aligning context timelines

Healthy MCWs make repair:

* explicit
* cheap
* early

---

## Why This Is Not Just “Prompt Engineering”

Traditional prompt engineering focuses on:

* shaping outputs
* controlling behavior
* increasing compliance

MCW-aware prompting focuses on:

* reducing hidden variables
* lowering repair cost
* preserving shared context
* making uncertainty visible

In MCW terms:

> **A system prompt is an initialization artifact, not a coordination solution.**

It injects static IUs early, but **cannot maintain or repair MCW on its own**.

---

## Toy Experiments (How This Can Be Tested)

MCW is intentionally designed to be testable without special access or tooling.

This repository includes **toy experiments** that examine:

* false alignment
* asymmetric state advancement
* overcompression damage
* constraint opacity
* repair suppression

These experiments:

* are qualitative by design
* can be run by individuals or teams
* apply to human–human and human–AI interaction
* generate interpretable outcomes beyond pass/fail

If MCW is not useful, these experiments should fail quietly.

---

## Why This May Be Useful

MCW provides:

* a vocabulary for coordination failures
* a way to separate capability from interaction quality
* a framework for designing better human–AI workflows
* a bridge between HCI, information theory, and practical use

Even if incomplete or partially wrong, MCW aims to be:

* locally useful
* falsifiable
* adaptable across domains

---

## Status and Intent

This framework is **early-stage** and **exploratory**.

Primary goals:

* reduce friction in real human–AI collaboration
* provide testable coordination hypotheses
* invite critique, refinement, or falsification

This repository is meant to be:

* forked
* challenged
* extended
* used experimentally

---

## Citation

If you use this framework in academic or technical work, please cite:

> [William "Alec" Akin]. *Meta-Context Window (MCW) Framework*. GitHub repository, 2026.

A formal citation entry will be provided as the framework matures.

