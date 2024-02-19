import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('gameFeatures_Analysis.csv')

# Sort the DataFrame by 'Friend Occurrences', 'All Occurrences', and 'Percentage' columns
df_sorted_friend = df.sort_values(by='Friend Occurrences', ascending=False)
df_sorted_all = df.sort_values(by='All Occurrences', ascending=False)
df_sorted_percentage = df.sort_values(by='Percentage', ascending=False)

# Plotting


# Plot for Friend Occurrences

plt.barh(df_sorted_friend['Game Feature'], df_sorted_friend['Friend Occurrences'], color='lightgreen')
plt.xlabel('Friend Occurrences', fontsize=12)  # Adjust label fontsize
plt.title('Friend Occurrences', fontsize=14)  # Adjust title fontsize

# Adjust layout
plt.tight_layout(pad=3)  # Add padding between subplots

# Show the plot
plt.show()

# Plotting
plt.figure(figsize=(8, 6))

# Plot for All Occurrences

plt.barh(df_sorted_all['Game Feature'], df_sorted_all['All Occurrences'], color='lightcoral')
plt.xlabel('All Occurrences', fontsize=12)  # Adjust label fontsize
plt.title('All Occurrences', fontsize=14)  # Adjust title fontsize

# Adjust layout
plt.tight_layout(pad=3)  # Add padding between subplots

# Show the plot
plt.show()
