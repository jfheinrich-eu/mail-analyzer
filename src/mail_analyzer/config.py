from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

APP_HOME = Path(
    os.getenv("MAIL_ANALYZER_HOME") or Path.home() / ".mail-analyzer"
).expanduser()
if not APP_HOME.is_absolute():
    APP_HOME = Path.cwd() / APP_HOME

DATA_DIR = APP_HOME / "data"
LOG_DIR = APP_HOME / "logs"
REPORT_DIR = APP_HOME / "reports"


class ConfigurationError(RuntimeError):
    """Raised when mandatory configuration is missing."""


@dataclass(frozen=True)
class Settings:
    client_id: str
    tenant_id: str
    database_url: str
    log_level: str


def get_log_level() -> str:
    return os.getenv("LOG_LEVEL", "INFO")


def _require(name: str) -> str:
    value = os.getenv(name)

    if not value:
        raise ConfigurationError(f"Environment variable '{name}' is missing.")

    return value


def load_settings() -> Settings:
    return Settings(
        client_id=_require("CLIENT_ID"),
        tenant_id=_require("TENANT_ID"),
        database_url=os.getenv(
            "DATABASE_URL",
            f"sqlite:///{(DATA_DIR / 'mail_analyzer.db').as_posix()}",
        ),
        log_level=get_log_level(),
    )


def ensure_app_directories() -> None:
    for directory in (APP_HOME, DATA_DIR, LOG_DIR, REPORT_DIR):
        if directory.is_symlink():
            raise ConfigurationError(
                "Application data directories must not be symbolic links."
            )

        directory.mkdir(parents=True, exist_ok=True, mode=0o700)
        if os.name == "posix":
            directory.chmod(0o700)
