from YahooDataDownloader import YahooDataDownloader
import YahooDataSources as Data


class DataDownloaderFactory:
    @staticmethod
    def download_data(data_type, start_date, end_date):

        if data_type in data.data_sources.keys():
            symbol = data.data_sources[data_type]
            downloader = YahooDataDownloader(data_type=symbol,
                                             start_date=start_date,
                                             end_date=end_date)
            return downloader.download_yahoo_data()
        else:
            raise ValueError(f'Unknown type of data: {data_type}')


if __name__ == "__main__":
    try:
        data = DataDownloaderFactory.download_data("Apple",
                                                   '2018-01-01',
                                                   '2023-01-01')
        print(data)
    except ValueError as error:
        print(error)
