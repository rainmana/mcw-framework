# Anchored H/R/D/M Rubrics & Inter-Rater Reliability Protocol

**Status:** Declared extension (Constitution [Article V](../constitution.md#article-v-extension-protocol)) · Evidence: L0 — instrument design, unpiloted. This page is the missing artifact between Article IV's L2 and L3: without it, no experiment using H/R/D/M can report inter-rater reliability, and no claim above L2 is reachable.

---

## Article V declaration block

- **Declaration.** This page *extends* the four canonical measurement proxies
  (H, R, D, M) with: behavioral anchors for each scale point, rater
  instructions, a blinded dual-rater reliability protocol, a split of R into
  repair-event count versus repair cost, a behavioral proxy definition for D,
  and a scope restriction for M. It is an extension, not a replacement: the
  canonical one-line definitions and 0–3 scale semantics in the
  [glossary](../glossary.md#measurement-proxies) are unchanged.
- **Non-contradiction.** Each anchor set instantiates its canonical
  description. Where the canonical D is phrased in terms of the shared
  coordination state itself (which is not directly observable), this page
  supplies a *measurement model* — observable consequences that stand in for
  the construct — and says so explicitly rather than quietly redefining D.
- **Falsification condition.** If, after one calibration round, two
  independent raters blinded to condition cannot reach quadratic-weighted
  kappa ≥ 0.4 on H and R across at least 12 transcripts, these rubrics fail
  as a measurement instrument, and H/R/D/M must not be used as outcome
  measures in any experiment claiming L3 evidence. That outcome would count
  *against* this extension and would be reported.
- **Layer 0 trace.** Four questions anyone can ask about a conversation —
  *how well do we understand each other? how hard was it to get back on
  track? how fast are we sliding apart? are we blaming the tool for a
  conversation problem?* — each scored 0–3 from things you can point to in
  the transcript.

---

## Rating units and shared definitions

These definitions are used by every anchor below. Raters apply them
mechanically; disputes about them are instrument bugs to be filed, not
resolved ad hoc mid-rating.

| Term | Definition |
|---|---|
| **Turn** | One message by one party. |
| **Exchange** | An adjacent pair of turns (one from each party). |
| **Window** | Five consecutive exchanges (or one natural task phase, if the protocol pre-declares phase boundaries). H, D, and M are scored per window. |
| **Repair-initiating turn** | A turn whose primary function is repair: it contains a clarification request, a correction of the other party's stated understanding, a restatement request, an explicit re-grounding move ("let's step back…"), or an explicit synchronization move ("since last time, X changed"). |
| **Repair episode** | The span from a repair-initiating turn to the first turn where both parties proceed without re-raising that misalignment. R (cost) is scored per repair episode. |
| **Dedicated repair turn** | A turn inside a repair episode that advances repair rather than the task. |
| **Late discovery** | A misalignment surfaced three or more exchanges after the turn that introduced the diverging IU (the rater must be able to point to both turns). |
| **Capability-blame statement** | An utterance attributing a failure to the counterpart's intelligence, competence, or model quality ("it's just not smart enough," "the model can't do this"), as opposed to attributing it to information not exchanged. |

---

## H — MCW Health (0–3), per window

Canonical definition: *perceived shared understanding between participants*
(`0 = broken / 3 = strong`).

| Score | Behavioral anchor |
|---|---|
| **H3 — strong** | No misalignment surfaces in the window; both parties use references to earlier content correctly (no corrections needed); at most one trivial clarification, resolved within a single exchange. |
| **H2 — adequate** | Minor misalignment surfaces but is repaired within the window in ≤ 2 dedicated repair turns; no completed work is discarded or redone. |
| **H1 — strained** | At least one misalignment forces rework or discarding of a work product, OR the same IU requires ≥ 2 clarification attempts without convergence within the window. |
| **H0 — broken** | The parties demonstrably pursue different goals or referents; a work product is rejected wholesale; or the interaction is abandoned or reset within the window. |

---

## R — Repair Cost (0–3), per repair episode

Canonical definition: *effort required to realign after a coordination
failure* (`0 = low / 3 = high`).

| Score | Behavioral anchor |
|---|---|
| **R0 — low** | Realignment within ≤ 1 dedicated repair turn; no work discarded. |
| **R1** | Realignment within 2 dedicated repair turns, or minor rework (a small portion of produced content revised). |
| **R2** | Realignment required 3–5 dedicated repair turns, or a work product had to be substantially redone. |
| **R3 — high** | Realignment required > 5 dedicated repair turns, a full restart/reset, or repair was abandoned with the misalignment left standing. |

### R split: repair-event count (R\_ev) vs. repair cost (R)

The system-prompt derivation's Prediction 1 ("reduced early repair events")
needs a *count*, but canonical R is a *cost*. Conflating them makes the
prediction unscorable. This extension therefore splits:

- **R (canonical, unchanged):** the 0–3 ordinal cost per repair episode, as
  anchored above.
- **R\_ev (extension):** the number of distinct repair episodes initiated per
  10 exchanges. A count, not an ordinal; report it as a rate.

A healthy interaction can have high R\_ev with low R (many cheap repairs —
often a *good* sign), which is precisely the distinction the single letter
was erasing.

---

## D — Drift Rate (0–3), per window

Canonical definition: *speed at which the shared coordination state
diverges* (`0 = stable / 3 = rapid`).

**Measurement model (stated, not smuggled):** the shared coordination state
is not directly observable, so D cannot be rated from it. This proxy scores
the observable signature of drift — *late discoveries*: misalignments that
surface well after the turn that introduced them. Fast-surfacing
misalignment is a repair event, not drift; misalignment that incubates is
drift. This is a measurement model for canonical D, not a new definition.

| Score | Behavioral anchor |
|---|---|
| **D0 — stable** | No late discoveries; any misalignment surfaces within 2 exchanges of the turn that introduced it. |
| **D1** | Exactly one late discovery in the window. |
| **D2** | Two late discoveries, or one whose introducing turn lies more than 10 exchanges back. |
| **D3 — rapid** | Three or more late discoveries, or the parties' end-of-window statements of the current goal materially disagree (where the protocol elicits or the transcript contains such statements). |

---

## M — Misattribution (0–3), per window — **Human ↔ AI only**

Canonical definition: *tendency to blame coordination failures on agent
capability rather than shared context* (`0 = none / 3 = frequent`).

**Scope restriction (declared):** "agent capability" has no defined referent
when both parties are human. M is scored **only in Human ↔ AI interactions**.
The two Human ↔ Human toy experiments (1 and 5) do not score M; their
expected-signature tables predate this restriction and are reconciled in the
pre-registration pages. Defining an M analogue for Human ↔ Human settings
(e.g., blame directed at a partner's competence rather than at what was
never said) would be a further extension requiring its own declaration.

**Ground-truth caveat (stated, not hidden):** whether a failure "really" was
coordination rather than capability is exactly what the framework is trying
to establish (Limitation 4 of the paper outline). These anchors therefore
require *transcript evidence* — the rater must locate the needed IU and
verify it was never externalized — which is a checkable proxy for
coordination failure, not a resolution of the confound. Where the rater
cannot verify either way, the window is marked M-unratable rather than
guessed.

| Score | Behavioral anchor |
|---|---|
| **M0 — none** | No capability-blame statements; failures, where discussed, are attributed to information not exchanged. |
| **M1** | Capability blame is expressed once but withdrawn or corrected during repair ("ah — I never actually told you X"). |
| **M2** | Capability blame recurs (≥ 2 statements) without verification, or the human takes capability-flavored corrective action (regenerating, switching models, dumbing the task down) while the transcript shows the needed IU was never externalized. |
| **M3 — frequent** | The interaction strategy is reorganized around presumed incapability (wholesale distrust, abandonment, permanent oversimplification) while the transcript shows the needed IU was never externalized. |

---

## Rater instructions

1. **Materials.** Raters receive the full transcript, condition-blinded: a
   third party (or a redaction script) strips condition labels, system
   prompts, hypothesis-bearing headers, and any manipulation notes before
   rating. The rater must not know which experimental arm produced the
   transcript.
2. **Do not consult the experiments' expected-signature or graded-outcome
   tables while rating.** Those tables predict directions and would prime
   scores (demand characteristics). Rate from the anchors on this page only.
3. **Procedure.** Segment the transcript into windows; identify repair
   episodes; then score H, D, M per window and R per repair episode, plus
   R\_ev per 10 exchanges. Point to line numbers for every non-zero score —
   a score that cannot cite transcript lines is not a score.
4. **Uncertainty is recorded, not resolved by fiat.** A rater may mark any
   window "unratable" with a reason. If more than 20% of windows in a study
   are unratable, that is an instrument failure signal and must be reported
   with the results.
5. **No mid-study anchor edits.** If an anchor proves ambiguous, finish the
   rating pass, file the ambiguity, and revise anchors only between studies
   (with the revision logged on this page's history).

---

## Inter-rater reliability protocol

- **Raters:** two minimum, rating independently, blinded to condition and to
  each other's scores.
- **Calibration:** two transcripts rated jointly and discussed before the
  study; calibration transcripts are excluded from analysis.
- **Corpus:** at least 12 transcripts (≥ 48 rated windows per proxy) before
  any experiment reports H/R/D/M as outcomes at L3.
- **Statistics:** quadratic-weighted Cohen's kappa per proxy (ordinal
  distances matter), with Krippendorff's alpha (ordinal) reported alongside
  as a robustness check.
- **Targets:** κ_w ≥ 0.6 per proxy to treat the instrument as usable;
  α ≥ 0.667 for tentative conclusions and α ≥ 0.8 for firm ones. Between
  0.4 and 0.6, results may be reported only with the reliability figures
  attached and claims capped at L2.
- **Failure rule (the losable bet, restated):** κ_w < 0.4 on H and R after
  one calibration round across ≥ 12 transcripts falsifies this instrument —
  see the declaration block. Disagreements of more than one scale point on
  the same window are logged as anchor defects regardless of aggregate κ.
- **Adjudication:** post-hoc consensus scores may be produced for exploratory
  analysis but are never substituted for the independent scores in
  reliability reporting.

---

## What this page does not claim

1. Not that these anchors are validated — they are unpiloted (L0) until the
   reliability protocol has been run.
2. Not that transcript-verifiable IU absence resolves the coordination-vs-
   capability confound; it bounds it (see the M caveat).
3. Not that the thresholds (5-exchange windows, 3-exchange late-discovery
   lag, the κ targets) are uniquely correct — they are pre-committed so they
   cannot be chosen after seeing results, which is the point of committing
   to them now.
