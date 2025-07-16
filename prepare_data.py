import pandas as pd

# Load the dataset
df = pd.read_csv('phishing_site_urls.csv')

# Show initial shape and columns
print("Initial shape:", df.shape)
print("Columns:", df.columns)

# Rename columns if necessary
df.columns = ['label', 'url']  # Adjust if columns are in different order

# Convert label to binary (1 = phishing, 0 = legitimate)
df['label'] = df['label'].apply(lambda x: 1 if x.lower() == 'phishing' else 0)

# Remove duplicates and missing values
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

# Show cleaned shape
print("After cleaning:", df.shape)

# Save cleaned data
df.to_csv('cleaned_data.csv', index=False)
print("Cleaned data saved to cleaned_data.csv")
