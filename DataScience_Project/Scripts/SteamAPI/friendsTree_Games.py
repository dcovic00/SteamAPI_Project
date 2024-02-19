import csv
from steam import Steam
from decouple import config

KEY = config("STEAM_API_KEY")

steam = Steam(KEY)

# Read Steam IDs from steam_friends.csv
steam_ids = []

with open('steam_friends.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        steam_ids.append(row[0])

# Keep track of unique games and their occurrences
games_data = {}

# Iterate through all user IDs
for steam_id in steam_ids:
    try:
        user_games = steam.users.get_owned_games(steam_id)
        print(user_games)  # Print the user games object to inspect its structure

        # Iterate through the games and update the occurrences
        for game in user_games['games']:
            appid = game['appid']
            if appid in games_data:
                games_data[appid]['playtime_forever'] += game['playtime_forever']
                games_data[appid]['occurrences'] += 1
            else:
                games_data[appid] = {
                    'name': game['name'],
                    'playtime_forever': game['playtime_forever'],
                    'occurrences': 1
                }
    except Exception as e:
        print(f"Error fetching data for {steam_id}: {e}. Skipping.")

# Write games_data to friends_games.csv
with open('friends_games.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['AppID', 'Game Name', 'Total Playtime', 'Occurrences'])
    for appid, data in games_data.items():
        writer.writerow([appid, data['name'], data['playtime_forever'], data['occurrences']])
