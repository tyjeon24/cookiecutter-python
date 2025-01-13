import logging
import logging.config
from datetime import datetime
from pathlib import Path


def setup_logging():
    EVERY_DAY = 1

    date_str = datetime.now().strftime("%Y-%m-%d")
    log_dir = Path("logs")
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file_path = log_dir / f"{date_str}.log"

    logging_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {"standard": {"format": "%(asctime)s - %(name)s - %(levelname)-8s - %(message)s"}},
        "handlers": {
            "console": {
                "level": "DEBUG",
                "class": "logging.StreamHandler",
                "formatter": "standard",
            },
            "file": {
                "level": "DEBUG",
                "class": "logging.handlers.TimedRotatingFileHandler",
                "formatter": "standard",
                "filename": str(log_file_path),
                "when": "midnight",
                "interval": EVERY_DAY,
                "encoding": "utf-8",
            },
        },
        "root": {
            "handlers": ["console", "file"],
            "level": "DEBUG",
            "propagate": False,
        },
    }

    logging.config.dictConfig(logging_config)
