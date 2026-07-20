from pathlib import Path


def resume():
    path = Path("career/cv/data/resume.yaml")

    path.parent.mkdir(parents=True, exist_ok=True)

    if path.exists():
        print("resume.yaml already exists.")
        return

    content = """\
personal:
  name: ""
  title: ""
  email: ""
  phone: ""
  location: ""
  linkedin: ""
  github: ""

summary: ""

experience:
  - company: ""
    role: ""
    dates: ""
    achievements:
      - ""

education:
  - institution: ""
    degree: ""
    dates: ""

projects:
  - name: ""
    description: ""
    technologies:
      - ""

skills:
  technical:
    - ""
  tools:
    - ""
"""

    path.write_text(content)

    print("✓ Created career/cv/data/resume.yaml")
