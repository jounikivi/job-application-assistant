import re


def normalize_text(text: str) -> str:
    """Normalisoi tekstin myöhempää analyysiä varten."""
    # Muutetaan teksti pienaakkosiksi, jotta vertailu ei riipu kirjainkoosta.
    lowered_text = text.lower()

    # Tiivistetään kaikki whitespace-merkit yhdeksi välilyönniksi.
    collapsed_whitespace = re.sub(r"\s+", " ", lowered_text)

    return collapsed_whitespace.strip()


def split_into_tokens(text: str) -> list[str]:
    """Jaa normalisoitu teksti tokeneiksi."""
    normalized_text = normalize_text(text)
    if not normalized_text:
        return []

    # Jaetaan normalisoitu teksti sanoiksi välilyönnin perusteella.
    return normalized_text.split(" ")
