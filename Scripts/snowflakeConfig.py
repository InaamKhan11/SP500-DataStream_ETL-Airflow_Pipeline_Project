import os
from dotenv import load_dotenv
import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas

load_dotenv()

def connect_snowflake():
    return snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA")
    )

def load_csv_to_snowflake(csv_path, table_name="STOCK_PRICES"):
    conn = connect_snowflake()
    cur = conn.cursor()

    # ✅ Read and clean CSV
    df = pd.read_csv(csv_path)
    df.columns = [c.strip().upper().replace(" ", "_").replace('"', '') for c in df.columns]
    df.rename(columns={"DATE": "TRADE_DATE"}, inplace=True)

    print("✅ Cleaned Columns:", df.columns)

    # ✅ Create or replace table in Snowflake
    create_table = f"""
    CREATE OR REPLACE TABLE {table_name} (
        TRADE_DATE DATE,
        CLOSE FLOAT,
        HIGH FLOAT,
        LOW FLOAT,
        OPEN FLOAT,
        VOLUME FLOAT,
        SYMBOL STRING,
        CLOSE_CHANGE FLOAT,
        CLOSE_PCT_CHANGE FLOAT
    )
    """
    cur.execute(create_table)

    # ✅ Upload DataFrame to Snowflake
    success, nchunks, nrows, _ = write_pandas(conn, df, table_name)
    if success:
        print(f"✅ {nrows} rows successfully loaded into Snowflake table '{table_name}'.")
    else:
        print("⚠ Upload failed.")

    cur.close()
    conn.close()
