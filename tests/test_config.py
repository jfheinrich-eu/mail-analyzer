import pytest

from mail_analyzer.config import (
    ConfigurationError,
    load_settings,
)


def test_load_settings_success(
    monkeypatch,
):
    monkeypatch.setenv(
        "CLIENT_ID",
        "client"
    )

    monkeypatch.setenv(
        "TENANT_ID",
        "tenant"
    )

    settings = load_settings()

    assert settings.client_id == "client"
    assert settings.tenant_id == "tenant"


def test_missing_client_id(
    monkeypatch,
):
    monkeypatch.delenv(
        "CLIENT_ID",
        raising=False
    )

    monkeypatch.setenv(
        "TENANT_ID",
        "tenant"
    )

    with pytest.raises(
        ConfigurationError
    ):
        load_settings()