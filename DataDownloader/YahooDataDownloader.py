import yfinance as yf


class YahooDataDownloader:
    def __init__(self, data_type, start_date, end_date):
        self.dataType = data_type
        self.startDate = start_date
        self.endDate = end_date

    def __str__(self):
        return "Downloading and returning finacial data from Yahoo service"

    def download_yahoo_data(self):
        return yf.download(self.dataType, self.startDate, self.endDate)
