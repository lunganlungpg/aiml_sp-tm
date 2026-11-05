# Data and reproducibility
Keep institutional/raw data outside Git. Record source, version, checksum, access
conditions, field geometry, season, units, missingness and preprocessing in a data
manifest before analysis. Never publish personal data, credentials or restricted
field coordinates. Synthetic examples must be labelled synthetic.

Initial public candidates: agridat::bose.multi.uniformity (15 x 26) and
agridat::baker.barley.uniformity (3 x 19). Audit installed dataset documentation
and reuse permissions before importing. These geometries are not the main 20 x 10
simulation geometry. No datasets are downloaded automatically.

Each experiment should save configuration, seed, Git commit, sessionInfo(), data
checksums, search budget, fit failures and Monte Carlo uncertainty. Outputs are
ignored by Git; archive reviewed releases and permitted results separately.

After selecting modelling dependencies, use renv::init() and renv::snapshot(),
review and commit the resulting lockfile, and verify renv::restore() in a fresh
environment. No untested dependency lockfile is supplied by this scaffold.
