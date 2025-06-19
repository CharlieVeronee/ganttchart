import matplotlib.pyplot as plt

from data_loader import ship_data_loader
from transformers import date_transformation, sort_duration_start, add_duration
from plotter import plot_ship_row
from aesthetics import colormap, axes_format, today_line, x_axis_margins
from utils import summary_stats
from dependencies import draw_docking_overlap

# Data Loading + Transformation
ship_df = ship_data_loader("data/Gantt_Chart_Data_Set.xlsx")
ship_df = date_transformation(ship_df)
ship_df = sort_duration_start(ship_df)
ship_df = add_duration(ship_df)

color_map = colormap(ship_df)


# Establish Figure
fig, ax = plt.subplots(figsize=(20, 10))

# Toggles
endpoints = False #show data endpoints
docking_dependency = False #show docking overlap
todayline = False #show today line

# Plot Maintenance + Docking Rows
for i,row in ship_df.iterrows(): #iterate over DataFrame rows as (index, Series) pairs
    plot_ship_row(ax, i, row, color_map, endpoints)
    
# Overlays
if docking_dependency:
    draw_docking_overlap(ax, ship_df)

# Post-Plotting Aesthetics
axes_format(
    ax,
    ship_names=ship_df["Ship Name"].tolist(),
    title="Maintenance And Docking Gantt Chart",
    xlabel="Date",
    ylabel="Ship Name",
    date="%b %Y",
)

x_axis_margins(ax, ship_df) #adding some margins to x axis

if todayline:
    today_line(ax)

# Summary Stats
summary_df = summary_stats(ship_df)
summary_df.to_csv("gantt_stats.csv", index=True)
print(summary_df)

# Plot Figure
ax.legend(loc="best")
plt.tight_layout()
fig.savefig("gantt_chart.png", dpi=300, bbox_inches="tight")
plt.show()