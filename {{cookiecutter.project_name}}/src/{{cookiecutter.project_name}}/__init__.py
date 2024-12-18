# logging
# from src.project.logging_config import logger
# logger.info("...")
from .logging_config import setup_logging

setup_logging()

# typeguard hook
from typeguard import install_import_hook

install_import_hook("src")
