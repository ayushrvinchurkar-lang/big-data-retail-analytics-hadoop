CREATE DATABASE IF NOT EXISTS retail_bda;
USE retail_bda;

CREATE EXTERNAL TABLE IF NOT EXISTS retail_transactions (
    transaction_id STRING,
    customer_id STRING,
    product_id STRING,
    product_category STRING,
    quantity INT,
    unit_price DOUBLE,
    transaction_date STRING,
    store_id STRING,
    region STRING,
    payment_method STRING,
    discount DOUBLE
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/retail/input'
TBLPROPERTIES ('skip.header.line.count'='1');

SHOW TABLES;
SELECT * FROM retail_transactions LIMIT 10;

SELECT
    product_category,
    ROUND(SUM(quantity * unit_price * (1 - discount)), 2) AS total_revenue
FROM retail_transactions
GROUP BY product_category
ORDER BY total_revenue DESC;

SELECT
    SUBSTR(transaction_date, 1, 7) AS sales_month,
    ROUND(SUM(quantity * unit_price * (1 - discount)), 2) AS monthly_revenue
FROM retail_transactions
GROUP BY SUBSTR(transaction_date, 1, 7)
ORDER BY sales_month;

SELECT
    region,
    COUNT(*) AS transaction_count,
    ROUND(SUM(quantity * unit_price * (1 - discount)), 2) AS regional_revenue
FROM retail_transactions
GROUP BY region
ORDER BY regional_revenue DESC;

SELECT
    customer_id,
    ROUND(SUM(quantity * unit_price * (1 - discount)), 2) AS customer_value
FROM retail_transactions
GROUP BY customer_id
ORDER BY customer_value DESC
LIMIT 10;
