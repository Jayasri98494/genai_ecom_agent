import sqlite3
import pandas as pd

DB_PATH = "db/ecommerce.db"

def run_sql_query(query):
    try:
        conn = sqlite3.connect(DB_PATH)
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df.to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}
