# Contributing
Work in a branch and open a pull request. Keep changes tied to a research objective.
Run `Rscript -e 'testthat::test_local()'`, `R CMD build .` and
`R CMD check --no-manual aimlsptm_0.0.0.9000.tar.gz`.
Run `Rscript -e 'roxygen2::roxygenise()'` after changing public documentation.
Do not commit restricted data or generated simulation batches. Record statistical
assumptions, seeds and independent validation evidence for methodological changes.
