-- database: c:/Users/adrie/Documents/Projects Data/quantum/customer_data.db
SELECT name FROM sqlite_master WHERE type='table';


SELECT * FROM training_data LIMIT 10;


SELECT * FROM testing_data LIMIT 10;


SELECT COUNT(*) AS total_rows FROM training_data;


SELECT COUNT(*) AS total_rows FROM testing_data;


SELECT DISTINCT Churn FROM testing_data;

PRAGMA table_info('training_data');

PRAGMA table_info('testing_data')


