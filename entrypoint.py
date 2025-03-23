from Sparplan import logger, config
from Sparplan.constants import *
from Sparplan.input_reader import InputReader


def main():
    # read data
    data = InputReader(config).read()
    logger.info("data = {}".format(data))

    logger.info("Finished")


if __name__ == "__main__":
    main()
