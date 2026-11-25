import typer

from mail_analyzer import __version__

app = typer.Typer(
    no_args_is_help=True
)

@app.callback()
def main() -> None:
    pass

@app.command()
def health() -> None:

    print(
        f"Mail Analyzer {__version__}"
    )

    print("Status: OK")


if __name__ == "__main__":
    app()