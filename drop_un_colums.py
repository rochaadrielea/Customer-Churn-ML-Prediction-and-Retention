import sqlite3
import pandas as pd

def dropping_columns(raw_db_path):
    """
    Connects to the raw database, drops unnecessary columns, and returns cleaned training and testing data.
    Args:
        raw_db_path (str): Path to the SQLite database.
    Returns:
        pd.DataFrame, pd.DataFrame: Cleaned training_data and testing_data.
    """
    try:
        # Step 1: Connect to the raw database
        connection_raw = sqlite3.connect(raw_db_path)
        print("Connected to the raw database successfully.")

        # Step 2: Load data from both tables
        training_data = pd.read_sql("SELECT * FROM training_data", connection_raw)
        testing_data = pd.read_sql("SELECT * FROM testing_data", connection_raw)
        print("Data loaded successfully from the raw database.")

    except Exception as e:
        print(f"Error loading data: {e}")
        return None, None
    finally:
        connection_raw.close()
        print("Raw database connection closed.")

    # Step 3: Perform data cleaning (e.g., drop CustomerID)
    try:
        if 'CustomerID' in training_data.columns:
            training_data.drop(columns=['CustomerID'], inplace=True)
        if 'CustomerID' in testing_data.columns:
            testing_data.drop(columns=['CustomerID'], inplace=True)
        print("Data cleaning completed.")
    except Exception as e:
        print(f"Error during data cleaning: {e}")
        return None, None

    # Return cleaned data
    return training_data, testing_data
