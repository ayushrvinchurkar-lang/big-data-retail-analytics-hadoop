-- Starter Hive queries for the retail analytics project.
-- Based on the report's described analyses; verify the schema before running.
-- The report's original source files were not supplied, so this is not claimed
-- to be the exact original script.
--
-- IMPORTANT:
-- 1. Confirm the CSV column names/order and delimiter.
-- 2. Confirm whether discount is stored as a fraction (e.g. 0.10) or percent.
-- 3. Confirm transaction_date format.
-- 4. Adjust this schema and revenue formula if your dataset differs.

CREATE DATABASE IF NOT EXISTS retail_bda;
USE retail_bda;

-- Starter schema: update fields/types to match the actual CSV.
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

-- Inspect table and sample rows after confirming schema.
SHOW TABLES;
SELECT * FROM retail_transactions LIMIT 10;

-- Revenue by product category.
SELECT
    product_category,
    ROUND(SUM(quantity * unit_price * (1 - discount)), 2) AS total_revenue
FROM retail_transactions
GROUP BY product_category
ORDER BY total_revenue DESC;

-- Monthly revenue (assumes transaction_date begins with YYYY-MM).
SELECT
    SUBSTR(transaction_date, 1, 7) AS sales_month,
    ROUND(SUM(quantity * unit_price * (1 - discount)), 2) AS monthly_revenue
FROM retail_transactions
GROUP BY SUBSTR(transaction_date, 1, 7)
ORDER BY sales_month;

-- Revenue by region.
SELECT
    region,
    COUNT(*) AS transaction_count,
    ROUND(SUM(quantity * unit_price * (1 - discount)), 2) AS regional_revenue
FROM retail_transactions
GROUP BY region
ORDER BY regional_revenue DESC;

-- Top 10 customers by calculated transaction revenue.
SELECT
    customer_id,
    ROUND(SUM(quantity * unit_price * (1 - discount)), 2) AS customer_value
FROM retail_transactions
GROUP BY customer_id
ORDER BY customer_value DESC
LIMIT 10;
