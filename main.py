import yfinance as yf

# the ticker class is used to access stock data based on ticker symbols in this case for 
# the S&P 500 index is is ^GSPC
sp500 = yf.Ticker("^GSPC")
