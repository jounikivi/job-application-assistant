from pathlib import Path

from job_application_assistant.cli import main, parse_args


def test_parse_args_for_analyze_command() -> None:
    args = parse_args(["analyze", "--job", "job.txt", "--cv", "cv.txt"])

    assert args.command == "analyze"
    assert args.job == Path("job.txt")
    assert args.cv == Path("cv.txt")
    assert args.output is None


def test_main_returns_zero_for_analyze_command(capsys) -> None:
    job_path = Path(__file__).parent / "_runtime_cli_job.txt"
    cv_path = Path(__file__).parent / "_runtime_cli_cv.txt"
    job_path.write_text("Backend Python role", encoding="utf-8")
    cv_path.write_text("Python, APIs, testing", encoding="utf-8")

    try:
        exit_code = main(["analyze", "--job", str(job_path), "--cv", str(cv_path)])
        captured = capsys.readouterr()

        assert exit_code == 0
        assert "Loaded job posting and CV successfully." in captured.out
        assert "Job text length:" in captured.out
        assert "CV text length:" in captured.out
    finally:
        if job_path.exists():
            job_path.unlink()
        if cv_path.exists():
            cv_path.unlink()


def test_main_returns_one_for_missing_input_file(capsys) -> None:
    exit_code = main(["analyze", "--job", "missing-job.txt", "--cv", "missing-cv.txt"])
    captured = capsys.readouterr()

    assert exit_code == 1
    assert "Error: File not found:" in captured.out
