# INF601 - Advanced Programing in Python
# Ryder Cook
# Mini Project 1

import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

data = yf.download("AAPL", start="2022-09-04", end="2022-09-14")

aaplPrices = []

for price in data['Adj Close']:
    aaplPrices.append(price)

print(aaplPrices)

# Create a numpy array
aaplarray = np.array(aaplPrices)
# Create matplotlib graph
plt.plot(aaplarray)

# Save plot as png
plt.savefig('charts/aapl.png')

# Show graph
plt.show()