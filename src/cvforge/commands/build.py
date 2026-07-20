from pathlib import Path
import yaml
from jinja2 import Environment, FileSystemLoader


def run():
    root = Path.cwd()

    data_file = root / "career/cv/data/resume.yaml"
    template_dir = root / "src/cvforge/templates/ats"

    output = root / "build/resume.tex"

    if not data_file.exists():
        print("No resume.yaml found. Run: cvforge new resume")
        return

    with open(data_file, "r") as file:
        data = yaml.safe_load(file)

    env = Environment(
        loader=FileSystemLoader(template_dir)
    )

    template = env.get_template("resume.tex.j2")

    rendered = template.render(**data)

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(rendered)

    print(f"✓ Generated {output}")
