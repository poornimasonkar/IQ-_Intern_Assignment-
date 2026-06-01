# Task 3 — Office Commute Calculator

## What this script does
- Asks the user for name, card balance, wallet cash,
  meal cost, travel cost, working days and start date
- Calculates total travel cost and total meal cost
- Checks if card and wallet balances are sufficient
- Computes the end date of the office stint
- Prints a clear summary of all costs and balances

## How to run

1. Open terminal
2. Go to the task3 folder:
   cd task3-calculator
3. Run the script:
   python calculator.py
4. Enter values when prompted

## No installation needed
This script uses only Python standard library.
No pip install required.

## Input format
- Card, wallet, meals, travel : decimal numbers (e.g. 500.50)
- Days                        : whole number (e.g. 5)
- Start date                  : dd/mm/yyyy format (e.g. 02/06/2026)

## Output
- Prints a full summary in the terminal
- Shows warning if card or wallet balance is insufficient

## Design Decisions
- Used try/except to handle invalid number inputs
- Used datetime.strptime to validate date format
- Used timedelta(days - 1) for end date so that
  5 days starting Monday ends on Friday not Saturday
- Kept code simple and linear without functions
  for readability 

  ## Files
  - calculator.py   : main script
- sample_run.txt  : transcript of one complete run
- README.md       : this file
