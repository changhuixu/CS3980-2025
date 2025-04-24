import logging

logging.basicConfig(
    filename="app.log",
    format="%(asctime)s: %(name)s: %(levelname).4s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)
logger.info("info meesage")
logger.warning("this line will be logged with Level of warning")
logger.info("info meesage")
logger.error("error ms")
logger.fatal("fatal msage")
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")
