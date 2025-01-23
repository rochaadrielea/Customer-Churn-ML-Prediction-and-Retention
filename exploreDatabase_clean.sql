-- database: c:/Users/adrie/Documents/Projects Data/quantum/cleaned_customer_data.db

SELECT name FROM sqlite_master WHERE type='table';


SELECT * FROM cleaned_training_data LIMIT 10;


SELECT * FROM cleaned_testing_data LIMIT 10;


SELECT COUNT(*) AS total_rows FROM cleaned_training_data;


SELECT COUNT(*) AS total_rows FROM cleaned_testing_data;


SELECT DISTINCT Churn FROM cleaned_testing_data;

PRAGMA table_info('cleaned_training_data');

PRAGMA table_info('cleaned_testing_data')
