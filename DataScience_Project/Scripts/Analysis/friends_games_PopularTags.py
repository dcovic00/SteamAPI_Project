import pandas as pd

# Read data from friends_games.csv and steamClean.csv
friends_games_df = pd.read_csv("friends_games.csv")
steam_clean_df = pd.read_csv("steamClean.csv")

# Drop rows with missing titles in steam_clean_df
steam_clean_df = steam_clean_df[pd.notna(steam_clean_df["Title"])]

# Initialize a dictionary to store the occurrences of Popular Tags for each game
tag_occurrences = {}

# Iterate over each game in friends_games.csv
for index, row in friends_games_df.iterrows():
    game_name = row["Game Name"]
    
    # Search for the corresponding game in steamClean.csv
    matched_game = steam_clean_df[steam_clean_df["Title"].str.contains(game_name, case=False)]
    
    # If a match is found
    if not matched_game.empty:
        # Extract Popular Tags for the matched game
        popular_tags = matched_game.iloc[0]["Popular Tags"]
        
        # Split the string representation of the list and remove unwanted characters
        tags_list = [tag.strip(" '[]") for tag in popular_tags.split(",")]
        
        # Count the occurrences of each Popular Tag
        for tag in tags_list:
            tag_occurrences[tag] = tag_occurrences.get(tag, 0) + 1

# Create a DataFrame from the tag_occurrences dictionary
tag_occurrences_df = pd.DataFrame(tag_occurrences.items(), columns=["Popular Tag", "Occurrences"])

# Save the DataFrame to a CSV file
tag_occurrences_df.to_csv("friends_games_PopularTags.csv", index=False)

print("Data saved to 'friends_games_PopularTags.csv'")
