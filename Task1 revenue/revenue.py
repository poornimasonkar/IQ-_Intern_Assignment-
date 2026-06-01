import matplotlib.pyplot as plt
# -------1. Source Data -----------------------
#Two seperate dictionaries- one hold the values, other one hold the names.

data = {
    'cash': 942.498,
    'todayCash': 9053.299,
    'Rev00016': 348.8300000005,
    'Rev00013': 31.99993,
    'Rev00015': 92.36,
    'Rev00017': 287.34,
    'Rev00020': 296.1,
    'Rev00018': 47.54,
    'Rev00045': 77.00,
}

revTypes ={
    'Rev00016': {'name': 'Petty cash', 'connectedTo': 'Physical'},
    'Rev00013': {'name': 'Debit card',  'connectedTo': 'HDFC'},
    'Rev00015': {'name': 'PhonePe',     'connectedTo': 'ICICI'},
    'Rev00017': {'name': 'Google pay',  'connectedTo': 'SBI'},
    'Rev00020': {'name': 'UPI',         'connectedTo': 'ICICI'},
    'Rev00018': {'name': 'Credit card', 'connectedTo': 'SBI'},
}

#-------2. Function: get_rev_name -----------------------
# This function takes a revenue type as input and returns the corresponding name from the revTypes dictionary.
# If the revenue type is not found in the dictionary, it returns 'Unknown'.

def get_rev_name(revId: str) -> str:
    entry = revTypes.get(revId)
    if entry:
        return entry['name'] # Access the 'name' field from the entry
    else:
        return 'Unknown' # Return 'Unknown' if the revId is not found in revTypes
    
#-------3. Filter: only rev keys -----------------------
# We only want to plot the revenue types, so we filter out the keys that start with 'Rev' from the data dictionary.    

rev_data = {
    key: value
    for key, value in data.items()
     if key.startswith('Rev')
     }

#-------4. Compute Total Revenue -----------------------

total = round(sum(rev_data.values()), 3)
print (f'Total Revenue: {total}')

#-------5. Resolve Names -----------------------

names = [get_rev_name(rev_id) for rev_id in rev_data.keys()]
values = [round(value, 3) for value in rev_data.values()]

print("\n Revenue ID-> Name mapping:")
for rev_id, name, value in zip(rev_data.keys(), names, values):
    print(f"{rev_id} -> {name}: {value}")

#-------6. Plotting -----------------------
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(names, values, color='steelblue',edgecolor='white', linewidth=0.8)

for bars, value in zip(bars, values):
    ax.text(
        bars.get_x() + bars.get_width() / 2,
         bars.get_height() + 3,
         f"{value:.3f}", ha='center', va='bottom', fontsize=9
         )
    
ax.set_xlabel('Revenue Type', fontsize=11)
ax.set_ylabel('Revenue Amount', fontsize=11)
ax.set_title('Revenue Breakdown by Type', fontsize=14, fontweight='bold')

plt.xticks(rotation=20, ha='right')
plt.tight_layout()
plt.savefig('revenue_plot.png', dpi=150)
plt.show()

print ("\nRevenue breakdown plot saved as 'revenue_plot.png'.")
