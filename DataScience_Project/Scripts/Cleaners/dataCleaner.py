import csv
from io import StringIO

# Input and output file names
input_csv_filename = "steam.csv"
output_csv_filename = "steamClean.csv"

# Desired categories to keep

desired_categories = ["Title",
                       "Original Price", "Discounted Price",
                       "Release Date",
                       "Recent Reviews Summary","All Reviews Summary",
                       "Recent Reviews Number", "All Reviews Number",
                       "Developer", "Publisher",
                       "Popular Tags", "Game Features"]



...
#desired_categories = ["Title", "Original Price", "Discounted Price", "Release Date", "Recent Reviews Summary",
#                      "All Reviews Summary", "Recent Reviews Number", "All Reviews Number", "Developer", "Publisher",
#                      "Supported Languages", "Popular Tags", "Game Features"]
...
# Read from the input CSV file
with open(input_csv_filename, newline="", encoding="utf-8") as input_csv:
    csv_reader = csv.reader(input_csv)
    
    # Extract the header
    header = next(csv_reader)
    
    # Find the indices of the desired categories
    indices = [header.index(category) for category in desired_categories]
    
    # Read and filter the data
    output_data = []
    for row in csv_reader:
        filtered_row = [row[index] for index in indices]
        output_data.append(filtered_row)

# Write the filtered data to the output CSV file
with open(output_csv_filename, "w", newline="", encoding="utf-8") as output_csv:
    csv_writer = csv.writer(output_csv)
    
    # Write the header
    csv_writer.writerow(desired_categories)
    
    # Write the filtered data
    csv_writer.writerows(output_data)

print(f"Filtered data has been saved to {output_csv_filename}")
