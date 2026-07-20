from pathlib import Path
import yaml


def run():
    resume = Path("career/cv/data/resume.yaml")

    if not resume.exists():
        print("❌ resume.yaml not found")
        return

    data = yaml.safe_load(resume.read_text()) or {}

    errors = []

    if not data.get("personal", {}).get("name"):
        errors.append("personal.name")

    if not data.get("summary"):
        errors.append("summary")

    if not data.get("experience"):
        errors.append("experience")

    if not data.get("skills", {}).get("technical"):
        errors.append("skills.technical")

    if errors:
        print("❌ Missing fields:")
        for item in errors:
            print(f" - {item}")
        return

    print("✓ Resume file found")
    print("✓ Required sections present")
    print("✓ Ready to build")
