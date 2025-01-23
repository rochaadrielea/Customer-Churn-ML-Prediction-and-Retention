import sqlite3
import pandas as pd
from drop_un_colums import dropping_columns  # Step 1: Import the cleaning function

# Database paths
raw_db_path = "/mnt/c/Users/adrie/Documents/Projects Data/quantum/customer_data.db"
cleaned_db_path = "/mnt/c/Users/adrie/Documents/Projects Data/quantum/cleaned_customer_data.db"

# Step 1: Perform data cleaning using `dropping_columns`
try:
    training_data, testing_data = dropping_columns(raw_db_path)
    if training_data is None or testing_data is None:
        print("Data cleaning failed. Exiting...")
        exit()
except Exception as e:
    print(f"Error during data cleaning: {e}")
    exit()

# Step 2: Handle missing values
def handle_missing_values(data):
    """
    Handle missing values for both OBJECCT and numeric columns.
    """
    for column in data.columns:
        if data[column].dtype == 'object':  
            mode_value = data[column].mode()[0]
            data[column] = data[column].fillna(mode_value)
        else:  # Numeric
            mean_value = data[column].mean()
            data[column] = data[column].fillna(mean_value)
    return data

try:
    training_data = handle_missing_values(training_data)
    testing_data = handle_missing_values(testing_data)
    print("Missing values handled successfully.")
except Exception as e:
    print(f"Error handling missing values: {e}")
    exit()

# Step 3: One-hot encode categorical variables
categorical_columns = ['Gender', 'Subscription Type', 'Contract Length']  
try:
    training_data = pd.get_dummies(training_data, columns=categorical_columns, drop_first=True)
    testing_data = pd.get_dummies(testing_data, columns=categorical_columns, drop_first=True)
    print("Categorical variables one-hot encoded successfully.")
except Exception as e:
    print(f"Error during one-hot encoding: {e}")
    exit()

# Step 4: Feature Engineering
try:
    # Create spending_per_month feature
    training_data['spending_per_month'] = training_data['Total Spend'] / training_data['Tenure']
    testing_data['spending_per_month'] = testing_data['Total Spend'] / testing_data['Tenure']

    # Categorize Tenure
    def categorize_tenure(tenure):
        """
        Categorize tenure into 'New', 'Established', and 'Long-Term'.
        """
        if tenure <= 12:
            return 'New'
        elif tenure <= 36:
            return 'Established'
        else:
            return 'Long-Term'

    training_data['Tenure_Category'] = training_data['Tenure'].apply(categorize_tenure)
    testing_data['Tenure_Category'] = testing_data['Tenure'].apply(categorize_tenure)

    # One-hot encode Tenure_Category
    training_data = pd.get_dummies(training_data, columns=['Tenure_Category'], drop_first=True)
    testing_data = pd.get_dummies(testing_data, columns=['Tenure_Category'], drop_first=True)
    print("Feature engineering completed successfully.")
except Exception as e:
    print(f"Error during feature engineering: {e}")
    exit()

# Step 5: Ensure the Churn column is an integer
try:
    training_data['Churn'] = training_data['Churn'].astype(int)
    testing_data['Churn'] = testing_data['Churn'].astype(int)
    print("Churn column converted to integer successfully.")
except Exception as e:
    print(f"Error converting Churn column to integer: {e}")
    exit()

# Step 6: Save cleaned and feature-engineered data into a new database
try:
    connection_cleaned = sqlite3.connect(cleaned_db_path)
    print("Connected to the cleaned database successfully.")

    # Drop existing tables to avoid conflicts
    connection_cleaned.execute("DROP TABLE IF EXISTS cleaned_training_data")
    connection_cleaned.execute("DROP TABLE IF EXISTS cleaned_testing_data")

    # Save cleaned data
    training_data.to_sql("cleaned_training_data", connection_cleaned, if_exists="replace", index=False)
    testing_data.to_sql("cleaned_testing_data", connection_cleaned, if_exists="replace", index=False)
    print("Cleaned data saved to the new database.")
except Exception as e:
    print(f"Error saving cleaned data: {e}")
finally:
    if 'connection_cleaned' in locals():
        connection_cleaned.close()
    print("Cleaned database connection closed.")
