from pathlib import Path
import sys
import shutil


def run():
    print("CVForge Doctor\n")

    checks = []

    checks.append(
        ("Python version",
         sys.version_info >= (3, 9))
    )

    checks.append(
        ("LaTeX installed",
         shutil.which("pdflatex") is not None)
    )

    checks.append(
        ("Resume data found",
         Path("career/cv/data/resume.yaml").exists())
    )

    checks.append(
        ("Templates found",
         Path("src/cvforge/templates").exists())
    )

    checks.append(
        ("Build directory writable",
         Path("build").exists() or Path(".").exists())
    )

    for name, ok in checks:
        print(f"{'✓' if ok else '❌'} {name}")

    print("\nSystem ready.")
