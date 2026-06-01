#Task 3 office Commuter Calculator

from datetime import datetime, timedelta
from tracemalloc import start  # timedelta lets add days to a date

# Step 1 — Collect all inputs

n = name = input(" Enter your name ")
c = card = float(input("Enter your card balance:"))
w = wallet = float(input("Enter your wallet balance:"))
m = meals = float(input("Enter the cost of one meal:"))
t = travel = float(input("Enter  one-way travel cost:"))
d = days = int(input("Enter the number of working days: "))
start_date = input("Enter the start date (DD/MM/YYYY): ")

# Step 2 — Validate inputs with try/except
try:
    c = card 
    w = wallet
    m = meals 
    t = travel
    d = days

    if days <=0:
        print ("Error: Days must be a positive integer.")

except ValueError:
    print("Invalid input. Please enter a valid number.")

   # Step 3 — Validate the date input
try:
    start = datetime.strptime(start_date, "%d/%m/%Y")
    end_date = start + timedelta(days=days-1)
    end_date_str = end_date.strftime("%d/%m/%Y")

except ValueError:
    print("Error: Date must be in dd/mm/yyyy format!")

# Step 4 — Calculate total costs
total_meals= m * d
total_travel = t * d 
total_meals= round(total_meals, 2)  # Round to 2 decimal places
total_travel = round(total_travel, 2)  # Round to 2 decimal places

# Step 5 — Calculate remaining balances

remaining_card = card - total_travel
remaining_wallet = wallet - total_meals

remaining_card = round(remaining_card, 2)
remaining_wallet = round(remaining_wallet, 2)

# Step 6 — Check if money is enough

if card < total_travel:
    shortfall = round(total_travel - card, 2)
    print(f"Card balance is short by {shortfall}!")

if wallet < total_meals:
    shortfall = round(total_meals - wallet, 2)
    print(f"Wallet cash is short by {shortfall}!")

    # Step 7 — Calculate end date

    end_date = start + timedelta(days = days - 1)
    end_date_str = end_date.strftime("%Y/%m/%d")

    # Step 8 — Output results


print(f"   Summary for {name}")
print("\n")
print(f"Daily travel cost  : Rs. {travel}")
print(f"Daily meal cost    : Rs. {meals}")
print(f"Total travel cost  : Rs. {total_travel}")
print(f"Total meal cost    : Rs. {total_meals}")
print(f"Remaining card     : Rs. {remaining_card}")
print(f"Remaining wallet   : Rs. {remaining_wallet}")
print(f"Office start date  : {start_date}")
print(f"Office end date    : {end_date_str}")
print("===========================")

