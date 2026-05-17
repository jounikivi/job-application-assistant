from pathlib import Path

import pytest

from job_application_assistant.io import load_input_texts, read_text_file


def test_read_text_file() -> None:
    # Luodaan testitiedosto testin ajon ajaksi suoraan testikansioon.
    path = Path(__file__).parent / "_runtime_test_file.txt"
    path.write_text("Hello world", encoding="utf-8")

    try:
        assert read_text_file(path) == "Hello world"
    finally:
        # Siivotaan testitiedosto pois myös silloin, jos testi epäonnistuu.
        if path.exists():
            path.unlink()


def test_read_text_file_raises_for_missing_file() -> None:
    # Käytetään polkua, jota ei pitäisi olla olemassa.
    path = Path(__file__).parent / "_missing_file.txt"

    # jatka tästä ja varmista, että FileNotFoundError heitetään.
    with pytest.raises(FileNotFoundError, match="File not found"):
        read_text_file(path)


def test_read_text_file_raises_for_directory() -> None:
    # Olemassa oleva kansiopolku ei kelpaa tiedostonluvulle.
    path = Path(__file__).parent

    with pytest.raises(ValueError, match="Path is not a file"):
        read_text_file(path)


def test_load_input_texts_reads_both_files() -> None:
    # Luodaan kaksi pientä syötetiedostoa, joista toinen kuvaa ilmoitusta
    # ja toinen CV:tä.
    job_path = Path(__file__).parent / "_runtime_job.txt"
    cv_path = Path(__file__).parent / "_runtime_cv.txt"
    job_path.write_text("Python developer role", encoding="utf-8")
    cv_path.write_text("Experienced with Python and testing", encoding="utf-8")

    try:
        loaded_texts = load_input_texts(job_path, cv_path)

        assert loaded_texts.job_text == "Python developer role"
        assert loaded_texts.cv_text == "Experienced with Python and testing"
    finally:
        # Siivotaan testitiedostot pois testiajon jälkeen.
        if job_path.exists():
            job_path.unlink()
        if cv_path.exists():
            cv_path.unlink()
