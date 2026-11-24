# Container image published to GitHub Packages as
#   ghcr.io/lunganlungpg/aiml_sp-tm
#
#   docker run --rm ghcr.io/lunganlungpg/aiml_sp-tm            # baseline design -> outputs/
#   docker run --rm -it ghcr.io/lunganlungpg/aiml_sp-tm R      # R session with aimlsptm loaded via library()

# rocker/r-ver = Ubuntu + pinned R, preconfigured for fast binary CRAN installs.
FROM rocker/r-ver:4.4.2

LABEL org.opencontainers.image.title="aiml_sp-tm" \
      org.opencontainers.image.description="aimlsptm: spatio-temporal agricultural experimental design (R)" \
      org.opencontainers.image.licenses="GPL-3.0-only"

WORKDIR /opt/aiml_sp-tm
COPY . .

# Install the package itself (it has no hard dependencies beyond base R).
RUN R CMD INSTALL . \
 && Rscript -e 'library(aimlsptm); cat("aimlsptm", as.character(packageVersion("aimlsptm")), "\n")'

# Default: reproduce the baseline fieldbook and schedules into ./outputs
CMD ["Rscript", "scripts/example.R"]
