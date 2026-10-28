import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

print("Loading dataset...")

df = pd.read_csv("retail_big.csv")

print("Original rows:", len(df))

# Use sample for ML to avoid WSL freezing
if len(df) > 100000:
    df = df.sample(n=100000, random_state=42)

print("Rows used for ML:", len(df))

print("Preprocessing...")

df["transaction_date"] = pd.to_datetime(df["transaction_date"], errors="coerce")
df["month"] = df["transaction_date"].dt.month
df["revenue"] = df["quantity"] * df["unit_price"] * (1 - df["discount"])

df = df.dropna()

region_encoder = LabelEncoder()
category_encoder = LabelEncoder()

df["region_encoded"] = region_encoder.fit_transform(df["region"])
df["category_encoded"] = category_encoder.fit_transform(df["product_category"])

X = df[[
    "quantity",
    "unit_price",
    "discount",
    "month",
    "region_encoded",
    "category_encoded"
]]

y = df["revenue"]

print("Splitting data...")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training model...")

model = RandomForestRegressor(
    n_estimators=20,
    max_depth=12,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

print("Predicting...")

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
rmse = np.sqrt(mean_squared_error(y_test, predictions))
r2 = r2_score(y_test, predictions)

print("Machine Learning Results")
print("------------------------")
print("MAE:", round(mae, 2))
print("RMSE:", round(rmse, 2))
print("R2 Score:", round(r2, 4))

print("Creating charts...")

category_revenue = df.groupby("product_category")["revenue"].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
category_revenue.plot(kind="bar")
plt.title("Total Revenue by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("revenue_by_category.png")
plt.close()

monthly_revenue = df.groupby("month")["revenue"].sum()
plt.figure(figsize=(10, 6))
monthly_revenue.plot(kind="line", marker="o")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("monthly_revenue_trend.png")
plt.close()

region_revenue = df.groupby("region")["revenue"].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
region_revenue.plot(kind="bar")
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("revenue_by_region.png")
plt.close()

plt.figure(figsize=(8, 6))
plt.scatter(y_test, predictions, alpha=0.4)
plt.title("Actual vs Predicted Revenue")
plt.xlabel("Actual Revenue")
plt.ylabel("Predicted Revenue")
plt.tight_layout()
plt.savefig("actual_vs_predicted.png")
plt.close()

feature_importance = pd.Series(
    model.feature_importances_,
    index=X.columns
).sort_values(ascending=False)

plt.figure(figsize=(10, 6))
feature_importance.plot(kind="bar")
plt.title("Feature Importance in Revenue Prediction")
plt.xlabel("Feature")
plt.ylabel("Importance")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("feature_importance.png")
plt.close()

print("Charts saved successfully.")
