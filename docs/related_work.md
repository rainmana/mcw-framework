# Related Work & Positioning

**Status:** Positioning with citations · Evidence: L0 — this page makes no empirical claims of its own; every empirical statement it references carries its source. All citations below were verified against primary sources (publisher pages, ACL Anthology, arXiv, Crossref) before inclusion.

This page situates the Meta-Context Window (MCW) framework relative to the research traditions that own its concepts. An earlier version of this page named five fields and cited nothing — which handed any hostile reviewer the cheapest possible attack: *"MCW is common ground plus conversational repair, renamed."* This version takes that attack seriously. It maps each MCW construct to its specific ancestor, states where the debt is total, states the one place the framework bets on something its ancestors do not predict, and specifies what evidence would make MCW redundant.

---

## Conversational repair (conversation analysis)

The repair vocabulary is not MCW's invention. Conversation analysis owns it: Schegloff, Jefferson & Sacks (1977) established the organization of repair in conversation — self- versus other-initiation, position, and the preference for self-correction; Schegloff (1992) analyzed third-position repair as "the last structurally provided defense of intersubjectivity"; Schegloff (1987) provided the closest existing precedent for a *taxonomy of sources of misunderstanding*; and Dingemanse et al. (2015) showed other-initiated repair to be a cross-linguistic universal, deployed on the order of once per 1.4 minutes of conversation.

**Relation:** MCW's five [repair operations](glossary.md#repair-operations) are engineered, coordination-scoped analogues of practices this literature describes descriptively. The debt is explicit and near-total for the *existence* of repair machinery. What MCW adds is not the observation that repair exists, but (a) a fixed, minimal operation set intended for cross-study comparison, and (b) treating repair *availability* as a manipulable variable with predicted coordination consequences ([Repair Suppression](glossary.md#repair-suppression), [Experiment 5](experiments/preregistration/exp5_repair_suppression.md)) and repair *timing* as a cost variable (the rubrics' [late-discovery model](experiments/hrdm_rubrics.md)).

## Grounding and common ground

This is the tradition most likely to make MCW redundant, and it gets the longest entry. Clark & Schaefer (1989) modeled discourse as contributions ratified through presentation and acceptance; Clark & Brennan (1991) defined grounding — the collaborative process by which parties establish the mutual belief that they have understood each other, at costs that vary by medium; Clark (1996) built the book-length theory of language use as joint action on accumulating common ground.

**Relation:** MCW's "shared coordination state" is, to a first approximation, common ground *plus* the grounding process *plus* salience and timing. The framework's canonical distinction — common ground is a property of shared beliefs, MCW a property of shared coordination state including salience, timing, and repair capacity — is a real but modest refinement, not a new theory. The honest statement is: **if an interaction involves two cognitively similar parties with symmetric memory and continuous availability, MCW reduces to grounding theory and should not be preferred to it.**

The framework's one genuinely novel bet lies where that symmetry breaks: the [HCW](glossary.md#human-context-window-hcw) advances continuously and non-enumerably; the [ACW](glossary.md#artificial-context-window-acw) is discrete and input-driven. Grounding theory was built on parties for whom this asymmetry does not arise, and it makes no predictions about it. MCW predicts coordination failures *specific to the asymmetry* — [Asymmetric State Advancement](glossary.md#asymmetric-state-advancement) — testable only in Human↔AI conditions ([Experiment 2](experiments/preregistration/exp2_asymmetric_advancement.md)). That is the wedge; everything else is inheritance.

## Joint activity and human–automation teamwork

The closest prior art for *applying* common ground to human–machine coordination already exists: Klein, Feltovich, Bradshaw & Woods (2005) analyzed common ground and coordination in joint activity, including a model of common-ground breakdown; Klein, Woods, Bradshaw, Hoffman & Feltovich (2004) posed the "ten challenges for making automation a team player," several of which (signaling status, being directable, making intentions legible) are recognizable ancestors of MCW's repair-permission and constraint-disclosure concerns. Cohen & Levesque (1991) formalized teamwork through joint intentions.

**Relation:** MCW must not pretend this work does not exist; it is the nearest neighbor. What MCW adds over Klein et al. is narrower and sharper: a *frozen, minimal* vocabulary under explicit [governance](constitution.md) (six failure modes, five repair operations, four proxies — fixed for cross-study comparison), an ordinal measurement program with [anchored rubrics](experiments/hrdm_rubrics.md) and [pre-registered falsification conditions](experiments/preregistration/index.md), and the LLM-specific context-window asymmetry, which 2000s-era automation work did not model.

## Breakdowns and situated action

Winograd & Flores (1986) made *breakdown* a first-class design concept — the moment equipment or coordination stops being transparent — and argued computers are best understood through the conversations they mediate. Suchman (1987) showed that plans are resources for situated action rather than determinants of it, and that human–machine communication fails where the machine cannot access the situated context of use.

**Relation:** MCW's failure modes are breakdown types in exactly Winograd & Flores' sense, restricted to the coordination layer. Suchman's argument is a standing caution for this framework: the HCW is situated in ways no enumeration captures — which is why the framework declares the HCW "not enumerable" and why the IU individuation problem remains flagged as open rather than solved.

## CSCW and articulation work

Schmidt & Bannon (1992) established articulation work — the ongoing, mostly invisible effort of coordinating cooperative work — as CSCW's core object; Schmidt & Simone (1996) developed coordination mechanisms as artifacts that reduce its cost.

**Relation:** MCW repair operations are articulation work, named at a finer grain and scoped to dyadic human–AI exchange. Where CSCW predicts that better coordination artifacts reduce coordination cost, MCW predicts a residue: failures that persist *with well-designed artifacts* because the relevant IUs were never externalized or were suppressed — a design goal of the framework, stated here as a claim to be earned, not a finding `[L0]` ([Experiment 4](experiments/preregistration/exp4_constraint_opacity.md) is the closest designed test: same interface, same constraint, only disclosure varies).

## Situation awareness and distributed cognition

Endsley (1995) formalized situation awareness — perception, comprehension, projection — including team SA; Hutchins (1995) relocated cognition into socio-technical systems, with coordination states carried by artifacts and representations rather than by any single head.

**Relation:** Hutchins is the license for MCW's central ontological move (a coordination state that is in neither party). The difference from SA: situation awareness concerns a party's model of the *task environment*; MCW's failure modes concern the parties' models of *each other's* meaning, salience, and constraints — [False Alignment](glossary.md#false-alignment) is two parties wrong about each other, not about the world.

## Information theory

Shannon (1948) supplies the vocabulary of entropy, channel, and noise. The framework borrows the *intuitions* — information loss under constrained transmission, uncertainty accumulating without correction — and currently no more than that: no random variable over the coordination state has been defined, so "MCW entropy" remains informal usage, marked as such wherever it appears (see [Entropy](glossary.md#entropy)). Defining a computable estimator (or deleting the term) is tracked as open work; until then the framework's actual quantification attempt is the H/R/D/M program, not entropy.

## LLM-era evidence (2023–2026)

The framework's premises now have a contemporary literature, and it cuts both ways:

- **LLMs under-ground.** Shaikh et al. (2024) found LLM generations exhibit large "grounding gaps" — following up, acknowledging, and clarifying far less than humans; Mohapatra, Kapadnis, Romary & Cassell (2024) benchmarked LLMs' conversational grounding and found current models weak at it; Benotti & Blackburn (2021) had already framed grounding as a collaborative process language technology mostly lacks; Lachenmaier, Sieker & Zarrieß (2025) probed grounding under loaded questions. This literature supports the framework's premise that the repair/grounding layer is where human–LLM coordination is thin — while also showing the phenomena are being measured without MCW vocabulary, which is pressure the framework must answer with differential predictions, not enthusiasm.
- **Clarification behavior is measurable and trainable.** CLAMBER (Zhang, Qin, Deng et al., 2024) benchmarks identifying and clarifying ambiguous questions; Zhang & Choi (2025) and Zhang, Knox & Choi (2025) study when models should ask rather than guess. These are existence proofs that [Repair Suppression](glossary.md#repair-suppression)-adjacent quantities (clarification rates) are codable at scale — the same quantities the [pre-registrations](experiments/preregistration/index.md) use as suppression markers.
- **Repair with conversational systems.** Alghamdi, Halvey & Nicol (2024) catalogued system and user strategies for repairing conversational breakdowns; Kim et al. (2024) taxonomized user dissatisfaction with ChatGPT, including failures users attribute to the model that trace to under-specified exchange — the phenomenon MCW's [M proxy](glossary.md#misattribution-m) names; Zamfirescu-Pereira, Wong, Hartmann & Yang (2023) showed non-experts systematically fail at prompt design in ways consistent with treating an initialization artifact as a coordination solution.
- **Human–AI teaming and mutual models.** Andrews et al. (2023) reviewed shared mental models in human–AI teams; Wang et al. (2024) and Zhang et al. (2024, preprint) study (mutual) theory of mind in human–AI collaboration; Duan et al. (2025) reviewed trust in autonomous teammates; Tankelevitch et al. (2024) analyzed the metacognitive demands of generative AI — the human-side burden MCW locates in the HCW; Gmeiner et al. (2023) documented co-creation breakdowns between designers and generative tools.
- **Context-window size is not coordination.** Liu et al. (2024) showed models use long contexts non-uniformly ("lost in the middle") — direct support for the framework's founding observation that ACW capacity and coordination quality are different variables.
- **Multi-agent coordination failures.** Cemri et al. (2025) built MAST, an empirically grounded taxonomy of 14 multi-agent LLM failure modes (specification, inter-agent misalignment, task verification) with strong inter-annotator agreement — a methodological standard (reliability-first taxonomy building) that MCW's own taxonomy has not yet met and should be measured against.

## Alignment, safety, and prompt engineering

Unchanged in substance from the prior version of this page: MCW does not compete with alignment or safety work; it addresses the layer where well-aligned, capable models still fail collaboratively — through hidden variables ([Constraint Opacity](glossary.md#constraint-opacity)), suppressed repair ([Repair Suppression](glossary.md#repair-suppression)), or silent divergence ([Drift](glossary.md#drift-silent-desynchronization)). System prompts are treated as [initialization artifacts](glossary.md#system-prompt-mcw-context), with the derivation and its registered A/B predictions in the [system prompt derivation](system_prompt_derivation.md).

---

## Differential predictions

"Complementary, not a replacement" is unfalsifiable as a slogan. This table states, per neighboring tradition, one observable where MCW's account diverges — each tied to a registered design:

| Tradition | Their account predicts | MCW predicts instead | Where it's testable |
|---|---|---|---|
| Grounding theory (Clark & Brennan) | Grounding costs are set by medium and task; no party-asymmetry term | Coordination failures specific to the continuous-HCW / discrete-ACW asymmetry: hidden off-turn advancement degrades coordination in Human↔AI dyads in ways matched Human↔Human dyads (where both parties advance off-turn and expect it) do not show | [Exp 2](experiments/preregistration/exp2_asymmetric_advancement.md), with a Human↔Human contrast as the natural follow-up |
| Conversation analysis | Repair machinery is universally available and self-organizing | Repair availability is a *manipulable variable*: suppressing it (net of time pressure) measurably worsens downstream coordination; and repair *cost* is ordered by discovery lag | [Exp 5](experiments/preregistration/exp5_repair_suppression.md); the rubrics' late-discovery model |
| CSCW / articulation work | Better coordination artifacts reduce coordination failures | A residue of failures survives artifact quality when constraint disclosure or IU externalization is withheld — same interface, different coordination outcomes | [Exp 4](experiments/preregistration/exp4_constraint_opacity.md) |
| Situation awareness | Coordination failure tracks degraded awareness of the task environment | [False Alignment](glossary.md#false-alignment): both parties can hold accurate task-environment models and still fail, because their models of *each other's meaning* diverge | [Exp 1](experiments/preregistration/exp1_false_alignment.md) |
| Prompt engineering | Better initialization reduces failure; sufficiently good prompts could eliminate repair | Initialization effects are bounded: re-grounding remains necessary in long interactions under *any* static prompt (a prompt that eliminated repair would falsify the framework's Property 1) | [Prompt predictions](experiments/preregistration/prompt_predictions.md), P5 |

## What would make MCW redundant

Stated as commitments, not rhetoric. MCW should be abandoned in favor of its ancestors if:

1. **The asymmetry bet fails.** If Human↔AI and matched Human↔Human conditions show the same coordination signatures across the registered experiments — no effect specific to the HCW/ACW asymmetry — then grounding theory plus conversational repair covers the phenomena, and the MCW vocabulary is a renaming. This is the framework's load-bearing wager.
2. **The taxonomy reduces without residue.** If the six failure modes map cleanly onto existing categories (Clark & Brennan's grounding costs; Klein et al.'s common-ground breakdown model; MAST's categories for the multi-agent case) with nothing left over *and* no better discriminant criteria, the taxonomy should be retired in favor of the source vocabularies.
3. **Existing instruments do the job.** If grounding-acts coding (Shaikh et al. 2024; Mohapatra et al. 2024) or MAST-style annotation classifies these phenomena with reliability and coverage the H/R/D/M program cannot match, the measurement program should adopt those instruments rather than compete with them.

## Methodological references

The measurement pages ([rubrics](experiments/hrdm_rubrics.md), [pre-registrations](experiments/preregistration/index.md)) rely on standard instruments: weighted kappa (Cohen, 1968), agreement benchmarks (Landis & Koch, 1977), Krippendorff's alpha (Krippendorff, 2018), and equivalence testing by TOST (Lakens, 2017).

---

## References

- Alghamdi, E., Halvey, M., & Nicol, E. (2024). System and User Strategies to Repair Conversational Breakdowns of Spoken Dialogue Systems. *Proceedings of the 6th ACM Conference on Conversational User Interfaces (CUI '24)*. https://dl.acm.org/doi/10.1145/3640794.3665558
- Andrews, R. W., Lilly, J. M., Srivastava, D., & Feigh, K. M. (2023). The role of shared mental models in human-AI teams: a theoretical review. *Theoretical Issues in Ergonomics Science*, 24(2), 129–175. https://doi.org/10.1080/1463922X.2022.2061080
- Benotti, L., & Blackburn, P. (2021). Grounding as a Collaborative Process. *Proceedings of EACL 2021*. https://aclanthology.org/2021.eacl-main.41/
- Cemri, M., et al. (2025). Why Do Multi-Agent LLM Systems Fail? *NeurIPS 2025 Datasets and Benchmarks Track*; arXiv:2503.13657. https://arxiv.org/abs/2503.13657
- Clark, H. H. (1996). *Using Language*. Cambridge University Press.
- Clark, H. H., & Brennan, S. E. (1991). Grounding in communication. In L. B. Resnick, J. M. Levine, & S. D. Teasley (Eds.), *Perspectives on Socially Shared Cognition* (pp. 127–149). APA. https://doi.org/10.1037/10096-006
- Clark, H. H., & Schaefer, E. F. (1989). Contributing to discourse. *Cognitive Science*, 13(2), 259–294.
- Cohen, J. (1968). Weighted kappa: Nominal scale agreement provision for scaled disagreement or partial credit. *Psychological Bulletin*, 70(4), 213–220.
- Cohen, P. R., & Levesque, H. J. (1991). Teamwork. *Noûs*, 25(4), 487–512.
- Dingemanse, M., Roberts, S. G., Baranova, J., Blythe, J., Drew, P., Floyd, S., Gisladottir, R. S., Kendrick, K. H., Levinson, S. C., Manrique, E., Rossi, G., & Enfield, N. J. (2015). Universal Principles in the Repair of Communication Problems. *PLOS ONE*, 10(9), e0136100. https://doi.org/10.1371/journal.pone.0136100
- Duan, W., Flathmann, C., McNeese, N. J., et al. (2025). Trusting Autonomous Teammates in Human-AI Teams: A Literature Review. *Proceedings of CHI 2025*. https://dl.acm.org/doi/10.1145/3706598.3713527
- Endsley, M. R. (1995). Toward a Theory of Situation Awareness in Dynamic Systems. *Human Factors*, 37(1), 32–64.
- Gmeiner, F., Yang, H., Yao, L., Holstein, K., & Martelaro, N. (2023). Exploring Challenges and Opportunities to Support Designers in Learning to Co-create with AI-based Manufacturing Design Tools. *Proceedings of CHI 2023*. https://dl.acm.org/doi/10.1145/3544548.3580999
- Hutchins, E. (1995). *Cognition in the Wild*. MIT Press.
- Kim, Y., Lee, J., Kim, S., Park, J., & Kim, J. (2024). Understanding Users' Dissatisfaction with ChatGPT Responses: Types, Resolving Tactics, and the Effect of Knowledge Level. *Proceedings of IUI 2024*. https://dl.acm.org/doi/10.1145/3640543.3645148
- Klein, G., Feltovich, P. J., Bradshaw, J. M., & Woods, D. D. (2005). Common Ground and Coordination in Joint Activity. In W. B. Rouse & K. R. Boff (Eds.), *Organizational Simulation* (pp. 139–184). Wiley.
- Klein, G., Woods, D. D., Bradshaw, J. M., Hoffman, R. R., & Feltovich, P. J. (2004). Ten Challenges for Making Automation a "Team Player" in Joint Human-Agent Activity. *IEEE Intelligent Systems*, 19(6), 91–95.
- Krippendorff, K. (2018). *Content Analysis: An Introduction to Its Methodology* (4th ed.). SAGE.
- Lachenmaier, C., Sieker, J., & Zarrieß, S. (2025). Can LLMs Ground when they (Don't) Know: A Study on Direct and Loaded Political Questions. *Proceedings of ACL 2025*. https://aclanthology.org/2025.acl-long.728/
- Lakens, D. (2017). Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses. *Social Psychological and Personality Science*, 8(4), 355–362.
- Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159–174.
- Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F., & Liang, P. (2024). Lost in the Middle: How Language Models Use Long Contexts. *Transactions of the Association for Computational Linguistics*, 12, 157–173. https://aclanthology.org/2024.tacl-1.9/
- Mohapatra, B., Hassan, S., Romary, L., & Cassell, J. (2024). Conversational Grounding: Annotation and Analysis of Grounding Acts and Grounding Units. *Proceedings of LREC-COLING 2024*. https://aclanthology.org/2024.lrec-main.352/
- Mohapatra, B., Kapadnis, M. N., Romary, L., & Cassell, J. (2024). Evaluating the Effectiveness of Large Language Models in Establishing Conversational Grounding. *Proceedings of EMNLP 2024*. https://aclanthology.org/2024.emnlp-main.545/
- Schegloff, E. A. (1987). Some Sources of Misunderstanding in Talk-in-Interaction. *Linguistics*, 25(1), 201–218.
- Schegloff, E. A. (1992). Repair After Next Turn: The Last Structurally Provided Defense of Intersubjectivity in Conversation. *American Journal of Sociology*, 97(5), 1295–1345.
- Schegloff, E. A. (2000). When 'Others' Initiate Repair. *Applied Linguistics*, 21(2), 205–243.
- Schegloff, E. A., Jefferson, G., & Sacks, H. (1977). The Preference for Self-Correction in the Organization of Repair in Conversation. *Language*, 53(2), 361–382. https://doi.org/10.2307/413107
- Schmidt, K., & Bannon, L. (1992). Taking CSCW seriously: Supporting articulation work. *Computer Supported Cooperative Work (CSCW)*, 1(1–2), 7–40.
- Schmidt, K., & Simone, C. (1996). Coordination mechanisms: Towards a conceptual foundation of CSCW systems design. *Computer Supported Cooperative Work (CSCW)*, 5(2–3), 155–200.
- Shaikh, O., Gligorić, K., Khetan, A., Gerstgrasser, M., Yang, D., & Jurafsky, D. (2024). Grounding Gaps in Language Model Generations. *Proceedings of NAACL 2024*. https://aclanthology.org/2024.naacl-long.348/
- Shannon, C. E. (1948). A Mathematical Theory of Communication. *Bell System Technical Journal*, 27(3), 379–423.
- Suchman, L. A. (1987). *Plans and Situated Actions: The Problem of Human-Machine Communication*. Cambridge University Press.
- Tankelevitch, L., Kewenig, V., Simkute, A., Scott, A. E., Sarkar, A., Sellen, A., & Rintel, S. (2024). The Metacognitive Demands and Opportunities of Generative AI. *Proceedings of CHI 2024*. https://dl.acm.org/doi/10.1145/3613904.3642902
- Wang, Q., Walsh, S., Si, M., Kephart, J., et al. (2024). Theory of Mind in Human-AI Interaction. *Extended Abstracts of CHI 2024*. https://dl.acm.org/doi/10.1145/3613905.3636308
- Winograd, T., & Flores, F. (1986). *Understanding Computers and Cognition: A New Foundation for Design*. Ablex.
- Zamfirescu-Pereira, J. D., Wong, R. Y., Hartmann, B., & Yang, Q. (2023). Why Johnny Can't Prompt: How Non-AI Experts Try (and Fail) to Design LLM Prompts. *Proceedings of CHI 2023*. https://dl.acm.org/doi/10.1145/3544548.3581388
- Zhang, M. J. Q., & Choi, E. (2025). Clarify When Necessary: Resolving Ambiguity Through Interaction with LMs. *Findings of NAACL 2025*. https://aclanthology.org/2025.findings-naacl.306/
- Zhang, M. J. Q., Knox, W. B., & Choi, E. (2025). Modeling Future Conversation Turns to Teach LLMs to Ask Clarifying Questions. *Proceedings of ICLR 2025*.
- Zhang, S., Wang, X., Zhang, W., et al. (2024). Mutual Theory of Mind in Human-AI Collaboration. arXiv:2409.08811 (preprint; not yet peer-reviewed). https://arxiv.org/abs/2409.08811
- Zhang, T., Qin, P., Deng, Y., Huang, C., et al. (2024). CLAMBER: A Benchmark of Identifying and Clarifying Ambiguous Information Needs. *Proceedings of ACL 2024*. https://aclanthology.org/2024.acl-long.578/

---

## Positioning summary

MCW should be understood as:

- a coordination lens, not a cognitive theory
- inheriting most of its machinery — and saying from whom
- betting on exactly one novel prediction class: effects of the HCW-continuous / ACW-discrete asymmetry, testable only in Human↔AI conditions
- falsifiable through the [pre-registered experiments](experiments/preregistration/index.md), with the redundancy conditions above as standing exit criteria
