from pathlib import Path

from job_application_assistant.cli import main, parse_args


def test_parse_args_for_analyze_command() -> None:
    args = parse_args(["analyze", "--job", "job.txt", "--cv", "cv.txt"])

    assert args.command == "analyze"
    assert args.job == Path("job.txt")
    assert args.cv == Path("cv.txt")
    assert args.output is None


def test_main_returns_zero_for_analyze_command(capsys) -> None:
    exit_code = main(["analyze", "--job", "job.txt", "--cv", "cv.txt"])

    captured = capsys.readouterr()

    assert exit_code == 0
    assert "Analyze command received." in captured.out
