import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

logging.debug("Debug message")
logging.info("Program started")
logging.warning("This is a warning")
logging.error("An error occurred")
logging.critical("Critical error occurred")
