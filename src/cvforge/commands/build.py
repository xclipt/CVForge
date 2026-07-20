from pathlib import Path
import yaml
import yaml
from jinja2 import Environment, FileSystemLoader


def run(template_name="ats"):

    root = Path.cwd()

    data_file = root / "career/cv/data/resume.yaml"

    template_dir = (
        root /
        "src/cvforge/templates" /
        template_name
    )

    output = root / "build/resume.tex"

    if not data_file.exists():
        print("No resume.yaml found. Run: cvforge new resume")
        return

    with open(data_file, "r") as file:
        data = yaml.safe_load(file)

    env = Environment(
        loader=FileSystemLoader(template_dir)
    )

    template_file = (
        "harshibar.tex.j2"
        if template_name == "ats"
        else "modern.tex.j2"
    )

    template = env.get_template(template_file)

    rendered = template.render(**data)

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(rendered)

    print(f"✓ Built using {template_name} template")
    print(f"✓ Generated {output}")
