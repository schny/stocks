import yfinance as yf

df = yf.download("AAPL", period="5y", interval="1d")
df.to_csv("AAPL_5years.csv")