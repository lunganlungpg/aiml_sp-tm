#' Enumerate schedules with early, middle and late coverage
#'
#' This enumerates feasible schedules only; it does not optimize an AUC criterion.
#' @param times Six strictly increasing finite candidate observation times.
#' @return A matrix with one feasible three-time schedule per row.
#' @export
#' @examples
#' choose_times(1:6)
choose_times <- function(times = seq_len(6L)) {
  if (!is.numeric(times) || length(times) != 6L ||
      any(!is.finite(times)) || any(diff(times) <= 0)) {
    stop("times must contain six strictly increasing finite numbers")
  }
  indices <- t(utils::combn(seq_len(6L), 3L))
  keep <- apply(indices, 1L, function(i) {
    length(unique((i - 1L) %/% 2L)) == 3L
  })
  matrix(times[indices[keep, , drop = FALSE]], ncol = 3L)
}
