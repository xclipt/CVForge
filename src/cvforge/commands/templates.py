from pathlib import Path


def run():
    root = Path("src/cvforge/templates")

    print("Available templates:\n")

    for category in sorted(root.iterdir()):
        if category.is_dir():
            print(category.name)

            for template in sorted(category.glob("*.tex.j2")):
                print(f"  └── {template.stem.replace('.tex', '')}")
