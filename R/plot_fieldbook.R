#' Plot a paired-row resolvable agricultural field layout
#'
#' Produces a grid visualization of the fieldbook with treatments and replicates.
#' @param layout Data frame returned by generate_blocks().
#' @return A matrix representing the spatial treatment allocation across rows and columns.
#' @export
plot_fieldbook <- function(layout) {
  if (!is.data.frame(layout) || !all(c("row", "column", "replicate", "treatment") %in% names(layout))) {
    stop("layout must contain row, column, replicate, and treatment columns")
  }
  nr <- max(layout$row)
  nc <- max(layout$column)
  grid_mat <- matrix(NA_integer_, nrow = nr, ncol = nc)
  for (i in seq_len(nrow(layout))) {
    grid_mat[layout$row[i], layout$column[i]] <- layout$treatment[i]
  }
  rownames(grid_mat) <- paste0("Row_", seq_len(nr))
  colnames(grid_mat) <- paste0("Col_", seq_len(nc))
  grid_mat
}
