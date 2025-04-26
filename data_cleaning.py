import pandas as pd

# Creating a sample dataset
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda', None],
    'Age': [28, 22, 34, None, 29],
    'City': ['New York', 'Paris', None, 'London', 'Tokyo']
}

# Create DataFrame
df = pd.DataFrame(data)

# Display original data
print("Original Data:")
print(df)

# Data Cleaning
# Fill missing values
df['Name'].fillna('Unknown', inplace=True)
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['City'].fillna('Unknown', inplace=True)

# Display cleaned data
print("\nCleaned Data:")
print(df)
