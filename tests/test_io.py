from pathlib import Path

import pytest

from job_application_assistant.io import read_text_file


def test_read_text_file() -> None:
  path = Path(__file__).parent / "test_file.txt"
  assert read_text_file(path) == "Hello world"
