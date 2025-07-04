import pandas as pd


csv_url = "https://example.com/yourfile.csv"

try:
    df = pd.read_csv(csv_url)
    print(df)
except Exception as e:
    print(f"Error reading the CSV file: {e}")
