import pandas as pd

class FeatureEngineeringCalculator:
    def __init__(self, data, peroid):
        self.data = pd.DataFrame(data)
        self.peroid = peroid

    def get_simple_moving_average_based_on_close_prices(self):
        return self.data['close'].rolling(window=self.peroid).mean()

    def get_exponential_moving_average_based_on_close_prices(self):
        return self.data['close'].ewm(span=self.peroid, adjust=False).mean()

    def calculate_rsi(self):
         pass

    def calculate_macd(self):
        pass

    def calculate_bollinger_bands(self):
        pass