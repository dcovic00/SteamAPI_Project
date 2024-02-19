import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('review_summary.csv')

# Sorting the DataFrame by Occurrence Count in descending order
df_sorted = df.sort_values(by='Occurrence Count', ascending=False)

# Define colors for the bars
colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen', 'lightpink', 'lightsalmon', 'lightblue', 'lightgreen']

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(df_sorted['ReviewName'], df_sorted['Occurrence Count'], color=colors)
plt.xlabel('Review Name')
plt.ylabel('Occurrence Count')
plt.title('Occurrence of Different Review Names')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add gridlines for better readability
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()
