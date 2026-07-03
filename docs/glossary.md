# MCW Framework — Canonical Glossary

This glossary defines all core terms used in the Meta-Context Window (MCW) framework. Terms are ordered **bottom-up**: foundational concepts appear first so that each definition can be read without requiring knowledge of later entries.

All definitions are **coordination-scoped**. They describe how information moves between actors and influences shared state — not how cognition works internally.

**Status:** Canonical (Constitution [Article I](constitution.md#article-i-definition-immutability)). Empirical assertions in this glossary carry inline evidence tags `[L0]`–`[L4]` per [Article IV](constitution.md#article-iv-epistemic-floor); see the [Evidence Layers](#evidence-layers-l0l4) entry. Each entry carries a **Layer 0 gloss** — a one-sentence plain-language form — so the [Article II](constitution.md#article-ii-layering-invariant) layering invariant is checkable per entry. Which fields of an entry are frozen and which are amendable is specified in the [change policy](#glossary-change-policy-frozen-vs-amendable-fields) at the end of this page.

---

## Foundational Concepts

---

### Entropy

**Type:** Physical / Information-theoretic concept

**Layer 0 gloss:** The less predictable something is, the more information it takes to pin down.

**Definition:**
Entropy is a measure of uncertainty or unpredictability in a system.

Two forms are relevant to this framework:

- **Thermodynamic entropy (Boltzmann):** `S = k_B ln Ω` — measures the number of possible microstates of a physical system. Sets hard constraints on all information systems.
- **Shannon entropy:** `H(X) = -Σ p(xᵢ) log₂ p(xᵢ)` — measures uncertainty in a probability distribution over symbols. This is the primary lever for MCW analysis.

**What it is not:**
Entropy is not "disorder," "decay," or "evil." It is a constraint on compression, prediction, and control.

**In MCW context:**
MCW degradation is described as rising uncertainty about what the other party knows, intends, or means — in the *spirit* of Shannon entropy `[L0]`. This correspondence is informal: no random variable, sample space, or probability distribution over the coordination state has been defined, so "MCW entropy," wherever it appears in framework documents, is an intuition pump rather than a computable quantity. The framework's actual measurement program is [H/R/D/M](#measurement-proxies). The Boltzmann form above acknowledges physical grounding and does no analytical work. Defining a computable estimator (or retiring the phrase) is tracked as open work.

---

### Information Unit (IU)

**Type:** Core framework primitive

**Layer 0 gloss:** The smallest piece of information that can change where the two of you stand.

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

**Scope note:** how to *count* IUs — whether an utterance is one IU or three — is an open problem. Candidate individuation criteria, a segmentation reliability plan, and the resulting caveats for countability-dependent claims are analyzed in the [IU individuation working note](working_notes/iu_individuation.md); until a criterion is adopted (which would be a declared Article V extension), quantitative IU claims should be phrased against planted, pre-registered distinctions.

**What IUs are not:**
- Not tokens (tokens are one *representation* of IUs)
- Not facts (facts may span many IUs)
- Not beliefs (beliefs are stabilized IU networks)
- Not values (values shape IU weighting, not IU identity)
- Not meanings in isolation (meaning is relational)

---

### Context Window

**Type:** General concept

**Layer 0 gloss:** What an actor can hold in mind at once.

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

**Layer 0 gloss:** Everything the human is holding in mind right now.

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

**Layer 0 gloss:** Everything the AI can see right now.

**Definition:**
The ACW is the bounded computational context that an AI system (typically a large language model) maintains during an interaction. It includes:

- active tokens and embeddings
- retrieved information (e.g., via RAG)
- model weights and prior training
- attention patterns over the current input

**Key characteristic:**
The ACW is **enumerable and formally bounded**. It advances only when input arrives — where input includes user messages, tool results, retrieved content, and scheduled invocations — and never spontaneously. In agentic and background configurations the ACW can therefore advance *between conversational turns*; what it cannot do is advance without input. The coordination-relevant asymmetry with the HCW is not turn-boundedness but **spontaneity**: the HCW advances continuously and unpromptedly; the ACW advances discretely and only on input.

**Definition history:** the v0.2 (April 2026) key characteristic read "It updates only when new input is provided. It does not advance between turns." — amended July 2026 because that text was false for agentic, tool-using, and background AI systems (the dominant deployment pattern the framework targets) and contradicted Article III's claimed applicability to AI–AI systems without modification. Prior text preserved here per the Amendment Procedure; the asymmetry that motivates the framework (continuous/spontaneous vs. discrete/input-driven) is retained and sharpened.

---

### Meta-Context Window (MCW)

**Type:** Emergent coordination construct — the central concept of this framework

**Layer 0 gloss:** The shared page you are both on — or think you are on.

**Definition:**
> The Meta-Context Window is the dynamically maintained shared state of meaning, salience, intent, and continuity that emerges through ongoing interaction between one or more human context windows (HCWs) and one or more artificial context windows (ACWs).

More formally, MCW is a **coupling function**:

> **MCW = f(HCW₁…HCWₙ, ACW₁…ACWₘ, T, C)**

Where T is time/interaction history and C is communication channel constraints (bandwidth, latency, modality, noise).

**Notation status:** informal `[L0]` — the coupling function is a mnemonic, not mathematics. It has no defined codomain, metric, or functional form, and one input (the HCW) is not enumerable, so the notation licenses no quantitative inference (Article IV). Its content is the qualitative properties listed below. Either a proper definition or explicit retirement of the notation is tracked as open work; until then, treat every appearance of this equation as shorthand for those properties.

**Key properties:**
- **Emergent:** MCW does not exist in either party alone; it arises from interaction
- **Bidirectional:** neither party owns it; both can degrade or repair it
- **Temporal:** exists in time, not in storage; decays without maintenance `[L1]`
- **Lossy:** not all internal state is transmitted; compression and omission are inherent
- **Not a sum or product:** MCW captures interaction dynamics that simple aggregation cannot represent

**What MCW is not:**

| What it is not | Why the distinction matters |
|---|---|
| Not the AI's context window (ACW) | Increasing token limits does not automatically improve MCW |
| Not chat history | A transcript is a record; MCW is a living coordination state |
| Not memory | Memory stores information; MCW aligns interpretation and relevance |
| Not RAG or retrieval | RAG can improve ACW while actively harming MCW `[L1]` |
| Not UI/UX | UI/UX influences bandwidth; MCW is the resulting shared state |
| Not prompt quality | Good prompts help *initialize* MCW; they cannot maintain or repair it |
| Not alignment or ethics | Those are *contents* that pass through MCW; MCW is the transport/synchronization layer |

---

## Process Concepts

---

### IU Flow

**Type:** Process model

**Layer 0 gloss:** Every message is chosen, packed, sent, unpacked, and absorbed — and can fail at each step.

**Definition:**
IU flow describes the five stages through which Information Units travel during any communicative act:

1. **Selection** — the actor chooses which IUs to externalize (governed by salience, intent, and incentives)
2. **Encoding** — IUs are compressed into a transmissible form (language, tokens, symbols)
3. **Transmission** — IUs pass through a constrained channel (latency, bandwidth, noise)
4. **Decoding** — the receiving actor reconstructs IUs using prior context and assumptions
5. **Integration** — IUs update the receiver's internal context window

MCW health is hypothesized to depend on cumulative fidelity across all five stages `[L0]`. Failure at any stage contributes to MCW degradation ("MCW entropy" in the framework's informal usage — see [Entropy](#entropy)).

---

### System Prompt (MCW context)

**Type:** Derived concept — MCW initialization artifact

**Layer 0 gloss:** The note the AI reads before the conversation starts.

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

**Layer 0 gloss:** You've slowly stopped talking about the same thing, and neither of you has noticed.

**Definition:**
Gradual, unacknowledged divergence between participating context windows. Neither party recognizes that their shared state is degrading.

**Early signals:** Responses feel technically correct but irrelevant; clarification requests arrive late; "that's not what I meant" appears only after significant effort has been invested.

**Key danger:** Drift feels like progress until it suddenly doesn't.

---

### Asymmetric State Advancement

**Type:** MCW failure mode

**Layer 0 gloss:** One of you moved on while the other stood still.

**Definition:**
One actor's context window advances — typically through off-turn reasoning or access to external information — without that advancement being externalized to the other party. This creates a phase lag between HCW and ACW.

**Early signals:** Frustration at "having to repeat myself"; the sense that one side is "behind"; resets that worsen rather than repair.

**Key danger:** Resetting the ACW does not reset the HCW; the asymmetry persists or grows.

**Scope note:** the definition is direction-symmetric — *either* party's window may advance off-turn without externalization. With the amended ACW definition (above), AI-side off-turn advancement via tool use, background runs, or scheduled work is a live case, not only the human side; the "resets worsen" danger applies in both directions.

---

### False Alignment

**Type:** MCW failure mode

**Layer 0 gloss:** You both said yes to different things.

**Definition:**
A state in which both parties believe they are coordinated when they are not. Shared language masks divergent interpretation; agreement is inferred rather than verified.

**Early signals:** Confidence increases while actual accuracy decreases; later revelations feel shocking rather than corrective; outcomes fail despite apparent consensus.

**Key danger:** False alignment suppresses the repair signals that would otherwise trigger correction, allowing drift to compound.

---

### Overcompression

**Type:** MCW failure mode

**Layer 0 gloss:** The summary threw away the part that mattered.

**Definition:**
Critical IU distinctions are lost due to premature or aggressive summarization. Nuance is sacrificed for efficiency; edge cases disappear from the shared state.

**Early signals:** Summaries feel "off" but are difficult to object to specifically; discomfort without a clear articulable error; edge cases vanish from discussion.

**Key danger:** Overcompressed IUs are difficult to recover — lost distinctions are no longer visible to either party.

---

### Constraint Opacity

**Type:** MCW failure mode

**Layer 0 gloss:** One of you is following a rule the other can't see.

**Definition:**
Hidden variables — such as undisclosed system constraints, policy restrictions, or unstated assumptions — influence one party's behavior without being legible to the other. These act as exogenous constraints on the coupling function.

**Early signals:** Confusing refusals or hedges; repair attempts targeting the wrong cause; misattribution to model incompetence.

**Key danger:** Neither party can locate the source of breakdown; repair is systematically misdirected.

---

### Repair Suppression

**Type:** MCW failure mode

**Layer 0 gloss:** Asking "wait, what do you mean?" has become too costly to say.

**Definition:**
Signals that would normally trigger MCW repair — clarifying questions, expressions of uncertainty, requests for restatement — are discouraged, ignored, or penalized.

**Early signals:** Clarifying questions drop; misunderstandings recur without correction; silence replaces productive disagreement.

**Key danger:** Functionally equivalent to immune suppression. The MCW loses its self-correcting capacity, and failures accumulate unchecked.

---

## Repair Operations

---

### Re-grounding

**Type:** IU repair operation

**Layer 0 gloss:** "Let's step back to what we're actually doing."

**Definition:**
Reintroducing foundational IUs to restore a shared reference point. Typically involves restating goals, assumptions, and scope.

*Example:* "Let's step back — what are we actually trying to accomplish here?"

---

### Decompression

**Type:** IU repair operation

**Layer 0 gloss:** Unpack the summary.

**Definition:**
Expanding a compressed IU bundle back into its component IUs. Reverses overcompression by recovering lost distinctions.

*Example:* "Can we break that summary back out into its parts?"

---

### Re-weighting

**Type:** IU repair operation

**Layer 0 gloss:** Say what matters most.

**Definition:**
Explicitly adjusting IU salience — clarifying which information matters most and which can be safely deprioritized.

*Example:* "The constraint I mentioned earlier matters more than anything else in this conversation."

---

### Disambiguation

**Type:** IU repair operation

**Layer 0 gloss:** Same word, different meanings — split them.

**Definition:**
Splitting an overloaded IU into its distinct components. Addresses false alignment caused by shared language with divergent meaning.

*Example:* "When you said 'optimize,' did you mean for speed, for accuracy, or for both?"

---

### Synchronization

**Type:** IU repair operation

**Layer 0 gloss:** Tell the other side what changed while they weren't looking.

**Definition:**
Aligning the IU timelines of participating actors — surfacing off-turn state changes to close asymmetric state advancement.

*Example:* "Since my last message I've been thinking about this differently — here's what changed."

---

## Measurement Proxies

The following are qualitative coordination proxies, not performance metrics. They are used in toy experiments to support structured reflection using 0–3 ordinal scales.

---

### MCW Health (H)

**Layer 0 gloss:** How well do we understand each other right now?

Perceived shared understanding between participants. Higher values indicate stronger alignment.

`0 = broken / 3 = strong`

---

### Repair Cost (R)

**Layer 0 gloss:** How hard was it to get back on the same page?

Effort required to realign after a coordination failure. Higher values indicate more costly repair.

`0 = low / 3 = high`

---

### Drift Rate (D)

**Layer 0 gloss:** How fast are we sliding apart?

Speed at which the shared coordination state diverges. Higher values indicate faster degradation.

`0 = stable / 3 = rapid`

---

### Misattribution (M)

**Layer 0 gloss:** Are we blaming the tool when the problem is the conversation?

Tendency to blame coordination failures on agent capability rather than shared context. Higher values indicate more frequent mislabeling.

`0 = none / 3 = frequent`

---

## Framework Meta-Concepts

---

### OSI Layers of Understanding

**Type:** Framework design principle

**Layer 0 gloss:** The same idea can be said simply or precisely — and must always be sayable simply.

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

**Per-entry annotation:** every glossary entry carries a **Layer 0 gloss** line — its Layer 0 compressed form — so this rule is checkable rather than aspirational. An entry whose content cannot be glossed in one plain sentence violates the layering invariant.

**Not to be confused with:** the [Evidence Layers L0–L4](#evidence-layers-l0l4) of Constitution Article IV, which grade the strength of empirical support, not accessibility.

**Notation:** where compact notation is needed, accessibility layers are written **A0–A5**; bare `L`*n* is reserved for evidence layers. This resolves the notation collision an earlier version of this entry flagged as open. Prose may still say "Layer 0" where the ladder is unambiguous from context (as in the per-entry "Layer 0 gloss").

---

### Evidence Layers (L0–L4)

**Type:** Framework meta-concept — canonical in [Constitution Article IV](constitution.md#article-iv-epistemic-floor)

**Layer 0 gloss:** How much proof stands behind a claim.

**Definition:**
A five-rung ladder declaring the strength of evidence behind any empirical claim about MCW dynamics. The definitions are fixed by Article IV of the Constitution:

- **L0 — Illustration:** Naturalistic observation, no controls; used to demonstrate recognizability only
- **L1 — Practitioner observation:** Extended personal use; subject to positionality bias; not generalizable
- **L2 — Designed pilot:** Structured observation with hypothesis; single observer or small N; no inter-rater reliability
- **L3 — Pilot with reliability:** Multi-rater pilot; inter-rater reliability reported; generalizable with caution
- **L4 — Controlled study:** Random assignment, control conditions, validated instruments; generalizable with stated scope

**Usage convention:** empirical assertions in framework documents carry an inline tag `[L0]`–`[L4]` at the claim site, and pages that make empirical claims state their overall evidence layer in a Status line. No claim may be stated above the layer its supporting data occupies (Article IV). The current framework is at L0–L1 for all empirical claims. Marker *presence* is checked mechanically in CI once [Constitution as Code](constitution_as_code.md) Phase 0 is in place; until every page is tagged, an untagged empirical sentence anywhere in the framework is a defect to be tagged, downgraded, or withdrawn — not an exemption from this convention.

**What evidence layers are not:**

- Not the [OSI Layers of Understanding](#osi-layers-of-understanding) (the accessibility ladder, written A0–A5): accessibility layers describe how compressed a *presentation* is; evidence layers describe how strong the *support* for a claim is. Bare `L`*n* notation always means an evidence layer
- Not a quality score: an honestly tagged L0 claim is fully legitimate; an L1 claim dressed as L3 is not

---

### MCW Constitution

**Type:** Framework design principle

**Layer 0 gloss:** The rules that keep the framework meaning the same thing for everyone.

**Definition:**
A short governance document encoding the core invariants of the framework: definition immutability, layering rules, substrate independence, the epistemic floor, extension protocol, anti-capture principles, compression invariance, and scope boundaries. The MCW Constitution is the immune system of the framework as a societal IU.

*Status: Adopted — [MCW Constitution v1.0](constitution.md), April 2026. An earlier version of this entry read "Proposed, not yet written"; that status line was stale, not a definitional change.*

---

## Glossary Change Policy — Frozen vs. Amendable Fields

Constitution [Article I](constitution.md#article-i-definition-immutability) freezes canonical definitions, while this glossary's closing note declares it "intended to evolve." Both are true — at different granularity. This section specifies the field-level policy.

**Frozen fields** — for the Article I constructs (MCW, HCW, ACW, IU, the six failure modes, the five repair operations, and the H/R/D/M proxies), the following change only through a declared departure or the [Amendment Procedure](constitution.md#amendment-procedure) (prior text preserved, rationale recorded):

- the **Definition** text, including blockquoted definition sentences
- **Key properties** / **Key characteristic** lists
- **What it is not** exclusion lists (Article VII requires these preserved under compression)
- the 0–3 scale semantics of H, R, D, and M

**Amendable fields** — ordinary review, no amendment required, provided the change does not alter the meaning of any frozen field:

- **Type** lines, **Layer 0 gloss** annotations, **Notation status** annotations, **Definition history** records, **Scope note** clarifications, evidence tags, cross-references, links, and formatting
- **Examples**
- **Early signals** and **Key danger** notes (illustrative, not definitional)
- Status lines and section ordering

Entries not listed in Article I (Entropy, Context Window, IU Flow, System Prompt, OSI Layers of Understanding, Evidence Layers as restated here, and this policy) are governed by ordinary review, with Article IV and Article VII discipline still applying to their content. The Evidence Layer definitions themselves are fixed in Constitution Article IV; the glossary entry restates them and must be corrected if it ever diverges.

A mechanical guard for the frozen fields (canonical text pinned by hash and verified in CI) is specified in [Constitution as Code](constitution_as_code.md).

---

*This glossary is intended to evolve within the change policy above: frozen fields change only by declared amendment; everything else by ordinary review. If a term appears in any framework document without a definition here, that is a gap to be filled — not a concept to be assumed.*
