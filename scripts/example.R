# scripts/example.R
# Reproducible execution of baseline spatio-temporal experimental design

if (!suppressWarnings(requireNamespace("aimlsptm", quietly = TRUE))) {
  source("R/layout.R")
  source("R/times.R")
} else {
  library(aimlsptm)
}

set.seed(2026)
layout <- generate_blocks()
stopifnot(validate_layout(layout))

dir.create("outputs", showWarnings = FALSE)
write.csv(layout, "outputs/baseline-fieldbook.csv", row.names = FALSE)
write.csv(choose_times(), "outputs/candidate-schedules.csv", row.names = FALSE)
writeLines(capture.output(sessionInfo()), "outputs/session-info.txt")

cat("Validated 200 plots, 20 treatments, 10 paired-row replicates; 8 feasible schedules.\n")
cat("Outputs exported to outputs/baseline-fieldbook.csv and outputs/candidate-schedules.csv\n")
