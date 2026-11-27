from typer.testing import CliRunner

from mail_analyzer import __version__
from mail_analyzer.cli import app


def test_version():

    assert __version__ == "0.1.0"


def test_health_command():

    result = CliRunner().invoke(app, ["health"])

    assert result.exit_code == 0
    assert "Mail Analyzer 0.1.0" in result.stdout
    assert "Status: OK" in result.stdout
