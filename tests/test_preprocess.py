from job_application_assistant.preprocess import normalize_text, split_into_tokens


def test_normalize_text_lowercases_and_collapses_whitespace() -> None:
    raw_text = "  Python   Developer\nREMOTE\tRole  "

    assert normalize_text(raw_text) == "python developer remote role"


def test_normalize_text_returns_empty_string_for_whitespace_only_input() -> None:
    assert normalize_text("  \n\t  ") == ""


def test_split_into_tokens_returns_words_in_order() -> None:
    raw_text = " Python   Developer\nREMOTE "

    assert split_into_tokens(raw_text) == ["python", "developer", "remote"]


def test_split_into_tokens_returns_empty_list_for_empty_input() -> None:
    assert split_into_tokens("  \n\t  ") == []
