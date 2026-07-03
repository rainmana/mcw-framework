# Working Note — IU Individuation

**Status:** Working note · Evidence: L0 — analysis of an open theoretical problem, not a fix. Nothing here is canon or a declared extension yet; if one of the candidate criteria below is adopted, that adoption will be filed as an Article V extension with its own falsification condition. Until then, claims that presuppose IU countability should be read with this note's caveats attached.

---

## The problem, stated plainly

The [Information Unit](../glossary.md#information-unit-iu) is the framework's atomic construct, and the framework cannot currently count them. There is no criterion for deciding whether an utterance is one IU or three, so every dependent construct that presupposes countability is hollow to that extent: [Overcompression](../glossary.md#overcompression) ("critical IU distinctions are lost" — how many?), [Decompression](../glossary.md#decompression) ("component IUs"), IU-flow "cumulative fidelity" (fidelity of *what units*?), and the paper outline's "IU entropy accumulation."

Worse, the definitions are mutually circular: an IU is "the minimal transferable element that can influence coordination state," and the coordination state (MCW) is what arises from exchanging IUs. Each is defined through the other; a reviewer can dissolve both with one question. This note proposes candidate individuation criteria, works one example, plans the reliability test, breaks the circularity with an independent existence criterion for the MCW, and lists what remains unresolved.

---

## Candidate individuation criteria

### C1 — Decision relevance (counterfactual removal)

> An IU is a minimal span of an utterance whose removal would change the receiving party's next task-relevant action.

- **Independence from MCW:** the criterion references *behavior* (the receiver's next action), not the coordination state — this is what breaks the definitional circle on the IU side.
- **Strengths:** coordination-scoped by construction; matches the glossary's examples (an assumption, a constraint, a correction — each changes what the receiver does next).
- **Weaknesses:** counterfactual evaluation is expensive (someone must judge "would the action have differed?"); minimal spans are not unique (two overlapping spans can each satisfy the test); "task-relevant action" needs a task with visible actions — the criterion is weakest exactly where coordination is most tacit.

### C2 — Ratification units (grounding-based)

> An IU is what the parties ground as a unit: the span presented and accepted as one contribution, in the sense of Clark & Schaefer's (1989) contribution model.

- **Strengths:** inherits a worked-out theory with decades of use; the acceptance phase gives an observable boundary signal (acknowledgment, continuation, clarification directed at the span).
- **Weaknesses:** imports the grounding machinery wholesale — awkward for a framework whose [one novel bet](../related_work.md) is where grounding theory underdetermines; and ratification units are hard to segment in human–LLM interaction because LLMs produce far *fewer* explicit grounding acts than humans (the grounding-gap finding of Shaikh et al. 2024, cited in the related-work page) — acceptance boundaries are under-marked, so C2's observable boundary signal is sparse exactly where this framework needs it. (An earlier version of this note claimed the opposite — that LLMs "over-acknowledge" — which misused the citation; corrected. Generic agreeable openers are not grounding acts, and were never what Shaikh et al. measured.)

### C3 — Propositional idea-unit coding

> An IU is a predicate–argument proposition, segmented per propositional idea-unit coding practice in discourse analysis.

- **Strengths:** the most mechanical of the three; closest to being automatable; segmentation traditions and reliability practices exist (unitizing reliability per Krippendorff, 2018).
- **Weaknesses:** propositions are *semantic* units, not *coordination* units — "the deadline is Friday" and "I'm anxious about the deadline" are one proposition each, but their coordination weight differs enormously; the criterion counts meaning, not influence, and so drifts from the IU's definitional point.

**Working preference (not a decision):** C1 as the definition-bearing criterion with C3 as the practical segmentation pass — segment propositionally, then merge/split by the decision-relevance test. That hybrid is what the worked example below uses. Adopting it for real is an Article V extension not yet filed.

---

## Worked example

Constructed transcript fragment (representative of the planning tasks in the [pre-registrations](../experiments/preregistration/index.md); a real pilot transcript should replace it when one exists):

> **H1:** Let's plan the workshop for the week of the 14th — Thursday if we can, since Priya is out Monday through Wednesday. Budget's capped at $2k, and that's firm.
> **A1:** Understood. Thursday the 17th, budget ceiling $2,000. Do you want catering inside that cap?
> **H2:** Yes — inside. And keep the afternoon free for the breakout.

**C3 pass (propositional):** H1 = {p1: workshop in week of the 14th; p2: prefer Thursday; p3: Priya out Mon–Wed; p4: budget capped at $2k; p5: the cap is firm} → 5 units. H2 = {p6: catering inside cap; p7: afternoon free for breakout} → 2 units. Total: 7.

**C1 merge/split pass (decision relevance):** p2 and p3 merge — p3's only decision consequence *in this task* is p2 (Thursday); removing p3 alone changes no downstream action if p2 stays. p4 and p5 stay distinct — removing p5 ("firm") licenses the receiver to propose small overruns, a different action space. Result: 6 IUs, and the analysis *shows its work* on the two contested merges.

**Where the criteria disagree, the disagreement is the data:** C3 counts 7, C1 counts 6, and C2 would count 3 (H1, A1's ratification, H2 each ground as single contributions in this fragment). A framework that says "critical IU distinctions are lost" owes its readers which of these counts it means. Until a criterion is adopted, Overcompression claims should be stated against *planted, pre-registered distinctions* (as [Experiment 3](../experiments/preregistration/exp3_overcompression.md) already does) rather than against free IU counts — that is the honest interim position.

---

## Inter-coder agreement plan

1. **Materials:** 10 transcript excerpts (~15 exchanges each) from pilot sessions, once any exist; until then, constructed fixtures like the above, labeled as such.
2. **Coders:** two, trained on the hybrid C3→C1 protocol with 2 calibration excerpts (excluded from analysis).
3. **Task:** independent segmentation (boundary placement) and unit counts.
4. **Statistic:** unitizing reliability (Krippendorff's unitizing alpha; Krippendorff, 2018), reported alongside raw boundary agreement. Tentative usability floor: α ≥ 0.7 — tentative because unitizing coordination-relevant spans is harder than unitizing topics, and the first round is expected to expose anchor defects rather than clear the bar.
5. **Losable outcome, pre-committed:** if trained coders cannot exceed α = 0.5 after one calibration round, no current criterion supports IU counting, and every countability-dependent claim in the framework must be rewritten in planted-distinction or ordinal-proxy terms. That result would be reported, not absorbed.

---

## Breaking the IU/MCW circularity: an existence criterion for the MCW

C1 already de-circularizes the IU (defined via receiver behavior, not via the MCW). The other half: what would make "a shared coordination state" more than a manner of speaking about two overlapping individual models plus a transcript?

**Proposed existence criterion (the yoked-outsider test):**

> An MCW exists for a dyad to the extent that the dyad's members resolve their own interaction's ambiguities — ellipsis, deictic references, task shorthand — better than *yoked outsiders* given the identical transcript and task materials.

Design sketch: at pre-registered points, pause the interaction and probe both the participant and (separately) an outsider who has read the full transcript: "what does 'the earlier version' refer to here?", "what will the next message most likely ask for?" If insiders systematically beat yoked outsiders, there is dyad-specific coordination state not carried by the transcript — an emergent residue worth a name. **If insiders never beat yoked outsiders, the transcript plus individual models suffice, the "emergent, stored-nowhere" ontology is unsupported, and the framework should drop it** — that is this note's losable bet, and it attacks the framework's central construct directly.

Caveats, stated now: outsider matching is hard (expertise, prior task familiarity); the AI-side "insider" probe measures the model's in-context behavior, not a mental state; and a positive result shows *some* dyad-specific state, not the full MCW as canonically described. The criterion bounds the ontology; it does not vindicate every property claimed for it.

---

## What remains unresolved

1. **Minimality is not unique** under C1; two coders can defend different minimal spans. The protocol treats disagreement as data, but the theory has no principled tiebreaker.
2. **Non-contiguous IUs** (a constraint stated across two turns) break span-based segmentation entirely.
3. **Granularity relativity:** the same utterance segments differently under different task grains; IU counts are task-indexed, which the glossary does not yet say.
4. **Paraphrase identity:** no criterion here decides when two phrasings are the *same* IU — required for "IU distinctions lost" claims and untouched by all three candidates.
5. **"IU entropy accumulation"** remains undefined even granting countability: a count is not a distribution (see the [Entropy status](../glossary.md#entropy)). Countability is necessary, not sufficient, for that phrase to mean anything.

None of these are hidden; a reviewer will find them, and this page exists so that they find them already named.
