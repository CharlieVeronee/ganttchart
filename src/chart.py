import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import plotly as plot

#Load Data From Excel
ship_df = pd.read_excel('/Users/charlesveronee/Desktop/GitHub_Projects/ganttchart/data/Gantt_Chart_Data_Set.xlsx')


#Data Cleaning + Formatting
for col in ['Maintenance Start Date', 'Maintenance End Date', 'Docking Start Date', 'Docking End Date']:
    ship_df[col] = pd.to_datetime(ship_df[col], format='%m/%d/%y') #ensure proper date format

ship_df = ship_df.sort_values("Docking Start Date").reset_index(drop=True) #sort by docking start date and reset index for iterrows()


#Establish Figure
fig, ax = plt.subplots(figsize=(20, 10))

#Pre-Plotting Aesthetics
#MAKE A COLOR PICKER THAT CREATES COLORS FOR EACH SHIP
#ADD LABELS FOR __DAYS IN MAINTENANCE
#ADD PLOTLY iNTERACTION THAT SHOWS ^
#ADD PLOTLY INTERACTION THAT SHOWS DEPENDENCIES

for i,row in ship_df.iterrows():
    #iterate over DataFrame rows as (index, Series) pairs.
    ax.barh(y = i+.2, width = (row['Maintenance End Date'] - row['Maintenance Start Date']).days, height = .3, left = row['Maintenance Start Date'])
    #align bars to left on maintenance start
    #width is difference in start vs end
    #y value is row number ie ship, must separate docking and maintenance so they don't overlap

    y = row['Maintenance Start Date']
    duration = (row['Maintenance End Date'] - row['Maintenance Start Date']).days
    ax.text(y, i+.2, f'Maintenance: {duration} days', va='center', ha='left', fontsize=8, color='black')

    ax.barh(y = i-.2, width = (row['Docking End Date'] - row['Docking Start Date']).days, height = .3, left = row['Docking Start Date'])

    #bar label
    y = row['Docking Start Date']
    duration = (row['Docking End Date'] - row['Docking Start Date']).days
    ax.text(y, i-.2, f'Docking: {duration} days', va='center', ha='left', fontsize=8, color='black')




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