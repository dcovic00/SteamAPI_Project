import pandas as pd

# Read data from friends_games.csv and steamClean.csv
friends_games_df = pd.read_csv("friends_games.csv")
steam_clean_df = pd.read_csv("steamClean.csv")

# Drop rows with missing titles in steam_clean_df
steam_clean_df = steam_clean_df[pd.notna(steam_clean_df["Title"])]

# Initialize a dictionary to store the occurrences of Game Features for each game
features_occurrences = {}

# Iterate over each game in friends_games.csv
for index, row in friends_games_df.iterrows():
    game_name = row["Game Name"]
    
    # Search for the corresponding game in steamClean.csv
    matched_game = steam_clean_df[steam_clean_df["Title"].str.contains(game_name, case=False)]
    
    # If a match is found
    if not matched_game.empty:
        # Extract Game Features for the matched game
        game_features = matched_game.iloc[0]["Game Features"]
        
        # Split the string representation of the list and remove unwanted characters
        features_list = [feature.strip(" '[]") for feature in game_features.split(",")]
        
        # Count the occurrences of each Game Feature
        for feature in features_list:
            features_occurrences[feature] = features_occurrences.get(feature, 0) + 1

# Create a DataFrame from the features_occurrences dictionary
features_occurrences_df = pd.DataFrame(features_occurrences.items(), columns=["Game Feature", "Occurrences"])

# Save the DataFrame to a CSV file
features_occurrences_df.to_csv("friends_games_GameFeatures.csv", index=False)

print("Data saved to 'friends_games_GameFeatures.csv'")
