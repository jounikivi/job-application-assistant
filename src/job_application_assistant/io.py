from dataclasses import dataclass
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


@dataclass(frozen=True, slots=True)
class LoadedTexts:
    """Sisältää analyysiin ladatut tekstisyötteet."""

    job_text: str
    cv_text: str


def load_input_texts(job_path: Path, cv_path: Path) -> LoadedTexts:
    """Lue työpaikkailmoituksen ja CV:n tekstit analyysiä varten."""
    return LoadedTexts(
        job_text=read_text_file(job_path),
        cv_text=read_text_file(cv_path),
    )
