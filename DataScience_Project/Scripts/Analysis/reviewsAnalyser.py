import pandas as pd

# Input and output file names
input_csv_filename = "steamClean.csv"
recent_reviews_output_filename = "recent_reviews_per_game.csv"
all_reviews_output_filename = "all_reviews_per_game.csv"

# Read the input CSV file into a Pandas DataFrame
input_df = pd.read_csv(input_csv_filename)

# Convert the "Recent Reviews Summary" and "All Reviews Summary" columns to string
input_df["Recent Reviews Summary"] = input_df["Recent Reviews Summary"].astype(str)
input_df["All Reviews Summary"] = input_df["All Reviews Summary"].astype(str)

# Function to clean and normalize review names
def clean_normalize_reviews(review_str):
    review_str = review_str.lstrip('- ')
    return review_str

# Apply the cleaning and normalization function to both columns
input_df["Recent Reviews Summary"] = input_df["Recent Reviews Summary"].apply(clean_normalize_reviews)
input_df["All Reviews Summary"] = input_df["All Reviews Summary"].apply(clean_normalize_reviews)

# Create a DataFrame for recent reviews with reviews and occurrences for every game
recent_reviews_per_game_df = pd.DataFrame(columns=["Game", "Review", "Occurrences"])

# Create a DataFrame for all reviews with reviews and occurrences for every game
all_reviews_per_game_df = pd.DataFrame(columns=["Game", "Review", "Occurrences"])

# Iterate over each row in the input DataFrame
for index, row in input_df.iterrows():
    game_title = row["Title"]
    recent_reviews = row["Recent Reviews Summary"]
    all_reviews = row["All Reviews Summary"]

    # Split and clean recent reviews
    recent_reviews_list = [clean_normalize_reviews(review.strip()) for review in recent_reviews.split(',')]
    recent_reviews_occurrences = pd.Series(recent_reviews_list).value_counts().reset_index()
    recent_reviews_occurrences.columns = ["Review", "Occurrences"]
    recent_reviews_occurrences["Game"] = game_title
    recent_reviews_per_game_df = pd.concat([recent_reviews_per_game_df, recent_reviews_occurrences], ignore_index=True)

    # Split and clean all reviews
    all_reviews_list = [clean_normalize_reviews(review.strip()) for review in all_reviews.split(',')]
    all_reviews_occurrences = pd.Series(all_reviews_list).value_counts().reset_index()
    all_reviews_occurrences.columns = ["Review", "Occurrences"]
    all_reviews_occurrences["Game"] = game_title
    all_reviews_per_game_df = pd.concat([all_reviews_per_game_df, all_reviews_occurrences], ignore_index=True)

# Save the results to new CSV files
recent_reviews_per_game_df.to_csv(recent_reviews_output_filename, index=False)
all_reviews_per_game_df.to_csv(all_reviews_output_filename, index=False)

print(f"Recent reviews per game have been saved to {recent_reviews_output_filename}")
print(f"All reviews per game have been saved to {all_reviews_output_filename}")
