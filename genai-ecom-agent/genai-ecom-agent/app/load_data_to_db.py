import pandas as pd
import sqlite3
import os

os.makedirs("db", exist_ok=True)
conn = sqlite3.connect("db/ecommerce.db")

data_files = {
    "ad_sales_metrics": "data/ad_sales_metrics.csv",
    "total_sales_metrics": "data/total_sales_metrics.csv",
    "eligibility": "data/eligibility.csv"
}

for table, path in data_files.items():
    df = pd.read_csv(path)
    df.to_sql(table, conn, if_exists='replace', index=False)
    print(f"Loaded {table}")

conn.close()
