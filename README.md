# AI/ML Guided Spatio-Temporal Agricultural Experimental Design

PhD research repository of **Lunganlung P G**, Agricultural Statistics,
ICAR–Indian Agricultural Research Institute.

This is an initial research scaffold based on the supplied Outline of Research
Work (ORW), not a completed or statistically validated optimization method.

## Start here
Install R (>= 4.1), then from the repository root:

```r
install.packages(c("testthat", "roxygen2"))
```
```sh
R CMD INSTALL .
Rscript scripts/example.R
Rscript -e 'testthat::test_local()'
R CMD build .
R CMD check --no-manual aimlsptm_0.0.0.9000.tar.gz
```

For the prepared Codex cloud environment, first run
`export PATH="/workspace/tools/r/bin:$PATH"`. A SHA256-pinned Linux environment
is recorded in `docs/environment-linux-64.lock`; with conda installed, recreate it
using `conda create -p /path/to/r-env --file docs/environment-linux-64.lock`.
The shorter `docs/environment.yml` describes dependency intent rather than a lock.
The current environment uses R 4.5.3; CI uses the current supported R release.

Open `aiml_sp-tm.Rproj` in RStudio if preferred. The example exports a validated
200-plot baseline fieldbook, candidate schedules and session information to
`outputs/`. Call `set.seed()` before randomization.

## What currently works
- Paired-row resolvable randomization: 20 rows x 10 columns, 20 treatments,
  10 replicates, each treatment exactly once per two-row replicate.
- Structural layout validation and enumeration of eight three-date schedules
  with early/middle/late coverage among six ordered candidate dates.
- Tests, R package checks and a small research example in GitHub Actions.

The baseline is unoptimized. Temporal regime allocation and statistical scoring
remain planned work. CI runs short checks, not thesis-scale simulations.

## Repository guide
| Path | Purpose |
| --- | --- |
| `R/`, `man/`, `tests/` | Package code, reference documentation and tests |
| `scripts/` | Reproducible entry points |
| `config/` | Explicit pilot planning settings (not an executable simulation) |
| `docs/orw/` | Original supplied research outline |
| `docs/research-plan.md` | Objectives, milestones and scientific gates |
| `docs/data-management.md` | Provenance, permissions and reproducibility |
| `docs/project-board.md` | GitHub Project board blueprint and initial backlog |
| `data/` | Local data locations; data contents ignored |
| `outputs/` | Generated local results; contents ignored |

## GitHub automation
The **R package checks** and **Research smoke example** workflows run on pushes to
`main`, pull requests and manual dispatch. No repository secrets are required.
After the first successful CI run, the owner can protect `main` by requiring
these checks and pull-request review in repository Settings. Project creation
and branch protection require GitHub account permissions and are separate settings.

## Research scope
The four ORW objectives concern spatial allocation, joint treatment/measurement
timing, spatio-temporal mixed-model evaluation, and R package development.
See the research plan for methods that are not implemented. Nitrogen rates and
application windows require agronomist approval before real-world use.

Package code is licensed under GPL-3. The supplied ORW is retained as an authored
research document; institutional data and third-party datasets retain their own
permissions. See `docs/orw/README.md`.
