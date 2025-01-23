import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Step 1: Load the cleaned data from the SQLite database
cleaned_db_path = "/mnt/c/Users/adrie/Documents/Projects Data/quantum/cleaned_customer_data.db"

try:
    connection = sqlite3.connect(cleaned_db_path)
    print("Connected to the cleaned database successfully.")
    training_data = pd.read_sql("SELECT * FROM cleaned_training_data", connection)
    print("Loaded cleaned training data.")
except sqlite3.Error as e:
    print(f"Error: {e}")
    exit()
finally:
    connection.close()

# Step 2: Prepare the data for machine learning
# Features (X) = everything except the "Churn" column (the answer we want to predict)
X = training_data.drop('Churn', axis=1)

# Target (y) = the "Churn" column (what we want to predict)
y = training_data['Churn']

# Step 3: Check for non-numeric columns and one-hot encode them
non_numeric_columns = X.select_dtypes(include=['object']).columns
print(f"Non-numeric columns: {non_numeric_columns}")

# Convert non-numeric columns into numeric using pd.get_dummies
X = pd.get_dummies(X, columns=non_numeric_columns, drop_first=True)

# Step 4: Split the data into training and testing sets
# 80% of the data is used to train the model, 20% is used to test it
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Training data size: {X_train.shape[0]} rows")
print(f"Testing data size: {X_test.shape[0]} rows")

# Step 5: Build and train a Logistic Regression model
model = LogisticRegression(max_iter=1000)  # Increase iterations for large datasets
model.fit(X_train, y_train)  # Train the model on the training data

print("Model training complete.")

# Step 6: Test the model on the testing data
predictions = model.predict(X_test)  # Predict churn for the testing data
accuracy = accuracy_score(y_test, predictions)  # Calculate accuracy
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Step 7: Evaluate the model
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

print("\nClassification Report:")
print(classification_report(y_test, predictions))
