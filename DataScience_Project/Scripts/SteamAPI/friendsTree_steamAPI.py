import csv
from steam import Steam
from decouple import config

KEY = config("STEAM_API_KEY")

steam = Steam(KEY)

def get_friends_recursive(steam_id, depth=1, max_depth=4):
    if depth > max_depth:
        return
    
    friends = steam.users.get_user_friends_list(steam_id)
    
    for friend in friends['friends']:
        print(f"Friend at depth {depth}: {friend['personaname']} ({friend['steamid']})")
        
        # Write Steam ID and username to CSV file
        with open('steam_friends.csv', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([friend['steamid'], friend['personaname']])
        
        get_friends_recursive(friend['steamid'], depth + 1, max_depth)

# Example usage with the initial Steam ID
initial_steam_id = "76561198017933491"
get_friends_recursive(initial_steam_id)
