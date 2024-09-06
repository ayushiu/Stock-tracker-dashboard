import yfinance as yf
import matplotlib.pyplot as plt

# List of stocks
stocks = ['APPLe', 'GOOGle', 'MSFT']

# Download the data for the specified period (1 year)
data = yf.download(stocks, period='1y')

# Create subplots for each stock
fig, axs = plt.subplots(len(stocks), 1, figsize=(10, 6))

# Plot the closing prices of each stock
for i, stock in enumerate(stocks):
    axs[i].plot(data['Close'][stock])  # Access the 'Close' column for the specific stock
    axs[i].set_title(stock)
    axs[i].set_xlabel('Date')
    axs[i].set_ylabel('Price')

plt.tight_layout()  # Adjust layout for better spacing
plt.show()
