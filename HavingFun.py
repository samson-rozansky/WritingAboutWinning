import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# Load the dataset
data = pd.read_csv("TheDataWeCaveAbout.csv")

# Dictionary to store averaged values for each topic type
diction = dict()

# Initialize the dictionary for each topic
for index, row in data.iterrows():
    diction[row[1][:4]] = [0] * 20  # Assuming there are 20 topics in columns

# Populate dictionary with sums for each topic across rows
for index, row in data.iterrows():
    for i in range(20):
        diction[row[1][:4]][i] += row[2 + i]  # Offset by 2 to skip the first two columns

# Calculate average values for each topic
for key in diction:
    diction[key] = [value / 20 for value in diction[key]]  # Averaging over 20 topics

# Calculate the differences of each topic with "MATH"
math_values = diction.get("MATH", [])
differences = {key: [diction[key][i] - math_values[i] for i in range(len(math_values))] for key in diction if key != "MATH"}

# Convert dictionary to DataFrame for analysis
diff_df = pd.DataFrame(differences, index=[f"Topic {i+1}" for i in range(len(math_values))])

# Calculate absolute differences for sorting
diff_sums = diff_df.abs().sum(axis=0).sort_values()  # Sum of absolute differences across all topics

# Get the five topics closest to zero, ensuring "COMP" is included
closest_topics = diff_sums.head(5).index.tolist()
if 'COMP' not in closest_topics:
    closest_topics.append('COMP')

# Prepare data for plotting
plot_data = diff_df[closest_topics].mean()  # Averaging differences for each topic

# Plotting
colors = ['orange' if topic == 'COMP' else 'gray' for topic in closest_topics]
plt.figure(figsize=(10, 6))
plot_data.plot(kind='bar', color=colors)
plt.title("Difference of Topics Against MATH (Top 5 Closest to Zero)")
plt.ylabel("Average Difference")
plt.xlabel("Topics")
plt.show()
