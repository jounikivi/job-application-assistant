import re

DEFAULT_STOP_WORDS = frozenset(
    {
        "a",
        "an",
        "and",
        "are",
        "for",
        "in",
        "is",
        "of",
        "on",
        "or",
        "the",
        "to",
        "with",
        "että",
        "ja",
        "myös",
        "on",
        "ovat",
        "sekä",
        "tai",
        "varten",
    }
)


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


def remove_stop_words(
    tokens: list[str],
    stop_words: frozenset[str] | set[str] | None = None,
) -> list[str]:
    """Poista listasta yleiset stop-sanat säilyttäen järjestys."""
    words_to_remove = stop_words if stop_words is not None else DEFAULT_STOP_WORDS

    # Säilytetään tokenien alkuperäinen järjestys, koska sillä voi olla
    # myöhemmin merkitystä fraasien muodostuksessa.
    return [token for token in tokens if token not in words_to_remove]


def preprocess_text(
    text: str,
    stop_words: frozenset[str] | set[str] | None = None,
) -> list[str]:
    """Suorita tekstille preprocess-putki."""
    tokens = split_into_tokens(text)
    return remove_stop_words(tokens, stop_words)
