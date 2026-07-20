import argparse
from cvforge.version import VERSION

from cvforge.commands.init import run as init_run
from cvforge.commands.new import resume as resume_run
from cvforge.commands.build import run as build_run
from cvforge.commands.pdf import run as pdf_run
from cvforge.commands.templates import run as templates_run
from cvforge.commands.validate import run as validate_run
from cvforge.commands.doctor import run as doctor_run


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

    build_parser = subparsers.add_parser(
        "build",
        help="Build LaTeX resume"
    )

    build_parser.add_argument(
        "--template",
        default="ats",
        help="Choose resume template"
    )

    subparsers.add_parser(
        "pdf",
        help="Generate PDF resume"
    )

    subparsers.add_parser(
        "templates",
        help="List available resume templates"
    )

    subparsers.add_parser(
        "validate",
        help="Validate resume data"
    )

    subparsers.add_parser(
        "doctor",
        help="Check CVForge environment"
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
        print(f"CVForge v{VERSION}")
        return

    if args.command == "init":
        init_run()
        return

    if args.command == "new":
        if args.new_command == "resume":
            resume_run()
            return

    if args.command == "build":
        build_run(args.template)
        return

    if args.command == "templates":
        templates_run()
        return

    if args.command == "validate":
        validate_run()
        return

    if args.command == "doctor":
        doctor_run()
        return

    if args.command == "pdf":
        pdf_run()
        return

    parser.print_help()


if __name__ == "__main__":
    main()
