import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import plotly as plot

from data_loader import ship_data_loader
from transformers import date_transformation, sort_duration_start, add_duration
from plotter import plot_ship_row
from aesthetics import colormap

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
ax.set(title = 'Maintenance And Docking Gantt Chart', ylabel = 'Ship Name', xlabel = 'Date') #title and axis names

#y axis
y_positions = list(range(len(ship_df))) #y axis datatype is number, need length of rows as y axis
ax.set_yticks(y_positions)
ax.set_yticklabels(ship_df['Ship Name']) #y tables
ax.invert_yaxis() #first ship on bottom -> first ship on top

#x axis
ax.xaxis_date()
#MAKE IT SO WORDS STAY IN GRAPH
#mAKE IT SO DATES ARE READABLE
ax.xaxis.set_major_locator(dates.MonthLocator())
ax.xaxis.set_major_formatter(dates.DateFormatter('%b %Y'))

ax.legend(loc = 'best') #no overlapping chart elements
plt.show()


#summary statistics


#ADD SUMMARY STATISTICS + VIEWING FOR DATA
#average days docking or maintenance