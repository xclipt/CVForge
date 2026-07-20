import argparse

from cvforge.commands.init import run as init_run
from cvforge.commands.new import resume as resume_run


def main():
    parser = argparse.ArgumentParser(
        prog="cvforge",
        description="AI-assisted ATS resume authoring toolkit."
    )

    parser.add_argument(
        "--version",
        action="store_true",
        help="Show CVForge version"
    )

    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser(
        "init",
        help="Initialize a CVForge workspace"
    )

    new_parser = subparsers.add_parser(
        "new",
        help="Create CVForge resources"
    )

    new_sub = new_parser.add_subparsers(dest="new_command")

    new_sub.add_parser(
        "resume",
        help="Create resume data file"
    )

    args = parser.parse_args()

    if args.version:
        print("CVForge v0.1.0")
        return

    if args.command == "init":
        init_run()
        return

    if args.command == "new":
        if args.new_command == "resume":
            resume_run()
            return

    parser.print_help()


if __name__ == "__main__":
    main()
