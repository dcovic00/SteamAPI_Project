import csv
from steam import Steam
from decouple import config
import matplotlib.pyplot as plt

KEY = config("STEAM_API_KEY")

steam = Steam(KEY)

# Read Steam IDs and usernames from steam_friends.csv
steam_ids = []
usernames = []

with open('steam_friends.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        steam_ids.append(row[0])
        usernames.append(row[1])

# Retrieve Steam levels and create a histogram
levels = []
for steam_id in steam_ids:
    try:
        user = steam.users.get_user_steam_level(steam_id)
        print(user)  # Print the user object to inspect its structure
        levels.append(user['player_level'])
    except KeyError as e:
        print(f"KeyError fetching data for {steam_id}: {e}. Skipping row.")

# Create a histogram of level occurrences
plt.hist(levels, bins=range(min(levels), max(levels) + 1), edgecolor='black')
plt.xlabel('Steam Level')
plt.ylabel('Number of Users')
plt.title('Distribution of Steam Levels')
plt.show()

# Write usernames and levels to friends_levels.csv
with open('steam_friends_levels.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Username', 'Steam Level'])
    for username, level in zip(usernames, levels):
        writer.writerow([username, level])
