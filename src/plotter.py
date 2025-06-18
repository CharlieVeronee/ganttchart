import matplotlib.pyplot as plt
import pandas as pd

def plot_phase(ax, y_index: int, row: pd.Series, phase: str, start_col: str, end_col: str, dur_col: str, color, y_offset: int):
    start = row[start_col]
    end = row[end_col]
    duration = row[dur_col]
    # draw bar
    ax.barh(
        y = y_index + y_offset,
        width  = duration,
        left   = start,
        height = 0.3,
        color  = color,
    )

    # annotate
    ax.text(
        x = start + pd.Timedelta(days=duration/2),
        y = y_index + y_offset,
        s = f"{phase}: {duration} days",
        va = "center",
        ha  = "center",
        fontsize=8,
        color = "black"
    )


def plot_ship_row(ax, index, row, color_map):
    color = color_map[row["Ship Name"]]
    #plot maintenance and docking phases
    plot_phase(
        ax, index, row,
        phase = "Maintenance",
        start_col = "Maintenance Start Date",
        end_col = "Maintenance End Date",
        dur_col = "Maintenance Duration",
        color = color,
        y_offset = +0.2
    )
    plot_phase(
        ax, index, row,
        phase = "Docking",
        start_col  = "Docking Start Date",
        end_col    = "Docking End Date",
        dur_col = "Docking Duration",
        color      = color,
        y_offset   = -0.2
    )