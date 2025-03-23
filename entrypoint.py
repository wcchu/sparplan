from Sparplan import logger, config
from Sparplan.constants import *
from Sparplan.input_reader import InputReader
from Sparplan.gardener import Gardener


def main():
    # read data
    data = InputReader(config).read()
    logger.info("data = {}".format(data))

    gardener = Gardener(config)
    gardener.work(data)

    logger.info("Finished")


if __name__ == "__main__":
    main()
