from __future__ import annotations

import logging

from logging.handlers import (
    RotatingFileHandler,
)

from mail_analyzer.config import (
    LOG_DIR,
)


def setup_logging() -> None:

    formatter = logging.Formatter(
        "%(asctime)s "
        "%(levelname)s "
        "%(name)s "
        "%(message)s"
    )

    app_handler = RotatingFileHandler(
        LOG_DIR / "app.log",
        maxBytes=10_000_000,
        backupCount=10,
        encoding="utf-8",
    )

    app_handler.setFormatter(
        formatter
    )

    root_logger = logging.getLogger()

    root_logger.setLevel(
        logging.INFO
    )

    root_logger.addHandler(
        app_handler
    )