import os
import subprocess
import sys
from pathlib import Path

import pytest

from mail_analyzer import config
from mail_analyzer.config import (
    ConfigurationError,
    load_settings,
)


def test_load_settings_success(
    monkeypatch,
):
    monkeypatch.setenv("CLIENT_ID", "client")

    monkeypatch.setenv("TENANT_ID", "tenant")

    settings = load_settings()

    assert settings.client_id == "client"
    assert settings.tenant_id == "tenant"


def test_import_does_not_create_app_directories(
    tmp_path,
):
    app_home = tmp_path / "app"
    env = os.environ.copy()
    env["MAIL_ANALYZER_HOME"] = str(app_home)
    env["PYTHONPATH"] = str(Path(__file__).resolve().parents[1] / "src")

    subprocess.run(
        [sys.executable, "-c", "import mail_analyzer.config"],
        check=True,
        cwd=tmp_path,
        env=env,
    )

    assert not app_home.exists()


def test_ensure_app_directories_creates_user_directories(
    monkeypatch,
    tmp_path,
):
    app_home = tmp_path / "app"
    data_dir = tmp_path / "data"
    log_dir = tmp_path / "logs"
    report_dir = tmp_path / "reports"
    monkeypatch.setattr(config, "APP_HOME", app_home)
    monkeypatch.setattr(config, "DATA_DIR", data_dir)
    monkeypatch.setattr(config, "LOG_DIR", log_dir)
    monkeypatch.setattr(config, "REPORT_DIR", report_dir)

    config.ensure_app_directories()

    assert data_dir.is_dir()
    assert log_dir.is_dir()
    assert report_dir.is_dir()
    if os.name == "posix":
        for directory in (app_home, data_dir, log_dir, report_dir):
            assert directory.stat().st_mode & 0o077 == 0


def test_ensure_app_directories_rejects_symlinked_home(
    monkeypatch,
    tmp_path,
):
    app_home = tmp_path / "app"
    target = tmp_path / "target"
    target.mkdir()
    app_home.symlink_to(target, target_is_directory=True)
    monkeypatch.setattr(config, "APP_HOME", app_home)

    with pytest.raises(ConfigurationError, match="symbolic links"):
        config.ensure_app_directories()


def test_missing_client_id(
    monkeypatch,
):
    monkeypatch.delenv("CLIENT_ID", raising=False)

    monkeypatch.setenv("TENANT_ID", "tenant")

    with pytest.raises(ConfigurationError):
        load_settings()
