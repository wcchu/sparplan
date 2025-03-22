from Sparplan import logger, config
from Sparplan.constants import *


def main():
    test_field = config["test_field"].get(str)
    logger.info("test_field = {}".format(test_field))


if __name__ == "__main__":
    main()
