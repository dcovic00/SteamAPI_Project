import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv('steamClean.csv')

# Replace 'Free' with 0.00 in 'Original Price' and 'Discounted Price' columns
df['Original Price'] = df['Original Price'].replace('Free', '0.00')
df['Discounted Price'] = df['Discounted Price'].replace('Free', '0.00')

# Convert pricing columns to numeric
prices_columns = ['Original Price', 'Discounted Price']
for col in prices_columns:
    df[col] = pd.to_numeric(df[col].replace('[\$,]', '', regex=True).str.replace(',', ''), errors='coerce')

# Remove games with prices over $200.00
df = df[(df['Original Price'] <= 200.00) & (df['Discounted Price'] <= 200.00)]

# Plot occurrences of discounted prices
plt.figure(figsize=(12, 6))
sns.set(style="whitegrid")
sns.set_color_codes("pastel")

discounted_prices_df = df['Discounted Price'].dropna()

# Only show multiples of $10 on the X-axis
xticks = range(0, int(df['Discounted Price'].max()) + 10, 10)

sns.lineplot(x=discounted_prices_df.value_counts().sort_index().index, 
             y=discounted_prices_df.value_counts().sort_index().values, 
             color="skyblue")

plt.title('Occurrences of Discounted Prices in Steam Games (Up to $200.00)')
plt.xlabel('Discounted Prices ($)')
plt.ylabel('Occurrences')
plt.xticks(xticks)
plt.tight_layout()

# Save data to CSV for discounted prices
discounted_prices_data = pd.DataFrame({'Discounted Price': discounted_prices_df.value_counts().sort_index().index,
                                       'Occurrences': discounted_prices_df.value_counts().sort_index().values})
discounted_prices_data.to_csv('discounted_prices_data.csv', index=False)

# Display the plot
plt.show()

# Plot occurrences of original prices
plt.figure(figsize=(12, 6))
sns.set(style="whitegrid")
sns.set_color_codes("pastel")

original_prices_df = df['Original Price'].dropna()

# Only show multiples of $10 on the X-axis
xticks = range(0, int(df['Original Price'].max()) + 10, 10)

sns.lineplot(x=original_prices_df.value_counts().sort_index().index, 
             y=original_prices_df.value_counts().sort_index().values, 
             color="salmon")

plt.title('Occurrences of Original Prices in Steam Games (Up to $200.00)')
plt.xlabel('Original Prices ($)')
plt.ylabel('Occurrences')
plt.xticks(xticks)
plt.tight_layout()

# Save data to CSV for original prices
original_prices_data = pd.DataFrame({'Original Price': original_prices_df.value_counts().sort_index().index,
                                     'Occurrences': original_prices_df.value_counts().sort_index().values})
original_prices_data.to_csv('original_prices_data.csv', index=False)

# Display the plot
plt.show()
