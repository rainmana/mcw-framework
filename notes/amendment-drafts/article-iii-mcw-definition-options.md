# Decision memo: Article III vs. the canonical MCW definition

**Status: DECIDED — Option B adopted** (Constitution v1.1, July 2026; author
delegated the choice and the amendment was filed with the Option B paperwork —
see `docs/constitution.md` § Amendments). This memo is retained unchanged below
as the decision record; the drafts are historical.

---

*(Original memo follows.)*

**Status:** Decision memo — NOT site content, NOT canon. Two mutually exclusive
amendment drafts follow. The choice between them is reserved for the framework
author (Alec) per the amendment procedure (author consent). Nothing in this file
takes effect until one option is selected, the paperwork below is applied, and
the corresponding PR is merged by the author.

---

## The contradiction

Constitution **Article III** (Substrate Independence) states:

> MCW, IUs, and all six failure modes are substrate-independent. They apply to
> human–human, human–AI, and AI–AI coordination systems without modification.

The **canonical MCW definition** (glossary, frozen by Article I) states:

> The Meta-Context Window is the dynamically maintained shared state of meaning,
> salience, intent, and continuity that emerges through ongoing interaction
> between one or more human context windows (HCWs) and one or more artificial
> context windows (ACWs).

By the canonical definition, a human–human system contains no ACW and therefore
has no MCW. Article III asserts the opposite. The canon contradicts itself, and a
reviewer can prove it with two quotations. One of the two texts must move, via
the amendment procedure.

A relevant fact for the decision: the framework's most defensible *novel* bet
(per the 2026-07-01 assessment) is the prediction of effects specific to the
HCW-continuous / ACW-discrete asymmetry — observable only in Human↔AI
conditions. Whichever option is chosen should protect that bet.

---

## Option A — Amend the MCW definition substrate-neutrally

**Move:** keep Article III as-is; amend the canonical MCW definition so substrate
independence is definitional rather than asserted.

### Amendment paperwork (glossary frozen-field amendment)

- **Amended construct:** MCW (Meta-Context Window), canonical definition text.
- **Previous text:** *"The Meta-Context Window is the dynamically maintained
  shared state of meaning, salience, intent, and continuity that emerges through
  ongoing interaction between one or more human context windows (HCWs) and one
  or more artificial context windows (ACWs)."*
- **New text:** *"The Meta-Context Window is the dynamically maintained shared
  state of meaning, salience, intent, and continuity that emerges through
  ongoing interaction between two or more bounded context windows. The primary
  instantiation studied by this framework is the coupling of one or more human
  context windows (HCWs) with one or more artificial context windows (ACWs)."*
- **Coupling function:** becomes `MCW = f(CW₁…CWₖ, T, C)` with HCW/ACW as the
  studied special case; the glossary's HCW/ACW entries are unchanged.
- **Rationale:** resolves the Article III contradiction in the direction of the
  framework's original cross-domain ambition (README "Background" section);
  human–human and AI–AI MCWs become canonical instances, not extensions.
- **Version:** framework version bumps (v0.2 → v0.3); a "Definition history"
  block is added to the glossary entry preserving the prior text; Constitution
  text is untouched (Article III becomes true as written).

### Consequences

- **For:** preserves the substrate-general ambition; Experiments 1 and 5
  (Human↔Human) remain canonical probes of MCW itself, not extension-scoped.
- **Against:** dilutes the framework's sharpest differential prediction — if MCW
  is substrate-neutral by definition, "MCW is just common ground, renamed" gets
  *easier* to argue, because the HCW/ACW asymmetry is demoted to one instance;
  the M proxy ("blame agent capability") and Asymmetric State Advancement's
  off-turn machinery still carry Human↔AI-flavored semantics that would need
  per-construct scoping notes.

---

## Option B — Keep the HCW/ACW-scoped definition; amend Article III to a scope statement

**Move:** keep the canonical MCW definition as-is; amend Article III so that
substrate independence is claimed only for the constructs whose definitions
support it (IUs, failure modes), and MCW's HCW/ACW phrasing becomes an explicit
scope restriction with generalization as a declared-extension path.

### Amendment paperwork (Constitution amendment, v1.0 → v1.1)

- **Amended article:** III — Substrate Independence.
- **Previous text:** *"MCW, IUs, and all six failure modes are
  substrate-independent. They apply to human–human, human–AI, and AI–AI
  coordination systems without modification."*
- **New text:** *"IUs and all six failure modes are substrate-independent: they
  apply to human–human, human–AI, and AI–AI coordination systems without
  modification. The MCW construct itself is canonically defined for HCW–ACW
  coupling; this is a declared scope restriction, not an accident of phrasing.
  Generalizations of MCW to human–human or AI–AI substrates are conjectured to
  be coherent `[L1]` but must be filed as declared extensions under Article V,
  with their own falsification conditions. The framework's sharpest
  substrate-specific prediction — coordination effects arising from the
  HCW-continuous / ACW-discrete asymmetry — is testable only in Human↔AI
  conditions and is deliberately protected by this scoping."*
  (Rules 1–3 and the anti-pattern of the current Article III are retained
  unchanged beneath this text.)
- **Rationale:** resolves the contradiction in the direction of the actual
  evidence base and the framework's novel bet; keeps failure modes usable in
  the two Human↔Human toy experiments without extension paperwork (they probe
  failure modes, not the MCW construct's substrate).
- **Version:** Constitution v1.1 with prior text and rationale recorded in an
  Amendments appendix; glossary untouched.

### Consequences

- **For:** matches what the framework can actually defend today; makes the
  differential-prediction story ("what MCW predicts that grounding theory does
  not") structurally explicit; no frozen glossary text changes.
- **Against:** narrows the stated ambition (README "Background" and
  related_work's "actor-agnostic" phrasing would need small consistency edits);
  multi-agent/organizational MCW talk becomes explicitly extension-territory.

---

## Interactions either way

- **Experiments 1 and 5 (Human↔Human):** under A, canonical; under B, canonical
  as *failure-mode* probes (failure modes stay substrate-independent), but any
  claim they make about "the MCW" of two humans would be extension-scoped.
- **The ACW off-turn amendment** (separate PR in this series) is orthogonal: it
  fixes what an ACW is, not which substrates MCW spans. No conflict with either
  option, but if Option A is chosen the two amendments should share one
  framework version bump.
- **Constitution version numbering:** if Option B is chosen, note that the
  A-layer notation amendment (also in this PR series) targets Article II and
  would combine with this into a single v1.1 (or sequence as v1.1/v1.2 in merge
  order — merge order decides).

## What this memo does not do

It does not pick. Both drafts are complete enough to apply mechanically once a
choice is made. If a choice arrives with edits, the amendment paperwork above
should be updated to record the actually-adopted text as "new text."
