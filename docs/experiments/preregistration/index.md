# Pre-Registration Templates

**Status:** Pre-registration templates · Evidence: L0 — designs; a study earns L2 only by being run *as registered*, and L3 only with the reliability protocol met.

The [toy experiments](../toy_experiments.md) state falsification conditions, but as originally written no outcome could actually trigger them: every cell of every graded-outcome table had a framework-friendly reading, the falsification conditions hinged on undefined equivalence ("equivalent drift rates," "no measurable improvement"), and the designs lacked the control arms their own falsification conditions referenced. A framework that cannot lose is not falsifiable, whatever its pages say.

These templates fix that by pre-committing — before any data exists — to what counts *against* each hypothesis. One template per experiment, plus one for the [system-prompt derivation's five predictions](../../system_prompt_derivation.md).

## Shared standards

Every template on this page inherits the following unless it explicitly overrides them:

- **Instrument.** H, R, R\_ev, D, and (Human↔AI only) M are scored per the [anchored rubrics](../hrdm_rubrics.md), by two independent raters blinded to condition, with the IRR protocol and targets defined there. Raters never see the expected-signature tables.
- **Analysis.** Ordinal outcomes use ordinal methods: Wilcoxon signed-rank for within-subject comparisons, Mann–Whitney U for between-subject comparisons, ordinal (proportional-odds) regression where covariates are needed. α = 0.05, two-sided unless a direction is pre-registered on the specific prediction.
- **Equivalence.** Falsification conditions phrased as "no difference" are decided by equivalence testing (TOST), with a pre-registered margin of **±0.5 scale points** on the 0–3 proxies unless the template overrides it. "We failed to find a difference" is not equivalence; an equivalence claim requires the 90% CI to lie within the margin.
- **Sample sizes are honesty-scaled.** The minimal Ns given are feasibility-based pilot sizes powered only for large effects. Templates say this instead of pretending otherwise. A null at pilot N is *suggestive*, not conclusive; a null at the registered N with equivalence bounds met *triggers the falsification condition*.
- **Assignment.** Participants (or dyads) are randomly assigned to arms; task order is counterbalanced where a participant sees multiple tasks.
- **Stopping rule.** Data collection stops at the registered N. No optional stopping, no peeking-based extension.
- **Deviation policy.** Any deviation from a registered template is logged in the study report and demotes the study's claimable evidence layer to L1 unless the deviation was itself registered before unblinding.
- **Ethics.** Studies involving deception or engineered social pressure (Experiments 1 and 5) carry consent/debrief requirements written into their templates. Where an institutional review process is available it applies; where it is not, the template's consent and debrief provisions are the floor, not the ceiling.
- **Reporting.** Null and disconfirming results are reported with the same prominence as confirming ones. The Constitution says a null result is welcomed; these templates are where that promise becomes checkable.

## Templates

| Template | Source design | Type |
|---|---|---|
| [Experiment 1 — False Alignment Injection](exp1_false_alignment.md) | [Toy Experiment 1](../toy_experiments.md#experiment-1-false-alignment-injection) | Human ↔ Human |
| [Experiment 2 — Asymmetric State Advancement](exp2_asymmetric_advancement.md) | [Toy Experiment 2](../toy_experiments.md#experiment-2-asymmetric-state-advancement) | Human ↔ AI |
| [Experiment 3 — Overcompression Damage](exp3_overcompression.md) | [Toy Experiment 3](../toy_experiments.md#experiment-3-overcompression-damage) | Human ↔ AI |
| [Experiment 4 — Constraint Opacity Stress Test](exp4_constraint_opacity.md) | [Toy Experiment 4](../toy_experiments.md#experiment-4-constraint-opacity-stress-test) | Human ↔ AI |
| [Experiment 5 — Repair Signal Suppression](exp5_repair_suppression.md) | [Toy Experiment 5](../toy_experiments.md#experiment-5-repair-signal-suppression) | Human ↔ Human |
| [Experiment 6 — Drift Accumulation](exp6_drift.md) | [Toy Experiment 6](../toy_experiments.md#experiment-6-drift-accumulation) (declared extension) | Human ↔ AI |
| [System-Prompt Predictions 1–5](prompt_predictions.md) | [System Prompt Derivation](../../system_prompt_derivation.md#falsifiable-predictions) | Human ↔ AI |

These templates supersede the toy-experiments pages *for scoring and interpretation purposes*; the toy-experiments page remains the design rationale.
