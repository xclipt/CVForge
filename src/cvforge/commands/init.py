from pathlib import Path


def run():
    root = Path.cwd()

    folders = [
        ".github",
        ".vscode",
        "career/cv/data",
        "career/cv/sections",
        "career/cv/assets",
        "career/cv/output",
        "templates/ats",
        "build",
    ]

    print("\n🚀 Initializing CVForge workspace...\n")

    for folder in folders:
        path = root / folder
        path.mkdir(parents=True, exist_ok=True)
        print(f"✓ Created {folder}")

    instructions = root / ".github/copilot-instructions.md"

    instructions.write_text(
        "# CVForge AI Instructions\n\n"
        "You are assisting with ATS-friendly resume creation.\n"
        "Prioritize measurable achievements, clarity, and professional language.\n"
    )

    print("\n✓ AI instructions created")
    print("\nCVForge workspace ready.")
