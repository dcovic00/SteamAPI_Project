import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('steam_friends_levels.csv')

# Sort the DataFrame by 'Steam Level' column in descending order
df_sorted = df.sort_values(by='Steam Level', ascending=False)

# Select only the top 20 values
top_30 = df_sorted.head(30)

# Plotting
plt.figure(figsize=(10, 6))
plt.barh(top_30['Username'], top_30['Steam Level'], color='skyblue')
plt.xlabel('Steam Level')
plt.ylabel('Username')
plt.title('Top 20 Steam Levels of Users')
plt.gca().invert_yaxis()  # Invert y-axis to display highest level at the top
plt.show()
