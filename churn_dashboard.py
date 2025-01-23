import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Database path
cleaned_db_path = "/mnt/c/Users/adrie/Documents/Projects Data/quantum/cleaned_customer_data.db"
plots_path = "/mnt/c/Users/adrie/Documents/Projects Data/quantum/plots"

# Step 1: Ensure the plots folder exists
if not os.path.exists(plots_path):
    os.makedirs(plots_path)
    print(f"Plots folder created at {plots_path}")
else:
    print(f"Plots folder already exists at {plots_path}")

# Step 2: Load data from the SQLite database
def load_data_from_db(table_name):
    """
    Load data from a specific table in the SQLite database.
    """
    try:
        connection = sqlite3.connect(cleaned_db_path)
        print(f"Connected to the database: {cleaned_db_path}")
        query = f"SELECT * FROM {table_name}"
        data = pd.read_sql(query, connection)
        connection.close()
        return data
    except sqlite3.Error as e:
        print(f"Error reading table {table_name}: {e}")
        return None

# Load training and testing data
training_data = load_data_from_db("cleaned_training_data")
testing_data = load_data_from_db("cleaned_testing_data")

# Ensure data was loaded
if training_data is None or testing_data is None:
    print("Failed to load data from the database. Exiting...")
    exit()

# Debug: Check for empty datasets
if training_data.empty:
    print("Training data is empty. Check your database.")
    exit()
if testing_data.empty:
    print("Testing data is empty. Check your database.")
    exit()

# Step 3: Generate and save plots
def generate_plots():
    """
    Generate and save key plots to the plots folder.
    """
    try:
        # Plot 1: Churn Distribution
        plt.figure(figsize=(8, 6))
        sns.countplot(x='Churn', data=training_data)
        plt.title('Churn Distribution')
        plt.savefig(f"{plots_path}/churn_distribution.png")
        plt.close()
        print("Saved churn_distribution.png")

        # Plot 2: Tenure vs. Churn
        plt.figure(figsize=(8, 6))
        sns.boxplot(x='Churn', y='Tenure', data=training_data)
        plt.title('Tenure vs. Churn')
        plt.savefig(f"{plots_path}/tenure_vs_churn.png")
        plt.close()
        print("Saved tenure_vs_churn.png")

        # Plot 3: Spending Per Month vs. Churn
        plt.figure(figsize=(8, 6))
        sns.boxplot(x='Churn', y='spending_per_month', data=training_data)
        plt.title('Spending Per Month vs. Churn')
        plt.savefig(f"{plots_path}/spending_per_month_vs_churn.png")
        plt.close()
        print("Saved spending_per_month_vs_churn.png")
    except Exception as e:
        print(f"Error generating plots: {e}")

# Call the function to generate and save plots
generate_plots()

print(f"All plots saved to {plots_path}")
