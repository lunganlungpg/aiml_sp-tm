# Setup validation

Validated in the prepared Linux cloud instance with R 4.5.3:
- Package installation: passed.
- testthat suite: 16 assertions passed; zero failures, warnings or skips.
- Complete smoke example: 200 plots, 20 treatments, 10 paired-row replicates;
  eight schedules; CSV fieldbook and session information exported.
- R CMD build: passed.
- R CMD check --no-manual: Status OK. Remote CRAN/Bioconductor index requests
  were blocked by network policy; installed dependencies, examples and tests
  were checked successfully. PDF manual generation was not run.
- Local dependency refresh from SHA256-pinned explicit lockfile: passed;
  installation, tests and smoke example passed again afterward.

GitHub-hosted workflow outcomes require checking the Actions tab after push.
Local success does not establish a GitHub-hosted CI result.

The cloud configuration draft saves install and startup instructions, plus
api.github.com as a custom allowed destination. It requires review/save and
publication in environment settings. Saving does not apply the network change
or publish the prepared filesystem snapshot. New-task restoration has not been
validated. The local R runtime and standalone conda executable are outside Git
under /workspace/tools and are intended to be retained in that snapshot.

Live GitHub Project creation and repository protection settings were not applied:
GitHub API access returned a proxy-level 403. See project-board.md for the backlog.
