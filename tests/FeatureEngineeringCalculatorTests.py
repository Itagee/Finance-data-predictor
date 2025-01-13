import unittest
import pandas as pd
from DataCalculator.FeatureEngineeringCalculator import (
    FeatureEngineeringCalculator
)


class TestFeatureEngineeringCalculator(unittest.TestCase):
    def setUp(self):
        self.data = {
            'Date': pd.date_range(start='2023-01-01',
                                  end='2023-01-12',
                                  freq='B'),
            'Open': [150, 152, 151, 149, 148, 145, 146, 148, 149],
            'High': [155, 157, 156, 154, 153, 150, 151, 153, 152],
            'Low': [148, 150, 149, 147, 146, 143, 144, 146, 145],
            'Close': [153, 154, 152, 151, 150, 148, 149, 151, 150],
            'Adj Close': [153, 154, 152, 151, 150, 148, 149, 151, 150],
            'Volume': [1000000, 1200000, 1100000, 1300000, 1400000,
                       1250000, 1300000, 1400000, 1350000]
        }

        self.calculator = FeatureEngineeringCalculator(
            data=self.data,
            period=5
        )

    def test_when_period_id_5_days_then_4_nan_is_returned(
            self):
        sma = self.calculator.get_simple_moving_average_based_on_close_prices()
        for i in range(4):
            self.assertTrue(pd.isna(sma[i]),
                            f"Expected NaN at index {i}, but got {sma[i]}"
                            )

    def test_when_period_is_5_days_then_sma_values_are_returned(self):

        sma = self.calculator.get_simple_moving_average_based_on_close_prices()
        self.assertEqual(sma[4], 152.0,
                         f"Expected 152.0 on day 5,"
                         f" but got {sma[4]}")
        self.assertEqual(sma[5], 151.0,
                         f"Expected 151.0 on day 6, "
                         f"but got {sma[5]}")
        self.assertEqual(sma[6], 150.0,
                         f"Expected 150.0 on day 7, "
                         f"but got {sma[6]}")
        self.assertEqual(sma[7], 149.8,
                         f"Expected 149.8 on day 8, "
                         f"but got {sma[7]}")
        self.assertEqual(sma[8], 149.6,
                         f"Expected 149.6 on day 9, "
                         f"but got {sma[8]}")
        self.assertEqual(len(sma), len(self.data['Close']),
                         f"Expected SMA length of "
                         f"{len(self.data['Close'])}, "
                         f"but got {len(sma)}")
        self.assertFalse(sma[4:].isna().any(),
                         "SMA contains NaN values after day 5, "
                         "but it should not")


if __name__ == '__main__':
    unittest.main()
