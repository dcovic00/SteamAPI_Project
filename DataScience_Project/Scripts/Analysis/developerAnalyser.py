import csv
from collections import Counter

# Input and output file names
input_csv_filename = "steamClean.csv"
output_csv_filename = "developers.csv"

# Column to analyze
column_to_analyze = "Developer"

# Read from the input CSV file
with open(input_csv_filename, newline="", encoding="utf-8") as input_csv:
    csv_reader = csv.reader(input_csv)

    # Extract the header
    header = next(csv_reader)

    # Find the index of the column to analyze
    index = header.index(column_to_analyze)

    # Collect unique developers and their occurrence counts
    developers_counter = Counter()

    for row in csv_reader:
        developer = row[index]
        developers_counter[developer] += 1

# Write the unique developers and their occurrence counts to the output CSV file
with open(output_csv_filename, "w", newline="", encoding="utf-8") as output_csv:
    csv_writer = csv.writer(output_csv)

    # Write the header
    csv_writer.writerow(["Developer", "Occurrence Count"])

    # Write the data
    for developer, count in sorted(developers_counter.items(), key=lambda x: x[0], reverse=True):
        csv_writer.writerow([developer, count])

print(f"Developers summary has been saved to {output_csv_filename}")
