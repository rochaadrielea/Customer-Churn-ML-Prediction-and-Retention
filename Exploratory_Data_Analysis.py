import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Step 1: Set up the plots folder
plots_folder = "/mnt/c/Users/adrie/Documents/Projects Data/quantum/eda_plots"
if not os.path.exists(plots_folder):
    os.makedirs(plots_folder)  # Create folder if it doesn't exist

# Step 2: Connect to the cleaned database
cleaned_db_path = "/mnt/c/Users/adrie/Documents/Projects Data/quantum/cleaned_customer_data.db"

try:
    connection = sqlite3.connect(cleaned_db_path)
    print("Connected to the cleaned database successfully.")
except sqlite3.Error as e:
    print(f"Error connecting to the database: {e}")
    exit()

# Step 3: Load data from the cleaned_training_data table
try:
    training_data = pd.read_sql("SELECT * FROM cleaned_training_data", connection)
    print("Loaded cleaned training data successfully.")
except Exception as e:
    print(f"Error loading training data: {e}")
    connection.close()
    exit()

# Step 4: Visualize and Save Plots
# 4.1 Churn Distribution
sns.countplot(x='Churn', data=training_data)
plt.title("Churn Distribution")
plt.savefig(os.path.join(plots_folder, "churn_distribution.png"))
plt.close()  # Close the plot to avoid overwriting

# 4.2 Tenure vs. Churn
sns.boxplot(x='Churn', y='Tenure', data=training_data)
plt.title("Tenure vs. Churn")
plt.savefig(os.path.join(plots_folder, "tenure_vs_churn.png"))
plt.close()

# 4.3 Monthly Charges vs. Churn
if 'MonthlyCharges' in training_data.columns:
    sns.boxplot(x='Churn', y='MonthlyCharges', data=training_data)
    plt.title("Monthly Charges vs. Churn")
    plt.savefig(os.path.join(plots_folder, "monthly_charges_vs_churn.png"))
    plt.close()

# 4.4 Contract Type vs. Churn
contract_columns = [col for col in training_data.columns if "Contract Length" in col]
if contract_columns:
    melted_data = training_data.melt(
        id_vars=['Churn'], value_vars=contract_columns,
        var_name='Contract Type', value_name='Value'
    )
    sns.countplot(x='Contract Type', hue='Churn', data=melted_data)
    plt.title("Contract Type vs. Churn")
    plt.savefig(os.path.join(plots_folder, "contract_type_vs_churn.png"))
    plt.close()

# Step 5: Document insights
print("""
Plots have been saved to the following folder:
{}
""".format(plots_folder))

# Close database connection
connection.close()
print("Database connection closed.")
