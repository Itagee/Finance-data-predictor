import unittest
import pandas as pd
from DataCalculator.FeatureEngineeringCalculator import (
    FeatureEngineeringCalculator
)


class TestFeatureEngineeringCalculator(unittest.TestCase):
    def setUp(self):
        self.data = {
            'Date': pd.date_range(start='2023-01-01', end='2023-01-12', freq='B'),
            'Open': [150, 152, 151, 149, 148, 145, 146, 148, 149],
            'High': [155, 157, 156, 154, 153, 150, 151, 153, 152],
            'Low': [148, 150, 149, 147, 146, 143, 144, 146, 145],
            'Close': [153, 154, 152, 151, 150, 148, 149, 151, 150],
            'Adj Close': [153, 154, 152, 151, 150, 148, 149, 151, 150],
            'Volume': [1000000, 1200000, 1100000, 1300000,
                       1400000, 1250000, 1300000, 1400000, 1350000]
        }
        self.calculator = FeatureEngineeringCalculator(data=self.data, period=5)

    def test_when_period_is_5_days_then_4_nan_is_returned_sma(self):
        self.calculator.get_simple_moving_average_based_on_close_prices()
        sma = self.calculator.data[f'SMA_{self.calculator.period}']
        for i in range(4):
            self.assertTrue(pd.isna(sma[i]),
                            f"Expected NaN at index {i}, "
                            f"but got {sma[i]}")

    def test_when_period_is_5_days_then_sma_values_are_returned(self):
        self.calculator.get_simple_moving_average_based_on_close_prices()
        sma = self.calculator.data[f'SMA_{self.calculator.period}']
        self.assertEqual(sma[4], 152.0)
        self.assertEqual(sma[5], 151.0)
        self.assertEqual(sma[6], 150.0)
        self.assertEqual(sma[7], 149.8)
        self.assertEqual(sma[8], 149.6)
        self.assertEqual(len(sma), len(self.data['Close']))
        self.assertFalse(sma[4:].isna().any())

    def test_when_period_is_5_days_then_5_nan_is_returned_gains(self):
        self.calculator.get_average_gains()
        average_gains = self.calculator.data[f'Average_Gain_{self.calculator.period}']
        for i in range(5):
            self.assertTrue(pd.isna(average_gains[i]),
                            f"Expected NaN at index {i}, "
                            f"but got {average_gains[i]}")

    def test_when_period_is_5_days_then_gains_values_are_returned(self):
        self.calculator.get_average_gains()
        average_gains = self.calculator.data[f'Average_Gain_{self.calculator.period}']
        self.assertEqual(average_gains[5], 0.2)
        self.assertEqual(average_gains[6], 0.2)
        self.assertEqual(average_gains[7], 0.6)
        self.assertEqual(average_gains[8], 0.6)
        self.assertFalse(average_gains[5:].isna().any())

    def test_when_period_is_5_days_then_5_nan_is_returned_loss(self):
        self.calculator.get_average_losses()
        average_loss = self.calculator.data[f'Average_Loss_{self.calculator.period}']
        for i in range(5):
            self.assertTrue(pd.isna(average_loss[i]),
                            f"Expected NaN at index {i}, "
                            f"but got {average_loss[i]}")

    def test_when_period_is_5_days_then_loss_values_are_returned(self):
        self.calculator.get_average_losses()
        average_loss = self.calculator.data[f'Average_Loss_{self.calculator.period}']
        self.assertEqual(average_loss[5], 1.2)
        self.assertEqual(average_loss[6], 1.2)
        self.assertEqual(average_loss[7], 0.8)
        self.assertEqual(average_loss[8], 0.8)
        self.assertFalse(average_loss[5:].isna().any())

    def test_when_period_is_5_days_then_5_nan_is_returned_rsi(self):
        self.calculator.calculate_rsi()
        rsi = self.calculator.data[f'RSI_{self.calculator.period}']
        for i in range(5):
            self.assertTrue(pd.isna(rsi[i]),
                            f"Expected NaN at index {i}, "
                            f"but got {rsi[i]}")

    def test_when_period_is_5_days_then_rsi_values_are_returned(self):
        self.calculator.calculate_rsi()
        rsi = self.calculator.data[f'RSI_{self.calculator.period}']
        self.assertEqual(rsi[5], 14.285714285714292)
        self.assertEqual(rsi[6], 14.285714285714292)
        self.assertEqual(rsi[7], 42.857142857142854)
        self.assertEqual(rsi[8], 42.857142857142854)
        self.assertFalse(rsi[5:].isna().any())


if __name__ == '__main__':
    unittest.main()
