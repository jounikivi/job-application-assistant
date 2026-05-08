from pathlib import Path

from job_application_assistant.io import read_text_file


def test_read_text_file(tmp_path: Path) -> None:
    # Luodaan testiä varten väliaikainen tiedosto, jotta testi ei riipu repoon
    # erikseen tallennetusta testidatasta.
    path = tmp_path / "test_file.txt"
    path.write_text("Hello world", encoding="utf-8")

    assert read_text_file(path) == "Hello world"
