from pathlib import Path

def read_text_file(path: Path) -> str:
  """Read a UTF-8 text file and return its contents."""
  if not path.exists():
    raise FileNotFoundError(f"File not found: {path}")
  
  if not path.is_file():
    raise ValueError(f"Path is not a file: {path}")

  return path.read_text(encoding="utf-8")