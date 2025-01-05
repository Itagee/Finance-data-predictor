import unittest
from unittest.mock import patch
import pandas as pd
from DataDownloader.DataDownloaderFactory import DataDownloaderFactory


class TestYahooDataDownloader(unittest.TestCase):

    @patch(
        'DataDownloader.YahooDataDownloader.YahooDataDownloader.download_yahoo_data'
    )
    def test_when_given_data_is_provided_then_specific_data_is_downloaded(
            self, mock_downloaded
    ):
        data = {
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
        mock_data = pd.DataFrame(data).set_index('Date')
        mock_downloaded.return_value = mock_data
        data = DataDownloaderFactory().download_data('Apple',
                                                     '2023-01-01',
                                                     '2023-01-12')
        pd.testing.assert_frame_equal(data, mock_data)


if __name__ == '__main__':
    unittest.main()
