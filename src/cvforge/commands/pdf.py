from pathlib import Path
import subprocess


def run():
    root = Path.cwd()

    tex_file = root / "build/resume.tex"

    if not tex_file.exists():
        print("No resume.tex found. Run: cvforge build")
        return

    print("Compiling PDF...")

    subprocess.run(
        [
            "pdflatex",
            "-interaction=nonstopmode",
            "-output-directory",
            str(root / "build"),
            str(tex_file)
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    pdf = root / "build/resume.pdf"

    if pdf.exists():
        print(f"✓ Generated {pdf}")
    else:
        print("PDF generation failed.")
