# Gantt Chart Project

A modular Python project for visualizing ship maintenance and docking schedules for the U.S. Navy as an interactive Gantt chart.

## File Structure

ganttchart/

├── data/

│ └── Gantt_Chart_Data_Set.xlsx # Raw Excel dataset

├── src/

│ ├── aesthetics.py # Color maps and style settings

│ ├── chart.py # Entry point: ties loader, transformer, plotter together

│ ├── data_loader.py # Loads Excel data into DataFrame

│ ├── plotter.py # Modular plotting functions (Matplotlib)

│ ├── transformers.py # Cleans, sorts, and adds duration

│ └── utils.py # Brief statistical analysis

├── .gitignore # Ignored files (Excel data, venv, **pycache**)

├── README.md # Project overview and instructions

└── requirements.txt # Python dependencies

## What the Code Does

Data Loading: data_loader.py reads the Excel file into a Pandas DataFrame and parses dates.

Transformation: transformers.py sorts by docking start date, resets the index, and computes maintenance/docking durations.

Aesthetics: aesthetics.py provides a function to generate evenly spaced colors for each ship and any default style settings for axes, titles, ect...

Plotting: plotter.py defines reusable functions to draw phased bars, annotate durations, toggle endpoints, and add a "today" line.

Entry Point: chart.py orchestrates the workflow: load → transform → plot → save or show.

## Running Code

### Dependencies / Requirements

Python 3.8+

pandas

numpy

matplotlib

### Install via:

pip install -r requirements.txt

### Installation & Usage

1. Clone the repository

git clone https://github.com/CharlieVeronee/ganttchart.git
cd ganttchart

2. Create virtual environment

python -m venv venv

source venv/bin/activate # on macOS/Linux

venv\Scripts\activate # on Windows

3. Install dependencies

pip install -r requirements.txt

4. Place the Excel file in the `data/` folder (filename: `Gantt_Chart_Data_Set.xlsx`).

5. Run the script

python3 src/chart.py

The script will display the Gantt chart and save an image (gantt_chart.png) + stats (gantt_stats.csv) in the project root.

## Workflow & Improvements

Exploration: I prototyped data transformations and various chart ideas and aesthetics.

Modularization: Functions are grouped by concern (loading, transforming, styling, plotting) to facilitate testing and future extension.

Additional Features: Line that displays current date, automatic color picking for most ideal color set, creation of statistics, exportation of images and stats, toggle to turn on and off endpoint dates

## Future Enhancements:

Integrate adjustText to avoid label collisions automatically.

Add Plotly functionality and interactivity.

## Approach, Challenges & Design Decisions

I chose a modular architecture to separate data handling from visualization, making it easy to test and swap out components. In the workflow, parsing and cleaning happen first. The color‐mapping and axis‐formatting live in dedicated modules to allow theme changes without touching core logic.

One challenge was balancing label legibility with chart density: narrow intervals could cause start/end labels to overlap. I addressed this by allowing toggles for endpoint annotations, introducing padded offsets, and planning for label‐adjustment libraries. Additionally, I had to plan the best way to separate out code for modularity and easy readability.
