# YahooFinanceDownloader

The main purpose of this code is to download historical stock prices for multiple stocks at once. The output of this is a single Excel file containing stock prices. It is also capable of calculating returns of those stocks and export them into different Excel file.

What parameters you can choose:
- What stock prices you want to download. They are denoted by their abreviation in the stock market. Examples: GOOG, FB, AMZN, TSLA, etc.
- Starting and ending date.
- Frequency of the prices (daily, weekly, monthly). Daily by default.
- What prices you want (open, high,	low	close,	adj close,	volume)

The code is available both in a Jupyter notebook and in a Python scipt. For those less familiar with Python ecosystem, you can run the notebook in Google Colab without needing to install any additional dependencies on your local machine.

Possible future improvements:
- Adding graphical user interface
