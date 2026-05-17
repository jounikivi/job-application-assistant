"""Command-line interface for the Job Application Assistant."""

from __future__ import annotations

import argparse
from collections.abc import Sequence
from pathlib import Path

from job_application_assistant.io import load_input_texts


def build_parser() -> argparse.ArgumentParser:
    """Create the top-level argument parser for the application."""
    parser = argparse.ArgumentParser(
        prog="job-application-assistant",
        description=(
            "Analyze a job posting against a CV locally and produce "
            "targeted recommendations."
        ),
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    analyze_parser = subparsers.add_parser(
        "analyze",
        help="Compare a job posting and a CV.",
    )
    analyze_parser.add_argument(
        "--job",
        type=Path,
        required=True,
        help="Path to the job posting text file.",
    )
    analyze_parser.add_argument(
        "--cv",
        type=Path,
        required=True,
        help="Path to the CV text file.",
    )
    analyze_parser.add_argument(
        "--output",
        type=Path,
        help="Optional path for writing a Markdown report.",
    )
    analyze_parser.set_defaults(handler=handle_analyze)

    return parser


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    """Parse CLI arguments into a namespace."""
    return build_parser().parse_args(argv)


def handle_analyze(args: argparse.Namespace) -> int:
    """Handle the analyze subcommand.

    The real analysis pipeline will be added in later phases. For now, this
    step proves that the CLI can load local source texts in a typed,
    testable way before preprocessing and extraction are added.
    """
    loaded_texts = load_input_texts(args.job, args.cv)

    print("Loaded job posting and CV successfully.")
    print(f"Job text length: {len(loaded_texts.job_text)}")
    print(f"CV text length: {len(loaded_texts.cv_text)}")
    if args.output is not None:
        print(f"Output file: {args.output}")
    else:
        print("Output file: not provided")

    return 0


def main(argv: Sequence[str] | None = None) -> int:
    """Run the CLI application and return a process exit code."""
    try:
        args = parse_args(argv)
        return args.handler(args)
    except (FileNotFoundError, ValueError) as error:
        print(f"Error: {error}")
        return 1
