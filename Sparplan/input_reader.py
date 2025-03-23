import pandas as pd


class InputReader:
    def __init__(self, config):
        self.config = config
        self.input_data_file = self.config["input_data_file"].get(str)

    def read(self):
        data = pd.read_parquet(self.input_data_file).sort_values("date")
        return data
