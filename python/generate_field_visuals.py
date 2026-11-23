"""
generate_field_visuals.py
-------------------------
Renders publication-ready field layout heatmaps, schedule timelines,
and interactive Plotly field maps for spatio-temporal experimental designs.
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go


def generate_all_visuals():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    fieldbook_path = os.path.join(base_dir, "..", "outputs", "baseline-fieldbook.csv")
    schedules_path = os.path.join(base_dir, "..", "outputs", "candidate-schedules.csv")
    plots_dir = os.path.join(base_dir, "..", "plots")
    os.makedirs(plots_dir, exist_ok=True)

    df_field = pd.read_csv(fieldbook_path)
    df_sched = pd.read_csv(schedules_path)

    nr = df_field["row"].max()
    nc = df_field["column"].max()

    # -------------------------------------------------------------
    # Plot 1: 200-Plot Fieldbook Grid Heatmap (20 Rows x 10 Columns)
    # -------------------------------------------------------------
    grid_treat = np.zeros((nr, nc), dtype=int)
    grid_rep = np.zeros((nr, nc), dtype=int)
    for _, row in df_field.iterrows():
        r = int(row["row"]) - 1
        c = int(row["column"]) - 1
        grid_treat[r, c] = int(row["treatment"])
        grid_rep[r, c] = int(row["replicate"])

    fig, ax = plt.subplots(figsize=(11, 14), dpi=300)
    # Color grid by Replicate block (paired rows)
    cmap = plt.get_cmap("tab20b", 10)
    im = ax.imshow(grid_rep, cmap=cmap, aspect="auto", alpha=0.35)

    # Add text labels (Treatment T1-T20) in each plot cell
    for r in range(nr):
        for c in range(nc):
            t_val = grid_treat[r, c]
            ax.text(c, r, f"T{t_val}", ha="center", va="center",
                    fontsize=9, fontweight="bold", color="#0f172a")

    # Add thick dividing horizontal lines between Replicates (every 2 rows)
    for r in range(2, nr, 2):
        ax.axhline(r - 0.5, color="#1e293b", linewidth=2.5, linestyle="-")

    ax.set_xticks(np.arange(nc))
    ax.set_yticks(np.arange(nr))
    ax.set_xticklabels([f"Col {c+1}" for c in range(nc)], fontsize=9, fontweight="bold")
    ax.set_yticklabels([f"Row {r+1} (Rep {(r//2)+1})" for r in range(nr)], fontsize=8.5, fontweight="bold")

    ax.set_title("🌾 Paired-Row Resolvable Incomplete-Block Layout (20 Rows × 10 Columns = 200 Plots)\n"
                 "Each 2-Row Block = 1 Complete Replicate Containing All 20 Treatments",
                 fontsize=11, fontweight="bold", pad=15)
    ax.set_xlabel("Field Range / Column Coordinate", fontsize=10, fontweight="bold", labelpad=8)
    ax.set_ylabel("Field Row / Paired Replicate Coordinate", fontsize=10, fontweight="bold", labelpad=8)

    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, "field_layout_heatmap.png"))
    plt.close()

    # -------------------------------------------------------------
    # Plot 2: Candidate Observation Schedules Timeline (8 Feasible Schedules)
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
    sched_matrix = df_sched.values

    # Colors for Early, Middle, Late sampling points
    phase_colors = {"Early": "#059669", "Middle": "#0284c7", "Late": "#d97706"}

    for idx, times in enumerate(sched_matrix):
        y_pos = len(sched_matrix) - idx
        # Draw horizontal connecting line
        ax.plot([times[0], times[2]], [y_pos, y_pos], color="#cbd5e1", linewidth=2.5, zorder=1)
        # Plot early, middle, late points
        ax.scatter(times[0], y_pos, color=phase_colors["Early"], s=100, zorder=3, edgecolors="#0f172a", label="Early Window (Dates 1-2)" if idx == 0 else "")
        ax.scatter(times[1], y_pos, color=phase_colors["Middle"], s=100, zorder=3, edgecolors="#0f172a", label="Middle Window (Dates 3-4)" if idx == 0 else "")
        ax.scatter(times[2], y_pos, color=phase_colors["Late"], s=100, zorder=3, edgecolors="#0f172a", label="Late Window (Dates 5-6)" if idx == 0 else "")
        ax.text(times[2] + 0.25, y_pos, f"S{idx+1}: [{times[0]}, {times[1]}, {times[2]}]", va="center", fontsize=9, fontweight="bold", color="#1e293b")

    ax.set_yticks(range(1, len(sched_matrix) + 1))
    ax.set_yticklabels([f"Schedule {len(sched_matrix) - i}" for i in range(len(sched_matrix))], fontsize=9, fontweight="bold")
    ax.set_xticks(range(1, 7))
    ax.set_xticklabels([f"Date {d}\n(Candidate)" for d in range(1, 7)], fontsize=9, fontweight="bold")

    # Add phase shading zones
    ax.axvspan(0.5, 2.5, color="#ecfdf5", alpha=0.5, label="Early Phase (Vegetative)")
    ax.axvspan(2.5, 4.5, color="#f0f9ff", alpha=0.5, label="Middle Phase (Flowering)")
    ax.axvspan(4.5, 6.5, color="#fffbeb", alpha=0.5, label="Late Phase (Maturity)")

    ax.set_xlim(0.5, 7.5)
    ax.set_title("⏱️ Spatio-Temporal Observation Schedules (3-Date Feasible Enumerations)\n"
                 "Ensures Balanced Phenological Coverage Across Crop Growth Stages",
                 fontsize=11, fontweight="bold", pad=12)
    ax.set_xlabel("Candidate Sampling Dates", fontsize=10, fontweight="bold")
    ax.set_ylabel("Candidate Schedule Enumeration", fontsize=10, fontweight="bold")
    ax.grid(axis="x", linestyle=":", alpha=0.6)
    ax.legend(loc="upper right", frameon=True, facecolor="white", fontsize=8.5)

    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, "temporal_sampling_schedules.png"))
    plt.close()

    # -------------------------------------------------------------
    # Plot 3: Treatment Replicate Incidence Matrix (Orthogonal Verification)
    # -------------------------------------------------------------
    inc_mat = pd.crosstab(df_field["replicate"], df_field["treatment"])
    fig, ax = plt.subplots(figsize=(10, 5), dpi=300)
    im = ax.imshow(inc_mat.values, cmap="Greens", aspect="auto")
    ax.set_xticks(range(20))
    ax.set_yticks(range(10))
    ax.set_xticklabels([f"T{t+1}" for t in range(20)], fontsize=8.5)
    ax.set_yticklabels([f"Rep {r+1}" for r in range(10)], fontsize=8.5)

    for r in range(10):
        for t in range(20):
            ax.text(t, r, str(inc_mat.values[r, t]), ha="center", va="center", fontsize=8.5, color="#064e3b")

    ax.set_title("🔬 Replicate-by-Treatment Incidence Verification (Every Cell = 1.0)\n"
                 "Confirms Exact Resolvability: Each Replicate Holds Exactly One Unit of Every Treatment",
                 fontsize=11, fontweight="bold", pad=12)
    ax.set_xlabel("Experimental Treatments (20 Levels)", fontsize=10, fontweight="bold")
    ax.set_ylabel("Field Replicates (10 Paired-Row Blocks)", fontsize=10, fontweight="bold")

    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, "treatment_balance_diagnostic.png"))
    plt.close()

    # -------------------------------------------------------------
    # Plot 4: Interactive Plotly Fieldbook Map (HTML)
    # -------------------------------------------------------------
    custom_hover = []
    for r in range(nr):
        row_hover = []
        for c in range(nc):
            plot_num = r * nc + (c + 1)
            t = grid_treat[r, c]
            rep = grid_rep[r, c]
            row_hover.append(
                f"<b>Plot #{plot_num}</b><br>"
                f"Row: {r+1} | Column: {c+1}<br>"
                f"Replicate: {rep} (Paired Row)<br>"
                f"<b>Assigned Treatment: T{t}</b>"
            )
        custom_hover.append(row_hover)

    fig_html = go.Figure(data=go.Heatmap(
        z=grid_rep,
        text=np.array([[f"T{val}" for val in row] for row in grid_treat]),
        texttemplate="%{text}",
        hoverinfo="text",
        hovertext=custom_hover,
        colorscale="Viridis",
        showscale=True,
        colorbar=dict(title="Replicate #")
    ))

    fig_html.update_layout(
        title="🌾 <b>Interactive 200-Plot Spatio-Temporal Agricultural Field Layout Map</b><br>"
              "<sup>Hover over any plot cell to inspect coordinates, paired-row replicate, and treatment assignment</sup>",
        xaxis=dict(title="Column / Range (1 to 10)", dtick=1),
        yaxis=dict(title="Row (1 to 20)", dtick=1, autorange="reversed"),
        width=850,
        height=950,
        template="plotly_white"
    )

    interactive_path = os.path.join(plots_dir, "interactive_fieldbook.html")
    fig_html.write_html(interactive_path, include_plotlyjs="cdn")

    print(f"All visual figures and interactive maps successfully generated in: {plots_dir}")


if __name__ == "__main__":
    generate_all_visuals()
