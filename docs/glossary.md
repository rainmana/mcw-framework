# MCW Framework — Canonical Glossary

This glossary defines all core terms used in the Meta-Context Window (MCW) framework. Terms are ordered **bottom-up**: foundational concepts appear first so that each definition can be read without requiring knowledge of later entries.

All definitions are **coordination-scoped**. They describe how information moves between actors and influences shared state — not how cognition works internally.

---

## Foundational Concepts

---

### Entropy

**Type:** Physical / Information-theoretic concept

**Definition:**
Entropy is a measure of uncertainty or unpredictability in a system.

Two forms are relevant to this framework:

- **Thermodynamic entropy (Boltzmann):** `S = k_B ln Ω` — measures the number of possible microstates of a physical system. Sets hard constraints on all information systems.
- **Shannon entropy:** `H(X) = -Σ p(xᵢ) log₂ p(xᵢ)` — measures uncertainty in a probability distribution over symbols. This is the primary lever for MCW analysis.

**What it is not:**
Entropy is not "disorder," "decay," or "evil." It is a constraint on compression, prediction, and control.

**In MCW context:**
MCW degradation corresponds to increasing Shannon entropy in the shared coordination state — rising uncertainty about what the other party knows, intends, or means.

---

### Information Unit (IU)

**Type:** Core framework primitive

**Definition:**
> An Information Unit is the minimal transferable element of information that can influence coordination state between actors.

IUs are the atomic elements through which MCWs form, degrade, and are repaired.

**Key properties:**
- **Substrate-independent:** an IU can exist in text, speech, symbols, prices, signals, or gestures
- **Representation-dependent:** the same IU is encoded differently in different systems (tokens for AI, concepts for humans)
- **Context-sensitive:** an IU's meaning depends on surrounding IUs and prior state
- **Composable:** IUs combine into higher-order structures (arguments, plans, prompts, beliefs)
- **Lossy under transfer:** IU exchange is never perfectly faithful — compression, omission, and distortion are inherent

**Examples:** a stated assumption, a goal, a constraint, a correction, a clarification, a summary

**What IUs are not:**
- Not tokens (tokens are one *representation* of IUs)
- Not facts (facts may span many IUs)
- Not beliefs (beliefs are stabilized IU networks)
- Not values (values shape IU weighting, not IU identity)
- Not meanings in isolation (meaning is relational)

---

### Context Window

**Type:** General concept

**Definition:**
A context window is the bounded set of information that an actor can actively maintain and reason over at a given moment.

All context windows are:
- **Finite** — bounded by cognitive or computational capacity
- **Selective** — not all available information fits or is prioritized
- **Dynamic** — contents shift over time

---

## Actor-Level Concepts

---

### Human Context Window (HCW)

**Type:** Actor-specific context window

**Definition:**
The HCW is the set of information a human actively holds when engaging in an interaction. It includes:

- working memory
- attention and salience weighting
- active goals and intent
- unspoken assumptions
- emotional state and timing

**Key characteristic:**
The HCW is **not enumerable** and advances **continuously** — including between conversational turns. A human may update their internal context window without externalizing that update.

---

### Artificial Context Window (ACW)

**Type:** Actor-specific context window

**Definition:**
The ACW is the bounded computational context that an AI system (typically a large language model) maintains during an interaction. It includes:

- active tokens and embeddings
- retrieved information (e.g., via RAG)
- model weights and prior training
- attention patterns over the current input

**Key characteristic:**
The ACW is **enumerable and formally bounded**. It updates only when new input is provided. It does not advance between turns.

---

### Meta-Context Window (MCW)

**Type:** Emergent coordination construct — the central concept of this framework

**Definition:**
> The Meta-Context Window is the dynamically maintained shared state of meaning, salience, intent, and continuity that emerges through ongoing interaction between one or more human context windows (HCWs) and one or more artificial context windows (ACWs).

More formally, MCW is a **coupling function**:

> **MCW = f(HCW₁…HCWₙ, ACW₁…ACWₘ, T, C)**

Where T is time/interaction history and C is communication channel constraints (bandwidth, latency, modality, noise).

**Key properties:**
- **Emergent:** MCW does not exist in either party alone; it arises from interaction
- **Bidirectional:** neither party owns it; both can degrade or repair it
- **Temporal:** exists in time, not in storage; decays without maintenance
- **Lossy:** not all internal state is transmitted; compression and omission are inherent
- **Not a sum or product:** MCW captures interaction dynamics that simple aggregation cannot represent

**What MCW is not:**

| What it is not | Why the distinction matters |
|---|---|
| Not the AI's context window (ACW) | Increasing token limits does not automatically improve MCW |
| Not chat history | A transcript is a record; MCW is a living coordination state |
| Not memory | Memory stores information; MCW aligns interpretation and relevance |
| Not RAG or retrieval | RAG can improve ACW while actively harming MCW |
| Not UI/UX | UI/UX influences bandwidth; MCW is the resulting shared state |
| Not prompt quality | Good prompts help *initialize* MCW; they cannot maintain or repair it |
| Not alignment or ethics | Those are *contents* that pass through MCW; MCW is the transport/synchronization layer |

---

## Process Concepts

---

### IU Flow

**Type:** Process model

**Definition:**
IU flow describes the five stages through which Information Units travel during any communicative act:

1. **Selection** — the actor chooses which IUs to externalize (governed by salience, intent, and incentives)
2. **Encoding** — IUs are compressed into a transmissible form (language, tokens, symbols)
3. **Transmission** — IUs pass through a constrained channel (latency, bandwidth, noise)
4. **Decoding** — the receiving actor reconstructs IUs using prior context and assumptions
5. **Integration** — IUs update the receiver's internal context window

MCW health is determined by cumulative fidelity across all five stages. Failure at any stage contributes to MCW entropy.

---

### System Prompt (MCW context)

**Type:** Derived concept — MCW initialization artifact

**Definition:**
A system prompt is a preloaded, static IU bundle injected into an ACW prior to MCW formation.

**Role in MCW:**
System prompts shape early IU selection and weighting and can reduce initial entropy — but they do not participate in MCW. They are not bidirectional, not temporally adaptive, and not capable of repair. They are initialization artifacts, not coordination solutions.

> A system prompt is the genome of the interaction. It sets initial conditions. It does not govern how the organism adapts.

**Implication:**
Overly opaque or rigid system prompts act as hidden variables (see *Constraint Opacity*) that can increase initial MCW entropy rather than reduce it.

---

## Failure Modes

---

### Drift (Silent Desynchronization)

**Type:** MCW failure mode

**Definition:**
Gradual, unacknowledged divergence between participating context windows. Neither party recognizes that their shared state is degrading.

**Early signals:** Responses feel technically correct but irrelevant; clarification requests arrive late; "that's not what I meant" appears only after significant effort has been invested.

**Key danger:** Drift feels like progress until it suddenly doesn't.

---

### Asymmetric State Advancement

**Type:** MCW failure mode

**Definition:**
One actor's context window advances — typically through off-turn reasoning or access to external information — without that advancement being externalized to the other party. This creates a phase lag between HCW and ACW.

**Early signals:** Frustration at "having to repeat myself"; the sense that one side is "behind"; resets that worsen rather than repair.

**Key danger:** Resetting the ACW does not reset the HCW; the asymmetry persists or grows.

---

### False Alignment

**Type:** MCW failure mode

**Definition:**
A state in which both parties believe they are coordinated when they are not. Shared language masks divergent interpretation; agreement is inferred rather than verified.

**Early signals:** Confidence increases while actual accuracy decreases; later revelations feel shocking rather than corrective; outcomes fail despite apparent consensus.

**Key danger:** False alignment suppresses the repair signals that would otherwise trigger correction, allowing drift to compound.

---

### Overcompression

**Type:** MCW failure mode

**Definition:**
Critical IU distinctions are lost due to premature or aggressive summarization. Nuance is sacrificed for efficiency; edge cases disappear from the shared state.

**Early signals:** Summaries feel "off" but are difficult to object to specifically; discomfort without a clear articulable error; edge cases vanish from discussion.

**Key danger:** Overcompressed IUs are difficult to recover — lost distinctions are no longer visible to either party.

---

### Constraint Opacity

**Type:** MCW failure mode

**Definition:**
Hidden variables — such as undisclosed system constraints, policy restrictions, or unstated assumptions — influence one party's behavior without being legible to the other. These act as exogenous constraints on the coupling function.

**Early signals:** Confusing refusals or hedges; repair attempts targeting the wrong cause; misattribution to model incompetence.

**Key danger:** Neither party can locate the source of breakdown; repair is systematically misdirected.

---

### Repair Suppression

**Type:** MCW failure mode

**Definition:**
Signals that would normally trigger MCW repair — clarifying questions, expressions of uncertainty, requests for restatement — are discouraged, ignored, or penalized.

**Early signals:** Clarifying questions drop; misunderstandings recur without correction; silence replaces productive disagreement.

**Key danger:** Functionally equivalent to immune suppression. The MCW loses its self-correcting capacity, and failures accumulate unchecked.

---

## Repair Operations

---

### Re-grounding

**Type:** IU repair operation

**Definition:**
Reintroducing foundational IUs to restore a shared reference point. Typically involves restating goals, assumptions, and scope.

*Example:* "Let's step back — what are we actually trying to accomplish here?"

---

### Decompression

**Type:** IU repair operation

**Definition:**
Expanding a compressed IU bundle back into its component IUs. Reverses overcompression by recovering lost distinctions.

*Example:* "Can we break that summary back out into its parts?"

---

### Re-weighting

**Type:** IU repair operation

**Definition:**
Explicitly adjusting IU salience — clarifying which information matters most and which can be safely deprioritized.

*Example:* "The constraint I mentioned earlier matters more than anything else in this conversation."

---

### Disambiguation

**Type:** IU repair operation

**Definition:**
Splitting an overloaded IU into its distinct components. Addresses false alignment caused by shared language with divergent meaning.

*Example:* "When you said 'optimize,' did you mean for speed, for accuracy, or for both?"

---

### Synchronization

**Type:** IU repair operation

**Definition:**
Aligning the IU timelines of participating actors — surfacing off-turn state changes to close asymmetric state advancement.

*Example:* "Since my last message I've been thinking about this differently — here's what changed."

---

## Measurement Proxies

The following are qualitative coordination proxies, not performance metrics. They are used in toy experiments to support structured reflection using 0–3 ordinal scales.

---

### MCW Health (H)

Perceived shared understanding between participants. Higher values indicate stronger alignment.

`0 = broken / 3 = strong`

---

### Repair Cost (R)

Effort required to realign after a coordination failure. Higher values indicate more costly repair.

`0 = low / 3 = high`

---

### Drift Rate (D)

Speed at which the shared coordination state diverges. Higher values indicate faster degradation.

`0 = stable / 3 = rapid`

---

### Misattribution (M)

Tendency to blame coordination failures on agent capability rather than shared context. Higher values indicate more frequent mislabeling.

`0 = none / 3 = frequent`

---

## Framework Meta-Concepts

---

### OSI Layers of Understanding

**Type:** Framework design principle

**Definition:**
A layered accessibility model — adapted from the OSI networking model — that organizes framework concepts at multiple compression levels. Each layer describes the same underlying concepts at a different level of abstraction and formality.

| Layer | Audience | Description |
|-------|----------|-------------|
| 0 | Anyone | Intuition only — "Are we on the same page?" |
| 1 | Generalists | Concepts with plain-language definitions |
| 2 | STEM-adjacent | Formal definitions with equations |
| 3 | Researchers | System models, entropy flows, phase transitions |
| 4 | Builders | Implementation, simulations, code |
| 5 | Domain specialists | Case studies across specific fields |

**Critical rule:** No concept may appear at a higher layer unless it already exists at a lower layer in compressed form. This prevents mystification, gatekeeping, and semantic drift.

---

### MCW Constitution

**Type:** Framework design principle

**Definition:**
A proposed short governance document encoding the core invariants of the framework: layering rules, definition immutability, compression invariance, mutation/extension rules, and anti-capture principles. The MCW Constitution is the immune system of the framework as a societal IU.

*Status: Proposed, not yet written.*

---

*This glossary is intended to evolve. If a term appears in any framework document without a definition here, that is a gap to be filled — not a concept to be assumed.*
