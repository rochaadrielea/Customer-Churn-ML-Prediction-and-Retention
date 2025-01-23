from flask import Flask, render_template
import sqlite3
import pandas as pd
import plotly.express as px
import plotly.io as pio

# Create Flask app
app = Flask(__name__)

# Database path
cleaned_db_path = "/mnt/c/Users/adrie/Documents/Projects Data/quantum/cleaned_customer_data.db"

def load_data(table_name):
    """
    Load data from SQLite database table.
    """
    connection = sqlite3.connect(cleaned_db_path)
    query = f"SELECT * FROM {table_name}"
    data = pd.read_sql(query, connection)
    connection.close()
    return data

@app.route('/')
def home():
    """
    Home route that displays the interactive plots.
    """
    # Load training data
    training_data = load_data("cleaned_training_data")

    # Plot 1: Churn Distribution
    fig1 = px.histogram(training_data, x="Churn", title="Churn Distribution")
    fig1.update_layout(bargap=0.2)
    churn_dist = pio.to_html(fig1, full_html=False)

    # Plot 2: Tenure vs. Churn
    fig2 = px.box(training_data, x="Churn", y="Tenure", title="Tenure vs. Churn")
    tenure_vs_churn = pio.to_html(fig2, full_html=False)

    # Plot 3: Spending Per Month vs. Churn
    fig3 = px.box(training_data, x="Churn", y="spending_per_month", title="Spending Per Month vs. Churn")
    spending_vs_churn = pio.to_html(fig3, full_html=False)

    # Render the template with plots
    return render_template("dashboard.html", churn_dist=churn_dist, tenure_vs_churn=tenure_vs_churn, spending_vs_churn=spending_vs_churn)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
