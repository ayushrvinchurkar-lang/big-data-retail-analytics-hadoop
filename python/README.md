# Python Component

This folder contains Python scripts for the Big Data Retail Analytics project.

## Scripts

### 1. `generate_retail_dataset.py`

Generates synthetic retail transaction data for analysis.

The dataset includes:

* Transaction IDs
* Customer and product IDs
* Product categories
* Quantities and unit prices
* Transaction dates
* Store IDs and regions
* Payment methods and discounts

The script is configured to generate a dataset of approximately 520 MB.

### 2. `retail_ml.py`

Contains the machine-learning and visualization workflow for retail revenue analysis.

The script includes:

* Random Forest regression
* Model evaluation using MAE, RMSE, and R²
* Revenue analysis by product category
* Monthly revenue trends
* Revenue analysis by region
* Actual-versus-predicted revenue visualization
* Feature-importance visualization

## Requirements

The scripts use Python. The machine-learning workflow also requires compatible versions of its data-processing, machine-learning, and visualization libraries.

## Running the Scripts

Run these commands from your project directory:

```bash
python3 generate_retail_dataset.py
python3 retail_ml.py
```

**Important:** The dataset generator creates a large CSV file. Ensure sufficient disk space is available before running it.

Test the machine-learning script in your environment before relying on its results. The generated dataset and the original machine-learning outputs are not included in this repository.
