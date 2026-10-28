import csv
import random
from datetime import datetime, timedelta
import os

output_file = "retail_big.csv"

target_size_mb = 520
target_size_bytes = target_size_mb * 1024 * 1024

categories = [
    "Electronics", "Fashion", "Grocery", "Home", "Beauty",
    "Sports", "Toys", "Books", "Furniture", "Automotive"
]

regions = [
    "London", "Manchester", "Birmingham", "Leeds", "Glasgow",
    "Liverpool", "Bristol", "Sheffield", "Cardiff", "Edinburgh"
]

payment_methods = [
    "Card", "Cash", "PayPal", "Bank Transfer", "Gift Card"
]

start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 12, 31)
date_range_days = (end_date - start_date).days

product_price_ranges = {
    "Electronics": (50, 1500),
    "Fashion": (10, 300),
    "Grocery": (1, 100),
    "Home": (20, 800),
    "Beauty": (5, 250),
    "Sports": (10, 600),
    "Toys": (5, 200),
    "Books": (3, 80),
    "Furniture": (100, 2000),
    "Automotive": (20, 1200)
}

with open(output_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow([
        "transaction_id",
        "customer_id",
        "product_id",
        "product_category",
        "quantity",
        "unit_price",
        "transaction_date",
        "store_id",
        "region",
        "payment_method",
        "discount"
    ])

    transaction_id = 1

    while os.path.getsize(output_file) < target_size_bytes:
        category = random.choice(categories)
        price_min, price_max = product_price_ranges[category]

        customer_id = f"CUST{random.randint(1, 250000):06d}"
        product_id = f"PROD{random.randint(1, 50000):05d}"
        quantity = random.randint(1, 10)
        unit_price = round(random.uniform(price_min, price_max), 2)
        random_date = start_date + timedelta(days=random.randint(0, date_range_days))
        store_id = f"STORE{random.randint(1, 500):04d}"
        region = random.choice(regions)
        payment_method = random.choice(payment_methods)
        discount = round(random.choice([0, 0.05, 0.10, 0.15, 0.20, 0.25]), 2)

        writer.writerow([
            f"TXN{transaction_id:09d}",
            customer_id,
            product_id,
            category,
            quantity,
            unit_price,
            random_date.strftime("%Y-%m-%d"),
            store_id,
            region,
            payment_method,
            discount
        ])

        transaction_id += 1

        if transaction_id % 500000 == 0:
            size_mb = os.path.getsize(output_file) / (1024 * 1024)
            print(f"Generated {transaction_id:,} rows | Size: {size_mb:.2f} MB")

final_size_mb = os.path.getsize(output_file) / (1024 * 1024)
print(f"Dataset created: {output_file}")
print(f"Final size: {final_size_mb:.2f} MB")
print(f"Total rows: {transaction_id - 1:,}")
import csv
import random
from datetime import datetime, timedelta
import os

output_file = "retail_big.csv"

target_size_mb = 520
target_size_bytes = target_size_mb * 1024 * 1024

categories = [
    "Electronics", "Fashion", "Grocery", "Home", "Beauty",
    "Sports", "Toys", "Books", "Furniture", "Automotive"
]

regions = [
    "London", "Manchester", "Birmingham", "Leeds", "Glasgow",
    "Liverpool", "Bristol", "Sheffield", "Cardiff", "Edinburgh"
]

payment_methods = [
    "Card", "Cash", "PayPal", "Bank Transfer", "Gift Card"
]

start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 12, 31)
date_range_days = (end_date - start_date).days

product_price_ranges = {
    "Electronics": (50, 1500),
    "Fashion": (10, 300),
    "Grocery": (1, 100),
    "Home": (20, 800),
    "Beauty": (5, 250),
    "Sports": (10, 600),
    "Toys": (5, 200),
    "Books": (3, 80),
    "Furniture": (100, 2000),
    "Automotive": (20, 1200)
}

with open(output_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow([
        "transaction_id",
        "customer_id",
        "product_id",
        "product_category",
        "quantity",
        "unit_price",
        "transaction_date",
        "store_id",
        "region",
        "payment_method",
        "discount"
    ])

    transaction_id = 1

    while os.path.getsize(output_file) < target_size_bytes:
        category = random.choice(categories)
        price_min, price_max = product_price_ranges[category]

        customer_id = f"CUST{random.randint(1, 250000):06d}"
        product_id = f"PROD{random.randint(1, 50000):05d}"
        quantity = random.randint(1, 10)
        unit_price = round(random.uniform(price_min, price_max), 2)
        random_date = start_date + timedelta(days=random.randint(0, date_range_days))
        store_id = f"STORE{random.randint(1, 500):04d}"
        region = random.choice(regions)
        payment_method = random.choice(payment_methods)
        discount = round(random.choice([0, 0.05, 0.10, 0.15, 0.20, 0.25]), 2)

        writer.writerow([
            f"TXN{transaction_id:09d}",
            customer_id,
            product_id,
            category,
            quantity,
            unit_price,
            random_date.strftime("%Y-%m-%d"),
            store_id,
            region,
            payment_method,
            discount
        ])

        transaction_id += 1

        if transaction_id % 500000 == 0:
            size_mb = os.path.getsize(output_file) / (1024 * 1024)
            print(f"Generated {transaction_id:,} rows | Size: {size_mb:.2f} MB")

final_size_mb = os.path.getsize(output_file) / (1024 * 1024)
print(f"Dataset created: {output_file}")
print(f"Final size: {final_size_mb:.2f} MB")
print(f"Total rows: {transaction_id - 1:,}")
