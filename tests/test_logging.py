import logging

import pytest

from mail_analyzer import config, logging_config
from mail_analyzer.config import ConfigurationError
from mail_analyzer.logging_config import (
    setup_logging,
)


def test_logging_setup_uses_configured_level_and_is_idempotent(
    monkeypatch,
    tmp_path,
):
    root_logger = logging.getLogger()
    previous_level = root_logger.level
    previous_handlers = tuple(root_logger.handlers)
    log_dir = tmp_path / "logs"
    monkeypatch.setattr(config, "APP_HOME", tmp_path / "app")
    monkeypatch.setattr(config, "DATA_DIR", tmp_path / "data")
    monkeypatch.setattr(logging_config, "LOG_DIR", log_dir)
    monkeypatch.setattr(config, "LOG_DIR", log_dir)
    monkeypatch.setattr(config, "REPORT_DIR", tmp_path / "reports")
    monkeypatch.setenv("LOG_LEVEL", "WARNING")

    try:
        setup_logging()
        setup_logging()

        app_handlers = [
            handler
            for handler in root_logger.handlers
            if handler.get_name() == "mail_analyzer"
        ]

        assert root_logger.level == logging.WARNING
        assert len(app_handlers) == 1
        assert (log_dir / "app.log").is_file()
    finally:
        for handler in tuple(root_logger.handlers):
            if handler not in previous_handlers:
                root_logger.removeHandler(handler)
                handler.close()

        root_logger.setLevel(previous_level)


def test_logging_setup_rejects_invalid_level(
    monkeypatch,
    tmp_path,
):
    monkeypatch.setattr(logging_config, "LOG_DIR", tmp_path)
    monkeypatch.setenv("LOG_LEVEL", "invalid")

    with pytest.raises(ConfigurationError, match="LOG_LEVEL"):
        setup_logging()

    assert not (tmp_path / "app.log").exists()
