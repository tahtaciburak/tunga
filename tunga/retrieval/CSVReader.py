import pandas as pd


class CSVReader:
    def __init__(self, path):
        self.path = path

    def read(self, *args, **kwargs):
        return pd.read_csv(self.path)
