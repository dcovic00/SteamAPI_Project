import csv
import matplotlib.pyplot as plt

# Read data from friends_games.csv
games_data = []

with open('friends_games.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        games_data.append({
            'AppID': row[0],
            'Game Name': row[1],
            'Total Playtime': int(row[2]),
            'Occurrences': int(row[3])
        })

# Sort data by occurrences and total playtime
games_data_sorted_occurrences = sorted(games_data, key=lambda x: x['Occurrences'], reverse=True)
games_data_sorted_playtime = sorted(games_data, key=lambda x: x['Total Playtime'], reverse=True)

# Write sorted data to CSV files
with open('friends_games_sortedByOccurrences.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    for row in games_data_sorted_occurrences:
        writer.writerow([row['AppID'], row['Game Name'], row['Total Playtime'], row['Occurrences']])

with open('friends_games_sortedByTotalPlaytime.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    for row in games_data_sorted_playtime:
        writer.writerow([row['AppID'], row['Game Name'], row['Total Playtime'], row['Occurrences']])

# Data visualization
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Bar chart for occurrences
ax1.bar(range(len(games_data_sorted_occurrences)), [game['Occurrences'] for game in games_data_sorted_occurrences], align='center')
ax1.set_xticks(range(0, len(games_data_sorted_occurrences), 10))
ax1.set_xticklabels([game['Game Name'] for game in games_data_sorted_occurrences[::10]], rotation=90)
ax1.set_ylabel('Occurrences')
ax1.set_title('Games Sorted by Occurrences')

# Bar chart for total playtime
ax2.bar(range(len(games_data_sorted_playtime)), [game['Total Playtime'] for game in games_data_sorted_playtime], align='center')
ax2.set_xticks(range(0, len(games_data_sorted_playtime), 10))
ax2.set_xticklabels([game['Game Name'] for game in games_data_sorted_playtime[::10]], rotation=90)
ax2.set_ylabel('Total Playtime')
ax2.set_title('Games Sorted by Total Playtime')

plt.tight_layout()
plt.show()
