# Re-import data and re-create the diction dictionary to calculate MATH and COMP averages
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
data = pd.read_csv('normalizedData.csv')

# Initialize dictionary for each topic type
diction = dict()

# Step 1: Populate dictionary with sums for each topic across rows
for index, row in data.iterrows():
    topic_key = row[1][:4]  # Prefix, e.g., "COMP" or "MATH"
    if topic_key not in diction:
        diction[topic_key] = [0] * 20  # Initialize with 20 zeros if topic is new

    for i in range(20):
        diction[topic_key][i] += row[2 + i]  # Offset by 2 to skip first two columns

# Step 2: Calculate the average values per topic for the 20 columns
for key in diction:
    diction[key] = [value / 20 for value in diction[key]]

# Step 3: Extract "MATH" and "COMP" data, assuming the 20 columns represent categories
math_values = diction.get("MATH", [])
comp_values = diction.get("COMP", [])

# Extract category labels (from columns 2 to 22 in the original dataset)
categories = data.columns[2:22]

# Plotting the scatter plot with lines for MATH and COMP
if math_values and comp_values:
    plt.figure(figsize=(12, 6))
    plt.plot(categories, math_values, marker='o', color='blue', label='MATH',linestyle='none')
    plt.plot(categories, comp_values, marker='o', color='orange', label='COMP',linestyle='none')
    
    # Adding labels and title
    plt.xlabel("Categories")
    plt.ylabel("Normalized Amount of times it appears")
    plt.title("Comparison of MATH and COMP across Categories")
    plt.xticks(rotation=45, ha="right")
    plt.legend()
    
    # Display the plot
    plt.ylim(0, 1)
    plt.tight_layout()
    plt.show()
else:
    print("MATH or COMP data not found in the dataset.")
