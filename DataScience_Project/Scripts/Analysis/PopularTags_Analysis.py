import pandas as pd

# Read data from friend_games_GameFeautures.csv and gameFeautures.csv
friends_games_PopularTags_df = pd.read_csv("friends_games_PopularTags.csv")
popular_tags_df = pd.read_csv("popular_tags.csv")

# Initialize lists to store the analysis results
popular_tags = []
friend_game_popular_tags_occurrences = []
all_game_popular_tags_occurrences = []
percentages = []

# Iterate over each row in friend_games_GameFeautures.csv
for index, row in friends_games_PopularTags_df.iterrows():
    popular_tag = row["Popular Tag"]
    friend_occurrences = row["Occurrences"]
    
    # Search for the corresponding game feature in gameFeautures.csv
    matching_row = popular_tags_df[popular_tags_df["Popular Tag"] == popular_tag]
    
    # If a match is found, extract the occurrence count
    if not matching_row.empty:
        all_occurrences = matching_row.iloc[0]["Occurrence Count"]
        
        # Calculate the percentage of friend occurrences relative to all occurrences
        percentage = (friend_occurrences / all_occurrences)
        
        # Append the analysis results to the lists
        popular_tags.append(popular_tag)
        friend_game_popular_tags_occurrences.append(friend_occurrences)
        all_game_popular_tags_occurrences.append(all_occurrences)
        percentages.append(percentage)
    else:
        print(f"Pop Tag '{popular_tag}' not found in gameFeatures.csv")

# Create a DataFrame from the analysis results
analysis_df = pd.DataFrame({
    "Game Feature": popular_tags,
    "Friend Occurrences": friend_game_popular_tags_occurrences,
    "All Occurrences": all_game_popular_tags_occurrences,
    "Percentage": percentages
})

# Sort the DataFrame by the "Percentage" column in descending order
analysis_df = analysis_df.sort_values(by="Percentage", ascending=False)

# Save the sorted DataFrame to a CSV file
analysis_df.to_csv("popularTags_Analysis.csv", index=False)

print("Analysis saved to 'popularTags_Analysis.csv'")
