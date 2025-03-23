import pandas as pd
from Sparplan import logger


class InputReader:
    def __init__(self, config):
        self.config = config
        self.input_data_file = self.config["input_data_file"].get(str)

    def read(self):
        df = pd.read_parquet(self.input_data_file)
        logger.debug("data of {} rows imported".format(len(df)))
        return {row["date"]: row["value"] for _, row in df.iterrows()}
