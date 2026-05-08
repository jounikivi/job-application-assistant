from pathlib import Path


def read_text_file(path: Path) -> str:
    """Lue UTF-8-tekstitiedosto ja palauta sen sisältö."""
    # Erotellaan puuttuva polku omaksi virheekseen, jotta syy on käyttäjälle selkeä.
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    # Hyväksytään vain oikeat tiedostot, ei esimerkiksi kansioita.
    if not path.is_file():
        raise ValueError(f"Path is not a file: {path}")

    return path.read_text(encoding="utf-8")
