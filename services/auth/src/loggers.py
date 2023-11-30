import logging

logger=logging.getLogger("my_logger")
logger.setLevel(logging.INFO)

consoleHandler =logging.StreamHandler()
consoleFormatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
consoleHandler.setFormatter(consoleFormatter)

logger.addHandler(consoleHandler)

