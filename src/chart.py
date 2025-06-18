import matplotlib.pyplot as plt

from data_loader import ship_data_loader
from transformers import date_transformation, sort_duration_start, add_duration
from plotter import plot_ship_row
from aesthetics import colormap, axes_format

#Data Loading + Transformation
ship_df = ship_data_loader("data/Gantt_Chart_Data_Set.xlsx")
ship_df = date_transformation(ship_df)
ship_df = sort_duration_start(ship_df)
ship_df = add_duration(ship_df)

color_map = colormap(ship_df)


#Establish Figure
fig, ax = plt.subplots(figsize=(20, 10))

#Plot Maintenance + Docking Rows
for i,row in ship_df.iterrows(): #iterate over DataFrame rows as (index, Series) pairs
    plot_ship_row(ax, i, row, color_map)


#Post-Plotting Aesthetics
axes_format(
    ax,
    ship_names=ship_df["Ship Name"].tolist(),
    title="Maintenance And Docking Gantt Chart",
    xlabel="Date",
    ylabel="Ship Name",
    date="%b %Y",
)

plt.tight_layout()
plt.show()


#summary statistics


#ADD SUMMARY STATISTICS + VIEWING FOR DATA
#average days docking or maintenance