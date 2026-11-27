from __future__ import annotations

import logging
from logging.handlers import (
    RotatingFileHandler,
)

from mail_analyzer.config import (
    LOG_DIR,
    ConfigurationError,
    ensure_app_directories,
    get_log_level,
)

_APP_HANDLER_NAME = "mail_analyzer"


def _configured_log_level() -> int:
    name = get_log_level().upper()
    level = logging.getLevelNamesMapping().get(name)
    if not isinstance(level, int):
        raise ConfigurationError("LOG_LEVEL must be a valid logging level.")

    return level


def setup_logging() -> None:
    root_logger = logging.getLogger()
    root_logger.setLevel(_configured_log_level())

    if any(handler.get_name() == _APP_HANDLER_NAME for handler in root_logger.handlers):
        return

    ensure_app_directories()

    formatter = logging.Formatter(
        "%(asctime)s " "%(levelname)s " "%(name)s " "%(message)s"
    )

    app_handler = RotatingFileHandler(
        LOG_DIR / "app.log",
        maxBytes=10_000_000,
        backupCount=10,
        encoding="utf-8",
    )

    app_handler.setFormatter(formatter)
    app_handler.set_name(_APP_HANDLER_NAME)
    root_logger.addHandler(app_handler)
