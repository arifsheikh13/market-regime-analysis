import yfinance as yf
import pandas as pd

# Define ticker and date range
ticker = "^NSEI"
start_date = "2015-01-01"
end_date = None  # None = latest available

# Download data from Yahoo Finance
df_raw = yf.download(
    ticker,
    start=start_date,
    end=end_date,
    progress=False
)

# IMPORTANT:
# - No column renaming
# - No index reset
# - No type conversion
# - No cleaning of any kind

# Save exactly as received
output_path = "data/raw/nifty_50_yfinance_raw.csv"
df_raw.to_csv(output_path)

print("Raw NIFTY 50 data saved successfully.")
