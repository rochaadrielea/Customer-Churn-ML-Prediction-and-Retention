import sqlite3
import pandas as pd

# File paths
training_file = "customer_churn_dataset-training-master.csv"
testing_file = "customer_churn_dataset-testing-master.csv"

# SQLite database name
db_name = "customer_data.db"

# Connect to SQLite database
conn = sqlite3.connect(db_name)

# Load training dataset into SQLite
df_training = pd.read_csv(training_file)
df_training.to_sql("training_data", conn, if_exists="replace", index=False)

# Load testing dataset into SQLite
df_testing = pd.read_csv(testing_file)
df_testing.to_sql("testing_data", conn, if_exists="replace", index=False)

# Commit and close the connection
conn.commit()
conn.close()

print(f"Datasets loaded into {db_name}!")
