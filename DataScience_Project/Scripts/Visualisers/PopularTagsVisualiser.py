import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('popularTags_Analysis.csv')

# Sort the DataFrame by 'Friend Occurrences' and 'All Occurrences' columns
df_sorted_friend = df.sort_values(by='Friend Occurrences', ascending=False)
df_sorted_all = df.sort_values(by='All Occurrences', ascending=False)

# Slice the DataFrame to keep only the top and bottom 10 values
df_top_bottom_friend = pd.concat([df_sorted_friend.head(10), df_sorted_friend.tail(10)])
df_top_bottom_all = pd.concat([df_sorted_all.head(10), df_sorted_all.tail(10)])

# Plotting for Friend Occurrences
plt.figure(figsize=(8, 6))
plt.barh(df_top_bottom_friend['Popular Tag'], df_top_bottom_friend['Friend Occurrences'], color='lightgreen')
plt.xlabel('Friend Occurrences', fontsize=8)
plt.ylabel('Popular Tag', fontsize=8)
plt.title('Friend Occurrences', fontsize=8)
plt.tight_layout(pad=3)
plt.show()

# Plotting for All Occurrences
plt.figure(figsize=(8, 6))
plt.barh(df_top_bottom_all['Popular Tag'], df_top_bottom_all['All Occurrences'], color='lightcoral')
plt.xlabel('All Occurrences', fontsize=8)
plt.ylabel('Popular Tag', fontsize=8)
plt.title('All Occurrences', fontsize=8)
plt.tight_layout(pad=3)
plt.show()
