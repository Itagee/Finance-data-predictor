import pandas as pd
class FeatureEngineeringCalculator:
    def __init__(self, data, period):
        self.data = pd.DataFrame(data)
        self.period = period

    def get_simple_moving_average_based_on_close_prices(self):
        self.data[f'SMA_{self.period}'] = self.data['Close'].rolling(window=self.period).mean()

    def get_exponential_moving_average_based_on_close_prices(self):
        self.data[f'EMA_{self.period}'] = self.data['Close'].ewm(span=self.period, adjust=False).mean()

    def get_average_gains(self):
        delta = self.data['Close'].diff()
        gain = delta.clip(lower=0)
        avg_gain = gain.rolling(window=self.period).mean()
        self.data[f'Average_Gain_{self.period}'] = avg_gain
        return avg_gain

    def get_average_losses(self):
        delta = self.data['Close'].diff()
        loss = delta.clip(upper=0)
        loss = loss.abs()
        avg_loss = loss.rolling(window=self.period).mean()
        self.data[f'Average_Loss_{self.period}'] = avg_loss
        return avg_loss

    def calculate_rsi(self):
        avg_gain = self.get_average_gains()
        avg_loss = self.get_average_losses()
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        self.data[f'RSI_{self.period}'] = rsi
        return rsi

    def calculate_macd(self):
        pass

    def calculate_bollinger_bands(self):
        pass



