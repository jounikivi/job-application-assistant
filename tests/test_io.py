from pathlib import Path

from job_application_assistant.io import read_text_file


def test_read_text_file() -> None:
    # Luodaan testitiedosto testin ajon ajaksi suoraan testikansioon, jotta
    # testi ei riipu pytestin tmp_path-fixturestä tässä ympäristössä.
    path = Path(__file__).parent / "_runtime_test_file.txt"
    path.write_text("Hello world", encoding="utf-8")

    try:
        assert read_text_file(path) == "Hello world"
    finally:
        # Siivotaan testitiedosto pois myös silloin, jos testi epäonnistuu.
        if path.exists():
            path.unlink()
