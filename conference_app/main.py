"""Punkt wejściowy aplikacji systemu rejestracji na konferencję."""

from conference_app.cli import run_cli


def main() -> None:
    """Uruchamia aplikację."""
    run_cli()


if __name__ == "__main__":
    main()
