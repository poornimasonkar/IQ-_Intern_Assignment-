# Task 1 — Revenue Analysis & Plot

## What this script does
- Reads revenue data from a Python dictionary
- Computes total of all Rev entries
- Maps Rev IDs to human-readable names
- Plots a bar chart and saves it as revenue_plot.png

## How to run

1. Install dependencies:
   pip install matplotlib

2. Run the script:
   python revenue.py

## Output
- Prints total revenue to terminal
- Opens a bar chart window
- Saves bar chart as revenue_plot.png

## Design Decisions
- Used startswith('Rev') to filter only revenue entries
- get_rev_name() function handles unknown IDs gracefully by returning 'Unknown'
- All values rounded to 3 decimal places using round()

## Effort Spent
Approximately 2 hours
