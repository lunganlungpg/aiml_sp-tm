# Research plan from the ORW

Title: AI/ML Guided Spatio-Temporal Design of Agricultural Field Experiments.
The original ORW in `docs/orw/` is the source; this summary is a working roadmap.

| Objective | Planned work | Completion evidence |
| --- | --- | --- |
| 1 | Learned pre-treatment mean maps; robust covariate-adjusted A-type allocation | Independent criterion checks; fair benchmarks; held-out field evaluation |
| 2 | Joint six-regime spatial assignment and three-of-six observation schedule | Estimable prespecified AUC contrast; agronomist-approved regime definitions |
| 3 | Covariance misspecification and mixed-model inference | Bias, RMSE, coverage, convergence and failure rates, Monte Carlo uncertainty |
| 4 | Validated R package | Tests, documentation, reproducible examples and archived environment |

## Milestones
- Nov–Dec 2026: literature audit and criterion-equivalence note.
- Dec 2026–Feb 2027: baseline design library and benchmark audit.
- By 28 February 2027: public/institutional data decision and agronomic sign-off.
- Mar–Jun 2027: held-out-field prediction and transfer evaluation.
- Jun–Sep 2027: verified criterion, covariance ensemble, randomization; freeze protocol.
- Oct–Dec 2027: spatial simulations.
- Jan–Jul 2028: joint temporal design and validation.
- Aug–Nov 2028: inference study and training-only robustness feedback.
- Dec 2028–Mar 2029: confirmation runs and package release candidate.
- Apr–Sep 2029: manuscripts and thesis synthesis.

## Scientific gates
Use only pre-treatment information for design. Separate training, tuning and final
confirmation seeds/fields. Pair methods on identical simulated fields, constraints
and recorded search budgets. Do not interpret conditional predictive intervals as
pure epistemic uncertainty. Report failed/singular fits in failure-rate denominators.
Report harm from misleading maps as well as gains; no ML advantage is assumed.

The primary geometry is 20 x 10, with 20 treatments appearing once per two-row
replicate. Temporal work uses a separate 12 x 10 geometry, six regimes, and 20
replications. Coded nitrogen rates and windows are placeholders, not agronomic advice.

## Not implemented yet
Mean-map learners, covariance estimation, A-type scoring, optimized swaps,
mixture randomization, AUC scoring, mixed-model inference and production simulations.
Do not use baseline randomization as evidence of optimized design performance.
