import logging
import confuse

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)

config = confuse.Configuration("Sparplan", __name__)
