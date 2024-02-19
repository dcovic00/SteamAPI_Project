import pandas as pd

# Read data from friend_games_GameFeautures.csv and gameFeautures.csv
friend_games_features_df = pd.read_csv("friends_games_GameFeatures.csv")
game_features_df = pd.read_csv("game_features.csv")

# Initialize lists to store the analysis results
game_features = []
friend_game_feature_occurrences = []
all_game_feature_occurrences = []
percentages = []

# Iterate over each row in friend_games_GameFeautures.csv
for index, row in friend_games_features_df.iterrows():
    game_feature = row["Game Feature"]
    friend_occurrences = row["Occurrences"]
    
    # Search for the corresponding game feature in gameFeautures.csv
    matching_row = game_features_df[game_features_df["Game Feature"] == game_feature]
    
    # If a match is found, extract the occurrence count
    if not matching_row.empty:
        all_occurrences = matching_row.iloc[0]["Occurrence Count"]
        
        # Calculate the percentage of friend occurrences relative to all occurrences
        percentage = (friend_occurrences / all_occurrences)
        
        # Append the analysis results to the lists
        game_features.append(game_feature)
        friend_game_feature_occurrences.append(friend_occurrences)
        all_game_feature_occurrences.append(all_occurrences)
        percentages.append(percentage)
    else:
        print(f"Game feature '{game_feature}' not found in gameFeatures.csv")

# Create a DataFrame from the analysis results
analysis_df = pd.DataFrame({
    "Game Feature": game_features,
    "Friend Occurrences": friend_game_feature_occurrences,
    "All Occurrences": all_game_feature_occurrences,
    "Percentage": percentages
})

# Sort the DataFrame by the "Percentage" column in descending order
analysis_df = analysis_df.sort_values(by="Percentage", ascending=False)

# Save the sorted DataFrame to a CSV file
analysis_df.to_csv("gameFeatures_Analysis.csv", index=False)

print("Analysis saved to 'gameFeatures_Analysis.csv'")
