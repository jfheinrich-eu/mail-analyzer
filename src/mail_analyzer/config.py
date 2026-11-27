from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


class ConfigurationError(RuntimeError):
    """Raised when mandatory configuration is missing."""


@dataclass(frozen=True)
class Settings:
    client_id: str
    tenant_id: str
    database_url: str
    log_level: str


def _require(name: str) -> str:
    value = os.getenv(name)

    if not value:
        raise ConfigurationError(f"Environment variable '{name}' is missing.")

    return value


def load_settings() -> Settings:
    return Settings(
        client_id=_require("CLIENT_ID"),
        tenant_id=_require("TENANT_ID"),
        database_url=os.getenv("DATABASE_URL", "sqlite:///data/mail_analyzer.db"),
        log_level=os.getenv("LOG_LEVEL", "INFO"),
    )


PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

DATA_DIR = PROJECT_ROOT / "data"
LOG_DIR = PROJECT_ROOT / "logs"
REPORT_DIR = PROJECT_ROOT / "reports"

for directory in (DATA_DIR, LOG_DIR, REPORT_DIR):
    directory.mkdir(parents=True, exist_ok=True)
