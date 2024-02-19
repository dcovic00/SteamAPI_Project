import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('friends_games.csv')

# Sort by occurrences
df_sorted_by_occurrences = df.sort_values(by='Occurrences', ascending=False)
top_20_occurrences = df_sorted_by_occurrences.head(20)

# Plotting occurrences
plt.figure(figsize=(10, 6))
plt.barh(top_20_occurrences['Game Name'], top_20_occurrences['Occurrences'], color='skyblue')
plt.xlabel('Occurrences')
plt.ylabel('Game Name')
plt.title('Top 20 Games by Occurrences')
plt.gca().invert_yaxis()  # Invert y-axis to display most frequent game at the top
plt.tight_layout()
plt.show()

# Sort by total playtime
df_sorted_by_playtime = df.sort_values(by='Total Playtime', ascending=False)
top_20_playtime = df_sorted_by_playtime.head(20)

# Plotting playtime
plt.figure(figsize=(10, 6))
plt.barh(top_20_playtime['Game Name'], top_20_playtime['Total Playtime'], color='lightgreen')
plt.xlabel('Total Playtime')
plt.ylabel('Game Name')
plt.title('Top 20 Games by Total Playtime')
plt.gca().invert_yaxis()  # Invert y-axis to display game with highest playtime at the top
plt.tight_layout()
plt.show()
