from typer.testing import (
    CliRunner,
)

from mail_analyzer.cli import app


runner = CliRunner()


def test_health():
    result = runner.invoke(
        app,
        ["health"],
    )

    assert result.exit_code == 0

    assert (
        "Status: OK"
        in result.stdout
    )