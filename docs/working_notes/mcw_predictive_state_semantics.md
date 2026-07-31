# Working Note — MCW Predictive-State Semantics and Context Topology

**Status:** Working note · Evidence: L0 — mathematical construction and adjacent-layer proposal, not empirical validation or canon. Nothing in this note replaces or redefines the canonical [MCW](../glossary.md#meta-context-window-mcw), [HCW](../glossary.md#human-context-window-hcw), [ACW](../glossary.md#artificial-context-window-acw), [IU](../glossary.md#information-unit-iu), failure modes, repair operations, or H/R/D/M proxies. The object defined below is an **operational predictive projection of evidence about coordination state**, not the canonical MCW itself.

**Working label:** MCW Predictive-State Semantics (MCW-PSS). The label is provisional. This note follows the declaration, non-contradiction, falsifiability, and traceability discipline of Constitution [Articles II, V, and VIII](../constitution.md), but it is not yet a declared extension.

!!! tip "New to the mathematics?"
    Begin with the [ground-up MCW-PSS mathematics guide](mcw_predictive_state_semantics_guide.md). It develops the idea from one ordinary scheduling conversation, explains how to say and read the core equations, defines the notation symbol by symbol, and links each simplified statement back to this formal note.

---

## A0 — The idea without mathematics

> Two complete context conditions count as the same operational coordination state when no allowed future coordination test can tell them apart.

The context affecting a human–AI interaction is not confined to the text presently visible to a model. It can be distributed across humans, AI agents, retrieval systems, memories, tools, compressors, routers, policies, interfaces, and environments. Each component sees or transforms only part of that context.

This note asks whether the resulting coordination state can be represented by what it predicts: how the system will respond to future ordinary exchanges, diagnostic questions, repairs, channel changes, and task interventions. Histories with identical relevant futures may be folded together. Histories with distinguishable futures must remain separate.

This does **not** claim that:

- every component is an actor or owns a canonical context window;
- the full human cognitive state can be read or enumerated;
- an observed transcript is the MCW;
- MCW is a product capability possessed by a model, prompt, RAG system, or architecture;
- a finite or low-dimensional coordination state always exists;
- mathematical consistency supplies empirical validation.

---

## 1. Why formalize this way?

The canonical glossary currently writes

$$
\mathrm{MCW}=f(\mathrm{HCW}_1,\ldots,\mathrm{HCW}_n,
\mathrm{ACW}_1,\ldots,\mathrm{ACW}_m,T,C),
$$

and correctly marks that expression as a mnemonic rather than mathematics: it has no declared codomain, metric, or functional form. This note does not silently upgrade that expression. It introduces a separate operational model with:

1. a declared system boundary;
2. typed state, intervention, and observation spaces;
3. a probability law for state change and observation;
4. actor-relative information sets;
5. an exact future-behavior equivalence relation;
6. an explicit distinction between exact and approximate folding;
7. identifiable limits on elicitation, compression, and reconstruction.

The objective is not to mathematize every human meaning. It is to define exactly which distinctions a particular coordination inquiry requires and what evidence could or could not recover them.

---

## 2. A typed context topology

### A1 gloss

> Context can be stored, selected, transformed, routed, hidden, or interpreted by different parts of a system; agency is only one role in that network.

Fix a declared system boundary and a typed directed graph

$$
G=(V,E,\tau),
$$

where $V$ is a set of components, $E$ is a set of directed information or control paths, and $\tau$ assigns roles. Candidate roles include:

| Role | Examples | Context function |
|---|---|---|
| Participant | Human, AI agent | Interprets observations and can select actions |
| Reservoir | Transcript, vector store, long-term memory, model parameters | Holds potentially reachable context |
| Aperture | Retrieval query, attention allocation, token budget, human attention | Selects what becomes locally available |
| Operator | Compressor, ranker, policy filter, MoE router | Transforms, weights, suppresses, or routes context |
| Channel | UI, API, STT/TTS, BCI, agent message bus | Carries a representation between components |
| Integrator | Human, model, agent, orchestrator | Incorporates a received representation into future state |
| Governor | System instruction, permission boundary, safety policy, budget | Constrains allowed transitions or observations |

A component may have several roles. Role names are descriptive extensions, not new canonical MCW constructs.

Assume $V$ is finite or countable. For every component $v\in V$, let $(\mathcal X_v,\Sigma_v)$ be its measurable local state space. The global state space is

$$
(\mathcal X,\Sigma)
=
\prod_{v\in V}(\mathcal X_v,\Sigma_v),
\qquad
X_t=(X_t^v)_{v\in V}.
$$

For mathematical convenience, assume these are standard Borel spaces unless a particular application supplies different structure. Finite or countable products then remain standard Borel. This assumption supports regular conditional probabilities; it does not assert that an analyst can inspect every coordinate of $X_t$.

### Actor-relative accessible context

For participant $i$, define the information available by time $t$ as a filtration

$$
\mathcal F_t^i
=
\sigma(\text{observations, actions, memories, and signals available to }i\text{ by }t).
$$

This supplies one formal interpretation of a bounded local context: the information on which that participant’s next action can condition. A component can still affect context without being a participant. A compressor, retriever, router, or hidden governor may alter $\mathcal F_t^i$ or the future transition law even if it has no goals or repair behavior of its own.

### Effective context is scope-relative

“All context” must not expand to the entire universe. Fix a coordination scope $\kappa$. If an interventional model is available, component state $X_t^v$ is **effective context** for $\kappa$ when some admissible change to that state changes a relevant future law:

$$
X_t^v\in\operatorname{Ctx}_\kappa
\quad\Longleftrightarrow\quad
\exists\,\pi,z,z' :
\mathbb P^\pi(Z^\kappa\mid \operatorname{do}(X_t^v=z))
\neq
\mathbb P^\pi(Z^\kappa\mid \operatorname{do}(X_t^v=z')).
$$

The $\operatorname{do}$ notation requires an explicit causal model. Without one, the weaker and purely predictive question is whether observing $X_t^v$ refines the law of a relevant future after the other declared observations are held fixed.

An unretrieved document can therefore be *reachable* context if an admissible query could retrieve it. A file that cannot affect any declared future is outside the scope, even if it exists somewhere in the environment.

---

## 3. Controlled, partially observed dynamics

Let $(\mathcal U,\Sigma_{\mathcal U})$ be an intervention space and $(\mathcal Y,\Sigma_{\mathcal Y})$ an observation space. An intervention may be an IU exchange, prompt, tool event, retrieval, channel change, elicitation, repair operation, model reset, or environmental action.

Represent the bounded system as a controlled stochastic process:

$$
X_0\sim\mu_0,
\qquad
X_{t+1}\sim P_t(\,\cdot\mid X_t,U_t),
\qquad
Y_{t+1}\sim Q_t(\,\cdot\mid X_{t+1},U_t),
$$

where $\mu_0$ is an initial law, $P_t$ is a transition kernel, and $Q_t$ an observation kernel. Time dependence permits nonstationarity. A deterministic system is the special case in which the kernels are point masses. Coordination outcomes are produced by a declared measurable map $g_\kappa$, for example $Z_t^\kappa=g_\kappa(Y_{1:t},U_{0:t-1})$; the map may retain an entire outcome path rather than a scalar score.

If a chosen $X_t$ is not Markov, it can always be augmented by enough history to make the process Markov formally. That move may create an enormous or infinite-dimensional state and therefore does not solve estimation or implementation.

The observable history is

$$
h_t=(u_0,y_1,u_1,y_2,\ldots,u_{t-1},y_t)\in\mathcal H.
$$

Formally, $\mathcal H=\bigsqcup_{t\ge0}(\mathcal U\times\mathcal Y)^t$ with the corresponding disjoint-union sigma-algebra. Historical actions in $h_t$ are treated as realized interventions; the policy that originally selected them is not part of a future comparison unless the scope declares it as state.

A probe policy $\pi=(\pi_j)_{j\ge0}$ is a sequence of nonanticipating measurable kernels that chooses each later intervention from the **future suffix** observed after the comparison time. The same policy is initialized at $h$ and $h'$: it may adapt to later observations, but it may not inspect the identity of the initial prefix and deliberately branch on whether it received $h$ or $h'$. Policies may otherwise be open-loop scripts or adaptive question-and-repair strategies.

---

## 4. Declaring the coordination scope

Every formal state claim is indexed by a scope

$$
\kappa=(G,\mathcal Z^\kappa,\Pi^\kappa,L^\kappa,D^\kappa),
$$

where:

- $G$ is the bounded context topology;
- $\mathcal Z^\kappa$ is the space of coordination-relevant outcomes produced by the declared measurable outcome map $g_\kappa$;
- $\Pi^\kappa$ is the allowed family of future probe or intervention policies;
- $L^\kappa\in\mathbb N\cup\{\infty\}$ is the future horizon;
- $D^\kappa$ is a declared metric on future-outcome laws when the pseudometric and error-bound results below are invoked. Other divergences or losses may be useful, but do not inherit those results automatically.

Candidate observable consequences of the canonical MCW dimensions include:

- **meaning:** referent selection, paraphrase prediction, or interpretation-sensitive action;
- **salience:** priority rankings and behavior under constrained time or tokens;
- **intent:** goal, commitment, and predicted-next-action compatibility;
- **continuity:** correct resumption, chronology, correction incorporation, and reopening conditions;
- **repair:** clarification behavior, repair outcome, and effort under a declared cost model.

These are candidate operationalizations, not validated replacements for H/R/D/M. Raw text similarity alone is not a sufficient coordination outcome.

---

## 5. Predictive-state semantics

### A1 gloss

> A coordination state is what must be remembered about the past to predict every relevant future we agreed to test.

Let $\mathcal H^\kappa\subseteq\mathcal H$ contain the admissible histories for which the controlled generative model defines a continuation. For every $\pi\in\Pi^\kappa$, fix a measurable continuation kernel

$$
\Gamma_\kappa^\pi:
\mathcal H^\kappa\times\Sigma_{(\mathcal Z^\kappa)^{L^\kappa}}
\longrightarrow[0,1],
\qquad
\mathbb P_h^\pi(\,\cdot\,):=\Gamma_\kappa^\pi(h,\,\cdot\,),
$$

where $\mathbb P_h^\pi$ is the law of the coordination-relevant future $Z_{1:L^\kappa}$ when the system continues from $h$ under the same suffix policy $\pi$.

If a history is reached only through a null-probability event, either use a structural/generative version of $\Gamma_\kappa^\pi$, fix a version of the relevant regular conditional law, or exclude that history from $\mathcal H^\kappa$. Statements involving observationally derived conditional laws are therefore understood up to the declared version and almost-sure equivalence.

### Definition 1 — Exact predictive coordination equivalence

$$
h\sim_\kappa h'
\quad\Longleftrightarrow\quad
\mathbb P_h^\pi=\mathbb P_{h'}^\pi
\quad\text{for every }\pi\in\Pi^\kappa.
$$

The operational predictive coordination state is the equivalence class

$$
S_t^\kappa=[h_t]_{\sim_\kappa}
\in
\mathcal S^\kappa:=\mathcal H^\kappa/\!\sim_\kappa.
$$

Equivalently, it can be represented as the prediction-valued object

$$
\sigma_\kappa(h)
=
(\mathbb P_h^\pi)_{\pi\in\Pi^\kappa},
$$

whose codomain is a product of spaces of probability measures. This codomain may be infinite-dimensional. Nothing in the definition guarantees a finite state machine.

Equip $\mathcal S^\kappa$ with the quotient sigma-algebra. The quotient need not itself be standard Borel. Any claim that a measurable estimator, posterior kernel, or recursive implementation exists requires additional regularity; the prediction-valued representation $\sigma_\kappa(h)$ can be used directly when those conditions are available.

**Interpretation boundary:** $S_t^\kappa$ is a task-relative behavioral projection supported by future laws. It is not asserted to be the complete canonical MCW, a complete human mental state, a neural coordinate, or a participant’s own belief.

### Proposition 1 — Exact predictive equivalence is an equivalence relation

**Claim.** $\sim_\kappa$ is reflexive, symmetric, and transitive.

**Proof sketch.** Each property follows from equality of the complete indexed family $(\mathbb P_h^\pi)_{\pi\in\Pi^\kappa}$. In particular, if every future law from $h$ equals the corresponding law from $h'$, and every law from $h'$ equals the corresponding law from $h''$, then every law from $h$ equals the corresponding law from $h''$. $\square$

### Proposition 2 — Minimal predictive sufficiency

Call a measurable representation $\phi:\mathcal H^\kappa\to\mathcal E$ **predictively sufficient** when, for every $\pi\in\Pi^\kappa$, there is a measurable probability kernel $R_\pi$ such that

$$
\mathbb P_h^\pi(\,\cdot\,)
=
R_\pi(\phi(h),\,\cdot\,)
\qquad
\text{for every }h\in\mathcal H^\kappa,
$$

or almost surely when the representation is defined only relative to a history distribution.

**Claim.** $S_t^\kappa$ is sufficient in the set-theoretic sense for the declared future laws. Moreover, any predictively sufficient representation $\phi(h)$ must refine the predictive quotient: there is a map $r$ such that

$$
S_t^\kappa=r(\phi(h_t)).
$$

**Proof sketch.** Sufficiency holds by construction because all histories in one class have identical declared future laws. If $\phi(h)=\phi(h')$ but the two histories were in different predictive classes, some allowed policy would distinguish their future laws, contradicting sufficiency of $\phi$. Thus $r$ exists as a set map. Its measurability requires compatible measurable structures on the representation and quotient. $\square$

This is the direct mathematical bridge to evaluation-tree folding: histories can be merged exactly when no allowed future subtree distinguishes them.

### Proposition 2a — When the quotient supports recursive dynamics

A predictive quotient at one fixed horizon is not automatically a reusable state machine. Suppose instead that equivalence compares all finite future horizons—or the complete infinite future path—and that:

1. $\Pi^\kappa$ contains every admissible finite continuation policy and is closed under conditioning on an action and observation;
2. the future law contains the observations used to update the state;
3. the continuation kernels arise from one jointly measurable, dynamically consistent controlled law, and $\mathcal H^\kappa$ is closed under every supported admissible one-step extension;
4. the quotient admits a standard-Borel measurable realization $q_\kappa:\mathcal H^\kappa\to\mathcal S^\kappa$ whose fibers are exactly the $\sim_\kappa$ classes;
5. the induced one-step history dynamics are **strongly lumpable** through $q_\kappa$.

Let $K_\kappa^Y(dy\mid h,u)$ be the immediate-observation kernel induced by the controlled process after history $h$ and intervention $u$, and let $u\star\pi$ denote the policy that applies $u$ once and then follows suffix policy $\pi$. Dynamic consistency means that this policy composition obeys the disintegration

$$
\mathbb P_h^{u\star\pi}
\!\left(Y_1\in A,Z_{2:}\in C\right)
=
\int_A
\mathbb P_{huy}^{\pi}(Z_{2:}\in C)
K_\kappa^Y(dy\mid h,u)
$$

for the declared future events and chosen structural versions. Strong lumpability then means that there is a measurable quotient transition kernel

$$
\overline K_\kappa:
\mathcal S^\kappa\times\mathcal U
\rightsquigarrow
\mathcal Y\times\mathcal S^\kappa
$$

such that, for every admissible $h,u$ and measurable $A\subseteq\mathcal Y$, $B\subseteq\mathcal S^\kappa$,

$$
\overline K_\kappa(A\times B\mid q_\kappa(h),u)
=
\int_A
\mathbf 1_B\!\left(q_\kappa(huy)\right)
K_\kappa^Y(dy\mid h,u),
$$

and the right-hand side is identical for every representative of $q_\kappa(h)$. Under these conditions the quotient is a controlled Markov state in the kernel sense. This joint kernel—not a pointwise successor selector—is the recursive object used below. A probabilistic-bisimulation construction is one sufficient route to this factorization.

Equality of future laws and existence of pairwise regular conditional probabilities do **not** alone establish this kernel. With continuous observations or uncountable policy families or equivalence classes, the exceptional null set may depend on the policy and representative pair; there need not be one common full-measure set on which a point update is representative-independent.

Only if there additionally exists a jointly measurable map

$$
F_\kappa:
\mathcal S^\kappa\times\mathcal U\times\mathcal Y
\longrightarrow
\mathcal S^\kappa
$$

such that

$$
q_\kappa(huy)=F_\kappa(q_\kappa(h),u,y)
$$

for $K_\kappa^Y(\,\cdot\mid h,u)$-almost every $y$ for every admissible $(h,u)$, with one representative-independent choice of versions, may the quotient be represented by the point update $T_\kappa([h],u,y)=F_\kappa([h],u,y)$. A countable determining family can help construct such a common version when the remaining regularity conditions also hold. For countable discrete observations, equality is pointwise on every shared positive-probability observation.

If the scope uses only a bounded horizon $L^\kappa$, the remaining horizon must be included in the state—or a family $S^{\kappa,\ell}$ must be used for $0\le\ell\le L^\kappa$. Otherwise the quotient is a horizon-specific predictive statistic, not a stationary automaton. The correctly typed default is then a kernel

$$
\overline K_{\kappa,\ell}:
\mathcal S^{\kappa,\ell}\times\mathcal U
\rightsquigarrow
\mathcal Y\times\mathcal S^{\kappa,\ell-1},
\qquad 1\le\ell\le L^\kappa.
$$

Only under the stronger common-version condition may this kernel be realized by a deterministic observation-indexed update

$$
T_{\kappa,\ell}:
\mathcal S^{\kappa,\ell}\times\mathcal U\times\mathcal Y
\longrightarrow
\mathcal S^{\kappa,\ell-1}.
$$

---

## 6. Distance without fake equivalence

Exact equality is fragile in stochastic or estimated systems. Choose a metric $D^\kappa$ on future probability laws—for example, total variation on general measurable outcomes or a task-justified Wasserstein metric on a metric outcome space—and define

$$
d_\kappa(h,h')
=
\sup_{\pi\in\Pi^\kappa}
D^\kappa(\mathbb P_h^\pi,\mathbb P_{h'}^\pi).
$$

If $d_\kappa(H,H')$ will itself be used as a random variable or optimized, assume $\Pi^\kappa$ is countable, has a countable dense subfamily that preserves the supremum, or satisfies joint-measurability conditions ensuring that this supremum is measurable.

When $D^\kappa$ is a bounded metric—or its supremum is finite over the declared policy family—$d_\kappa$ is a pseudometric on histories. Without that finiteness condition it is an extended pseudometric, permitted to take the value $+\infty$. In either case,

$$
h\sim_\kappa h'
\quad\Longleftrightarrow\quad
d_\kappa(h,h')=0.
$$

For total variation, this note uses

$$
D_{\mathrm{TV}}(P,Q)=\sup_A|P(A)-Q(A)|,
$$

which equals one half of the $L^1$ distance when densities exist.

### Warning — $\epsilon$-closeness is not generally transitive

The relation $d_\kappa(h,h')\le\epsilon$ is not necessarily an equivalence relation. For one Bernoulli future outcome with parameters $0$, $0.4$, and $0.8$, adjacent pairs have total-variation distance $0.4$, while the endpoints have distance $0.8$. With $\epsilon=0.4$, the first is “close” to the second and the second to the third, but the first is not close to the third.

Approximate folding therefore requires an explicit abstraction rule, such as:

- clusters whose maximum within-cluster diameter is at most $\epsilon$;
- representative states with a declared maximum radius;
- probabilistic bisimulation metrics with downstream error bounds;
- covers rather than quotient classes.

It must not silently call pairwise $\epsilon$-closeness an equivalence relation.

### Proposition 3 — Bounded-outcome preservation

If $D^\kappa$ is total variation, $d_\kappa(h,h')\le\epsilon$, and $g$ is any measurable future coordination utility with $0\le g\le1$, then for every allowed policy $\pi$,

$$
\left|
\mathbb E_h^\pi[g]-\mathbb E_{h'}^\pi[g]
\right|
\le\epsilon.
$$

This gives $\epsilon$ an operational interpretation: it bounds the change in every normalized future quantity measurable in the declared scope.

---

## 7. Actor beliefs are not the relational state

No participant need know the predictive coordination state. For measurable $B\subseteq\mathcal S^\kappa$, participant $i$ has the eventwise actor-relative conditional belief

$$
b_t^i(B)
=
\mathbb P(S_t^\kappa\in B\mid\mathcal F_t^i).
$$

An analyst has a different belief based on the instrumentation available to the study:

$$
b_t^{\mathrm{obs}}(B)
=
\mathbb P(S_t^\kappa\in B\mid\mathcal F_t^{\mathrm{obs}}).
$$

These conditional probabilities exist eventwise as conditional expectations. Treating $B\mapsto b_t^i(B)$ as a regular posterior probability kernel requires the additional standard-Borel or measurable-prediction representation conditions noted above.

This separates at least three objects that broad appeals to “subjectivity” often collapse:

1. the relational future-behavior class;
2. the human’s belief about that class;
3. the AI’s belief about that class.

A candidate formal signature of [False Alignment](../glossary.md#false-alignment), to be treated as an extension rather than a replacement definition, is that both actors assign high probability to successful coordination while held-out future laws reveal incompatible interpretation or action.

---

## 8. HCW elicitation and observability

### A0 gloss

> We cannot directly see everything a person is holding in mind, but we can ask, observe, and measure; each method reveals a selective view, and asking may itself change the person’s state.

Let $H_t$ denote latent human context state, $a_t^{\mathrm{elicit}}$ an elicitation action, and $c_t$ a modality such as text, speech, gesture, behavioral choice, physiological sensing, or BCI. A response is generated through an elicitation/observation kernel

$$
R_t\sim E_{c_t}(\,\cdot\mid H_t,a_t^{\mathrm{elicit}}),
$$

while elicitation may also change the human:

$$
H_{t+1}\sim T_H(\,\cdot\mid H_t,a_t^{\mathrm{elicit}},R_t).
$$

This distinguishes passive readout from reactive measurement. A question may retrieve a prior belief, change salience, introduce framing, construct a new opinion, or prompt revision during articulation.

### Definition 2 — HCW observability envelope

For an elicitation-policy family $\mathcal Q$, modality family $\mathcal C$, and horizon $L$, define

$$
\eta\equiv_{\mathcal Q,\mathcal C,L}\eta'
$$

when every allowed adaptive elicitation policy produces the same response law from candidate human-context conditions $\eta$ and $\eta'$ through horizon $L$. As above, the same nonanticipating policy is initialized in each candidate condition, and observationally constructed continuation laws require declared regular-conditional versions. The resulting classes are the human-context distinctions observable under that protocol—not the complete HCW.

A BCI refines the envelope only when it distinguishes task-relevant states that the previous channel family could not. More measurements or bandwidth alone do not establish greater decision-relevant informativeness.

### Articulation as a lossy channel family

For a single noninteractive transfer, consider the Markov chain

$$
H_t
\longrightarrow I_t^{\mathrm{selected}}
\longrightarrow S_t^{\mathrm{encoded}}
\longrightarrow S_t^{\mathrm{transmitted}}
\longrightarrow \widehat I_t^{A}.
$$

Under the stated Markov assumption and without external side information, the data-processing inequality gives

$$
I(H_t;\widehat I_t^A)
\le
I(H_t;S_t^{\mathrm{transmitted}})
\le
I(H_t;S_t^{\mathrm{encoded}})
\le
I(H_t;I_t^{\mathrm{selected}}).
$$

This does not imply that every individual transfer loses information or that an IU existed fully formed inside the human. It states that downstream processing cannot increase mutual information about $H_t$ without side information. Interactive questioning can add side information and alter $H_t$, which must be modeled separately.

---

## 9. Replace catch-all uncertainty terms

“Subjective” and “non-deterministic” should not be used where a more specific mechanism is available.

| Broad phrase | More precise object | Observable consequence |
|---|---|---|
| Subjective viewpoint | Actor-relative information set $\mathcal F_t^i$ | Actors condition on different evidence |
| Subjective interpretation | Actor-specific decoding or observation kernel | Same signal produces different inferred IUs |
| Personal importance | Actor-specific salience or utility functional | Priority differs under constrained resources |
| Hidden inner state | Latent variable with a declared measurement model | Several latent states fit the same observation |
| Non-deterministic output | Aleatoric transition or emission kernel | Repeated controlled trials vary |
| Unknown state or parameter | Epistemic posterior uncertainty | Additional evidence can change the estimate |
| Partial observability | Non-injective observation channel | Distinct states remain observationally aliased |
| Channel noise | Stochastic corruption kernel | Repeated transmissions disagree |
| Representation loss | Many-to-one encoding or compression map | A distinction cannot be recovered without side information |
| Ambiguity | Multiple admissible semantic decoding maps | Several interpretations remain consistent |
| Drift over time | Nonstationary kernel or hidden state transition | The same nominal probe changes distribution over time |
| Asking changes the answer | Endogenous elicitation/intervention | Measurement changes later response laws |
| Different people respond differently | Actor- or dyad-conditioned parameters | Effects fail to transport without a population model |
| Model form is uncertain | Structural/model-class uncertainty | Different mechanisms induce similar observed laws |

This taxonomy does not deny stochasticity or lived perspective. It prevents those words from acting as undifferentiated explanations.

---

## 10. Compression as a proposed state-folding operation

Let the deterministic measurable map $C_B$ compress history $H$ into an artifact with budget $B$. Let $J_e$ reinject that artifact using declared downstream side information $e$. Require $J_e(C_B(h))$ to produce an admissible comparison history or initialization in the same scope, environment, clock, and remaining horizon as $h$. The side information must not secretly encode which source history produced the artifact.

### Predictive sufficiency

$C_B$ is predictively sufficient for the declared future family when, for every $\pi\in\Pi^\kappa$, there is a measurable probability kernel $R_\pi$ satisfying

$$
\mathbb P_h^\pi(\,\cdot\,)
=
R_\pi(C_B(h),\,\cdot\,)
\qquad
\text{for every }h\in\mathcal H^\kappa.
$$

Under a declared distribution over histories, the corresponding almost-sure statement is equivalent, subject to the regular-conditional assumptions above, to

$$
Z_{\mathrm{future}}^\pi
\perp\!\!\!\perp
H
\mid C_B(H)
\qquad
\text{for every }\pi\in\Pi^\kappa.
$$

For deterministic $C_B$, predictive sufficiency is also equivalent set-theoretically—and almost surely in the distribution-relative version—to recoverability of the predictive state from the artifact: there is a map $r$ such that

$$
S^\kappa(H)=r(C_B(H)).
$$

### Operational preservation after reinjection

Even an informationally sufficient artifact may be ignored or misread downstream. Define operational distortion

$$
\Delta_\kappa(h;C_B,J_e)
=
d_\kappa\bigl(h,J_e(C_B(h))\bigr).
$$

This separates two failure sources:

1. the artifact omitted a predictive distinction;
2. the continuing system received the distinction but failed to use it.

### Proposition 4 — Irreversible predictive merge

**Claim.** Suppose deterministic compression maps $h$ and $h'$ to the same artifact while $h\not\sim_\kappa h'$. No common continuation procedure that receives only that artifact and source-independent side information can exactly preserve both original predictive classes.

**Proof sketch.** Because $h\not\sim_\kappa h'$, choose a policy $\pi^*$ witnessing $\mathbb P_h^{\pi^*}\neq\mathbb P_{h'}^{\pi^*}$. Identical artifacts, the same decoder, and source-independent side information induce the same reconstructed law under $\pi^*$ for both histories. That single law cannot equal both distinct original laws. $\square$

This is a precise candidate signature of [Overcompression](../glossary.md#overcompression): a compression operator merged distinctions that matter to at least one declared future.

### Proposition 5 — Compositional distortion bound

For sequential context transformations producing admissible comparison conditions $x_0,x_1,\ldots,x_n\in\mathcal H^\kappa$ under the same policy family, outcome space, clock, and remaining horizon,

$$
d_\kappa(x_0,x_n)
\le
\sum_{j=1}^{n}d_\kappa(x_{j-1},x_j).
$$

This follows pointwise from the triangle inequality. For stochastic transformations, expectations may be taken only after the pointwise conditions and measurability assumptions hold. The bound is not a claim that actual loss grows monotonically or that later transformations cannot repair earlier damage using side information.

### Task-constrained rate–distortion question

Once a distribution over histories and a valid distortion are declared, compression can be posed as

$$
\min_{C_B}\;\mathbb E[\ell(C_B(H))]
\qquad
\text{subject to}\qquad
\mathbb E[\Delta_\kappa(H;C_B,J_e)]\le\epsilon,
$$

where $\ell$ is code length, token cost, latency, or another declared resource. This is a research program, not a claim that the needed distributions or optimal compressor are already known.

---

## 11. Repair as control rather than guaranteed reset

Let $\mathcal U_R\subseteq\mathcal U$ contain the five canonical repair operations: re-grounding, decompression, re-weighting, disambiguation, and synchronization. In this model they are controlled interventions. Their effects remain stochastic and context-dependent.

For the state-based control expressions below, assume the measurable quotient transition kernel in Proposition 2a exists—whether by strong lumpability, probabilistic bisimulation, or the stronger common-version point update—and that admissible repair policies are measurable. A pointwise successor map is not required. Without that kernel, repair can still be compared through history-indexed continuation laws, but $S_t^\kappa$ must not be treated as a controlled Markov state.

Choose a measurable target set $\mathcal G\subseteq\mathcal S^\kappa$ representing an acceptable predictive coordination region. For repair policy $\rho$, define the hitting time

$$
\tau_{\mathcal G}=\inf\{t\ge0:S_t^\kappa\in\mathcal G\},
$$

and, if a nonnegative measurable cost function $c$ is justified, expected repair cost

$$
V_\rho(s)
=
\mathbb E_s^\rho
\left[
\sum_{t=0}^{\tau_{\mathcal G}-1}c(S_t^\kappa,U_t)
\right].
$$

A repair can also be tested by whether the post-repair state lies within a declared predictive radius of a synchronized reference under held-out probes.

Nothing in the present axioms implies that repair cost is non-decreasing in discovery lag. Later information can reveal an easy correction, a disagreement can self-resolve, or side information can restore a distinction. A monotonic repair-lag theorem would require additional assumptions such as irreversible loss or monotone accumulation and should not be inferred from this note.

---

## 12. What mathematics can establish before experiments

Conditional on the declared spaces, policies, kernels, and observables, mathematics can establish:

1. exact predictive equivalence is an equivalence relation;
2. its quotient is the coarsest sufficient predictive state for the declared future family;
3. approximate pairwise closeness is not generally an equivalence relation;
4. total-variation distance bounds changes in bounded future outcomes;
5. a deterministic compressor that merges distinct predictive classes cannot preserve both without side information;
6. sequential transformation error obeys a triangle-inequality budget;
7. observationally equivalent latent models cannot be distinguished by any estimator restricted to the allowed observations;
8. under continuation closure or a compatible bisimulation condition, a finite predictive quotient yields a valid candidate for Jess-style finite-state folding; a bounded-horizon quotient alone does not.

These are conditional mathematical results, not toy arithmetic. They expose exactly which assumptions carry each conclusion.

### What mathematics cannot establish alone

Mathematics alone cannot establish:

- that the selected outcomes operationalize meaning, salience, intent, or continuity;
- that the predictive quotient is nontrivial, finite, estimable, or useful in real interactions;
- that the topology variables improve prediction beyond transcripts and actor-level context;
- the actual human, model, retrieval, routing, or channel kernels;
- whether an elicitation method distinguishes relevant HCW conditions;
- whether BCI decoding tracks coordination-relevant meaning;
- whether the canonical failure modes are reliably discriminable;
- whether a proposed repair improves coordination;
- whether an MCW-guided compressor outperforms matched alternatives;
- whether this formal projection captures something not already handled by common ground, distributed cognition, predictive-state, or stochastic-control theories.

The fact that measurement can alter the measured interaction does not eliminate empirical contact. It means the measurement or elicitation policy belongs in $U_t$ and its state-changing effect belongs in $P_t$.

---

## 13. Bridge to non-destructive state reconstruction

Smith et al.’s non-destructive finite-state-machine reconstruction supplies the motivating algorithmic pattern: apply controlled inputs, observe outputs, expand future behavior, and fold indistinguishable subtrees.

For MCW-PSS:

1. histories are nodes in an intervention–observation tree;
2. ordinary exchanges, elicitation, channel changes, and repair operations form the intervention family;
3. task-grounded coordination consequences form the observations;
4. $\sim_\kappa$ determines exact folds;
5. $d_\kappa$ supports bounded approximations with explicit error;
6. trusted-versus-candidate quotient graphs expose altered transitions, reachable states, compression failures, or repair behavior.

Internal model features—activations, attention, retrieval traces, MoE routing, memory access—may improve exploration or explain a split. They do not define predictive equivalence unless the declared coordination outcome itself includes those measurements.

---

## 14. Losable claims and retirement conditions

The formal definitions are stipulations; their usefulness is losable. This line of work should be narrowed or abandoned if:

1. **Actor-only sufficiency:** transcript and actor-level variables predict every declared future as well as the distributed topology. Then the non-actor topology adds no operational MCW value.
2. **No emergent residue:** yoked outsiders with the same transcript and task materials predict and resolve the interaction as well as insiders. Then transcript plus individual models may suffice.
3. **Trivial quotient:** all histories collapse into one class or nearly every history remains unique under plausible scopes. Then the representation offers no useful compression.
4. **No estimable abstraction:** every finite or bounded-complexity approximation violates held-out predictive error limits.
5. **No compression benefit:** MCW-derived state-transfer artifacts do not preserve held-out futures better than matched ordinary summaries or extractive baselines.
6. **No repair specificity:** failure-matched repairs do not outperform generic clarification, additional time, or additional context.
7. **Redundancy:** established common-ground, distributed-cognition, predictive-state, or decentralized-control models explain the same observables with equal or better parsimony.

These are empirical retirement conditions for the research program, not logical falsifications of an equivalence relation.

---

## 15. Open decisions before promotion

1. Should MCW-PSS remain a model **of evidence about MCW**, become a declared extension, or motivate a future canonical amendment?
2. Should the context topology live inside a broadened ACW, outside MCW as an adjacent substrate, or become part of MCW’s canonical ontology?
3. Which coordination outcomes and probe families are legitimate for the first scoped instance?
4. Should exact equivalence be history-based, latent-state-based, or both with an explicit realization theorem?
5. Which probability-law metric is appropriate for mixed text, action, ranking, and repair outcomes?
6. Which assumptions would justify a finite-state approximation?
7. How should reactive elicitation record whether an IU was retrieved, constructed, reframed, or revised?
8. Which frozen statements concerning HCW/ACW “enumerability” and universal transfer loss require separate amendment proposals?

---

## Mathematical ancestry and methodological references

This proposal inherits substantial machinery and should claim only the MCW-specific operationalization and synthesis:

- Åström, K. J. (1965). “Optimal Control of Markov Processes with Incomplete State Information I.” *Journal of Mathematical Analysis and Applications*, 10, 174–205. https://doi.org/10.1016/0022-247X(65)90154-X
- Blackwell, D. (1953). “Equivalent Comparisons of Experiments.” *The Annals of Mathematical Statistics*, 24(2), 265–272. https://doi.org/10.1214/aoms/1177729032
- Ferns, N., Panangaden, P., & Precup, D. (2004). “Metrics for Finite Markov Decision Processes.” *Proceedings of UAI 2004*. https://arxiv.org/abs/1207.4114
- Littman, M. L., Sutton, R. S., & Singh, S. (2001). “Predictive Representations of State.” *Advances in Neural Information Processing Systems 14*. https://papers.nips.cc/paper_files/paper/2001/hash/1e4d36177d71bbb3558e43af9577d70e-Abstract.html
- Nayyar, A., Mahajan, A., & Teneketzis, D. (2013). “Decentralized Stochastic Control with Partial History Sharing: A Common Information Approach.” *IEEE Transactions on Automatic Control*, 58(7), 1644–1658. https://doi.org/10.1109/TAC.2013.2239000
- Shalizi, C. R., & Crutchfield, J. P. (2001). “Computational Mechanics: Pattern and Prediction, Structure and Simplicity.” *Journal of Statistical Physics*, 104, 817–879. https://doi.org/10.1023/A:1010388907793
- Smith, J., Oler, K., Miller, C., & Manz, D. (2017). “Reverse Engineering Integrated Circuits Using Finite State Machine Analysis.” *Proceedings of HICSS-50*. https://aisel.aisnet.org/hicss-50/eg/supply_chain_security/4/
- Tishby, N., Pereira, F. C., & Bialek, W. (1999). “The Information Bottleneck Method.” *Proceedings of the 37th Annual Allerton Conference on Communication, Control, and Computing*, 368–377. https://arxiv.org/abs/physics/0004057

Related traditions still requiring a dedicated comparison include probabilistic bisimulation, controlled Nerode equivalence, partially observable stochastic games, dynamic epistemic logic, active system identification, causal abstraction, psychometrics, measurement invariance, and reactive measurement.

---

## Working-note summary

The central proposal is:

> Treat evidence about MCW as a task-relative predictive state of a typed, partially observed context topology. Fold histories only under exact future-law equivalence; approximate them only with explicit error bounds. Treat elicitation, compression, and repair as interventions whose effects are included in the process rather than dismissed as “subjective” or “non-deterministic.”

This construction is mathematically coherent under its stated assumptions. Whether it is empirically useful, distinct from prior frameworks, finite enough to estimate, or faithful to lived human–AI coordination remains open.
