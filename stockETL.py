import pandas as pd
import requests
import yfinance as yf
from datetime import datetime
from Scripts.awsConfig import upload_to_s3
import snowflake.connector
from Scripts.snowflakeConfig import load_csv_to_snowflake

SP500_URL = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

def get_sp500_tickers():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/141.0.0.0 Safari/537.36"
    }
    print("🔍 Fetching S&P 500 company tickers...")
    response = requests.get(SP500_URL, headers=headers)
    response.raise_for_status()
    tables = pd.read_html(response.text)
    tickers = tables[0]['Symbol'].tolist()
    print(f"✅ Total tickers found: {len(tickers)}")
    return tickers

def fetch_yfinance_data(symbols, start_date, end_date, interval):
    results = {}
    for symbol in symbols:
        try:
            print(f"📈 Fetching data for {symbol} ...")
            df = yf.download(
                tickers=symbol,
                start=start_date,
                end=end_date,
                interval=interval,
                progress=False,
                ignore_tz=True
            )
            if not df.empty:
                print(f"✅ Data received for {symbol}, rows: {len(df)}")
                results[symbol] = df
            else:
                print(f"⚠ No data for {symbol}")
        except Exception as e:
            print(f"❌ {symbol} fetch error: {e}")
    return results

def transform_data(df, symbol):
    df.columns = [col[0] if isinstance(col, tuple) else col for col in df.columns]
    df = df.reset_index()
    df["symbol"] = symbol
    df["close_change"] = df["Close"].diff().fillna(0)
    df["close_pct_change"] = df["Close"].pct_change().fillna(0) * 100
    return df[["Date", "Close", "High", "Low", "Open", "Volume", "symbol", "close_change", "close_pct_change"]]

if __name__ == "__main__":
    start_date = "2025-10-01"
    end_date = datetime.today().strftime("%Y-%m-%d")
    interval = "1d"

    print(f"\n🚀 Starting Data Extraction from {start_date} to {end_date}\n")

    tickers = get_sp500_tickers()

    # For testing, limit to 5 tickers (to run faster)
    sample_tickers = tickers[:5]
    print(f"\n🎯 Sample tickers: {sample_tickers}\n")

    data = fetch_yfinance_data(sample_tickers, start_date, end_date, interval)

    all_data = []
    for symbol, df in data.items():
        transformed_df = transform_data(df, symbol)
        all_data.append(transformed_df)
        print(f"🔄 Transformed data for {symbol} (rows: {len(transformed_df)})")

    if all_data:
        final_df = pd.concat(all_data)
        csv_file = "stock_data.csv"
        final_df.to_csv(csv_file, index=False)
        print(f"\n💾 Saved '{csv_file}' successfully (rows: {len(final_df)})")

          # Upload to AWS S3
        upload_to_s3(csv_file, f"sp500/{csv_file}")
        load_csv_to_snowflake(csv_file)

    else:
        print("⚠ No data fetched to save!")
