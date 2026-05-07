"""Command-line interface for the Job Application Assistant."""

from __future__ import annotations

import argparse
from collections.abc import Sequence
from pathlib import Path


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
    proves that the CLI wiring works and that paths flow into the app in a
    typed, testable way.
    """
    print("Analyze command received.")
    print(f"Job file: {args.job}")
    print(f"CV file: {args.cv}")
    if args.output is not None:
        print(f"Output file: {args.output}")
    else:
        print("Output file: not provided")

    return 0


def main(argv: Sequence[str] | None = None) -> int:
    """Run the CLI application and return a process exit code."""
    args = parse_args(argv)
    return args.handler(args)
