import logging
from Sparplan import logger, config
from Sparplan.constants import *
from Sparplan.input_reader import InputReader
from Sparplan.gardener import Gardener

log_lev = config["log_level"].get(str)
logging.basicConfig(level=LOG_LEVELS[log_lev])


def main():
    logger.info("Started")

    # read data
    logger.info("reading data ...")
    data = InputReader(config).read()

    # gardener's work
    gardener = Gardener(config)
    logger.info("gardener planting seeds based on schedule ...")
    gardener.work(data)
    # final report
    logger.info("gardner reporting relative gain ...")
    gardener.final_report(data)

    logger.info("Finished")


if __name__ == "__main__":
    main()
