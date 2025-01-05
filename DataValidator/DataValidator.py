import pandas as pd


class DataValidator:
    def __init__(self, data):
        self.data = pd.DataFrame(data)

    def get_amount_of_empty_data(self):
        return self.data.isnull().sum().sum()

    def get_matrix_of_values(self):
        return self.data.isnull().values

    def remove_duplicated_values_if_exist(self):
        duplicated_count = self.data.duplicated().sum()
        if duplicated_count > 0:
            self.data = self.data.drop_duplicates()
            return duplicated_count
        return 0

    def remove_empty_rows_and_columns_if_exist(self):
        rows_before = len(self.data)
        cols_before = len(self.data.columns)

        self.data = self.data.dropna(how='all').dropna(axis=1, how='all')

        rows_after = len(self.data)
        cols_after = len(self.data.columns)

        return {
            'Removed Rows': rows_before - rows_after,
            'Removed Columns': cols_before - cols_after,
        }

    def check_for_negative_values(self):
        negative_values = self.data[
            ['Open', 'High', 'Low', 'Close']
        ].lt(0).sum().sum()
        return negative_values

    def get_data(self):
        return self.data
