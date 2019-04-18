from .logger import Logger
import traceback

logger = Logger("/var/log/via/python")

try:
    raise ValueError("Bad value")
except ValueError:
    logger.error(traceback.format_exc())

logger.error("An error occured...")

logger.info("Something just happened...")
