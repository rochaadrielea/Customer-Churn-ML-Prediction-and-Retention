# Tool Usage - Step-by-Step Instructions



### Create Virtual Environment:


python3 -m venv quantum_env
source quantum_env/bin/activate

### Install Dependencies:

pip install -r requirements.txt

** File Link** 
   - [requirements.txt](requirements.txt)

###  Process Kaggle Dataset
Download Dataset
python kaggle_customer_data.py

** File Link** 
   - [kaggle_customer_data.py](kaggle_customer_data.py)

unzip Kaggle Data
python unzip_dataset.py

** File Link** 
   - [unzip_dataset.py](unzip_dataset.py)

###  Familiarization of data and database creator


raw data to database SQLite
python excelRaw_to_sqlite.py

** File Link** 
   - [excelRaw_to_sqlite.py](excelRaw_to_sqlite.py)


Familiarization of raw data
python exploreDatabase_raw.sql


** File Link** 
   - [exploreDatabase_raw.sql](exploreDatabase_raw.sql)

###  Clean  Data

python data_cleaning_and_preparation.py

** File Link** 
   - [data_cleaning_and_preparation.py](data_cleaning_and_preparation.py)

Familiarization of clean data
python exploreDatabase_clean.sql


** File Link** 
   - [exploreDatabase_clean.sql](exploreDatabase_clean.sql)


###  logistic regression model

   Model Building
   python model_building_ml.py

** File Link** 
   - [model_building_ml.py](model_building_ml.py)

###  EDA

Exploratory Data Analysis
python Exploratory_Data_Analysis.py


** File Link** 
   - [Exploratory_Data_Analysis.py](Exploratory_Data_Analysis.py)

### IF YOU WANT VIZUALISE WITH PNG

Plot churn analyses 
    python churn_dashboard.py

** File Link** 
   - [churn_dashboard.py](churn_dashboard.py)

###  Visualization on server

python flask_dashboard.py

** File Link** 
   - [flask_dashboard.py](flask_dashboard.py)

