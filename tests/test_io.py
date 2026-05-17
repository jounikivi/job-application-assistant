from pathlib import Path

import pytest

from job_application_assistant.io import read_text_file


def test_read_text_file_raises_for_missing_file() -> None:
    # Käytetään polkua, jota ei pitäisi olla olemassa.
    path = Path(__file__).parent / "_missing_file.txt"

    # jatka tästä ja varmista, että FileNotFoundError heitetään.
    with pytest.raises(FileNotFoundError, match="File not found"):
        read_text_file(path)