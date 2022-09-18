# INF601 - Advanced Programing in Python
# Ryder Cook
# Mini Project 1

import os
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

# Five stocks
ticker_names = ["AAPL", "GOOGL", "BTC-USD", "TSLA", "META"]
# Collect data from last ten days
data = yf.download(tickers=ticker_names, start="2022-09-07", end="2022-09-17")


# Save plot as png in new folder
def new_direct(direct):
    # Only make folder if folder doesn't exists
    if not os.path.exists(direct):
        os.mkdir(direct)


# Get the closing prices from five stocks
def closing_prices(ticker):
    return [price for price in data['Adj Close'][ticker]]


# Draw the charts for five stocks and save to new folder
def draw_charts(tickers):
    chart_dir = "charts"
    new_direct(chart_dir)
    for ticker in tickers:
        ticker_price = np.array(closing_prices(ticker))
        plt.plot(ticker_price)
        # Fancy chart output
        plt.title(f"{ticker} Stock Price the Last 10 Days")
        plt.xlabel("Day")
        plt.ylabel("Price")
        # Save plot as png in new folder
        plt.savefig(os.path.join(chart_dir, f"{ticker}.png"))
        plt.close()


draw_charts(ticker_names)
