import pandas as pd
import yfinance as yf

ticker = 'NVDA'

ts = yf.download(
    ticker,
    start="2006-01-01",
    end="2026-01-01",
    interval="1d",
    auto_adjust=True
)

# Format
ts.columns = ts.columns.get_level_values(0)
ts.columns.name = None
ts = ts.reset_index()
ts = ts.rename(columns={
    'Date': 'date',
    'Open': 'open',
    'High': 'high',
    'Low': 'low',
    'Close': 'close',
    'Volume': 'volume'
})

ts = ts[['date', 'open', 'high', 'low', 'close', 'volume']]
ts['date'] = pd.to_datetime(ts['date'], format='%Y-%m-%d')
ts.to_csv(f'data/{ticker}_1d_ohlcv.csv', index=False)