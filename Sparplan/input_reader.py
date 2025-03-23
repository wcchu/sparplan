import pandas as pd


class InputReader:
    def __init__(self, config):
        self.config = config
        self.input_data_file = self.config["input_data_file"].get(str)

    def read(self):
        df = pd.read_parquet(self.input_data_file)
        return {row["date"]: row["value"] for _, row in df.iterrows()}
