import pandas as pd

df = pd.read_csv("netflix_titles.csv")

print(df.head())

print(df.info())
# STEP 2: Handle Missing Values

df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')
df['country'] = df['country'].fillna('Unknown')
df['rating'] = df['rating'].fillna('Unknown')

print("\nMissing values after cleaning:\n")
print(df.isnull().sum())
# STEP 3: Convert date_added to datetime

df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# Create new column: year_added
df['year_added'] = df['date_added'].dt.year

print("\nDate column type after conversion:\n")
print(df[['date_added', 'year_added']].head())
# STEP 4: Split and normalize genres

df['listed_in'] = df['listed_in'].str.split(', ')

df = df.explode('listed_in')

print("\nGenres after splitting:\n")
print(df[['title', 'listed_in']].head(10))
# STEP 5: Split and normalize countries

df['country'] = df['country'].str.split(', ')

df = df.explode('country')

print("\nCountries after splitting:\n")
print(df[['title', 'country']].head(10))
# STEP 6: Clean and split duration column

df['duration'] = df['duration'].fillna('0 min')

df[['duration_value', 'duration_type']] = df['duration'].str.split(' ', expand=True)

print("\nDuration after cleaning:\n")
print(df[['title', 'duration', 'duration_value', 'duration_type']].head(10))
# STEP 7: Remove unnecessary columns

df.drop(columns=['description'], inplace=True)

# (optional) remove cast if not needed for dashboard
df.drop(columns=['cast'], inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Reset index
df.reset_index(drop=True, inplace=True)

print("\nFinal cleaned data info:\n")
print(df.info())
# STEP 8: Save cleaned dataset

df.to_csv("netflix_cleaned_data.csv", index=False)

print("\nCleaned data saved as netflix_cleaned_data.csv")
