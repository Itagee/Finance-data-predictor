import pandas as pd


class FeatureEngineeringCalculator:
    def __init__(self, data, period):
        self.data = pd.DataFrame(data)
        self.period = period

    def get_simple_moving_average_based_on_close_prices(self):
        return self.data['Close'].rolling(window=self.period).mean()

    def get_exponential_moving_average_based_on_close_prices(self):
        return self.data['Close'].ewm(span=self.period, adjust=False).mean()

    def calculate_rsi(self):
        pass

    def calculate_macd(self):
        pass

    def calculate_bollinger_bands(self):
        pass
