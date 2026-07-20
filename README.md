# CVForge

AI-assisted ATS resume builder powered by Python, LaTeX, and VS Code.

CVForge transforms structured resume data into professional PDF resumes using reusable templates and AI-assisted writing workflows.

## Features

- ATS-friendly LaTeX resume generation
- Structured YAML resume data
- Multiple resume templates
- PDF generation pipeline
- VS Code AI assistance
- Modular template system

## Architecture

resume.yaml
    |
    v
CVForge Engine
    |
    +--> ATS Template
    |
    +--> Photo Template
    |
    v
LaTeX
    |
    v
PDF Resume

## Installation

Clone repository:

git clone https://github.com/greenhell1101/CVForge.git
cd CVForge

Install:

pip install -e .

## Usage

Initialize workspace:

cvforge init

Create resume:

cvforge new resume

Build:

cvforge build

Generate PDF:

cvforge pdf

## AI Assistance

CVForge includes VS Code AI instructions and prompt templates for ATS optimization and resume improvement.

## Roadmap

- [x] CLI engine
- [x] Resume data model
- [x] LaTeX renderer
- [x] PDF generation
- [x] Multiple templates
- [x] AI workflow foundation
- [ ] VS Code extension
- [ ] Job matching
- [ ] Resume scoring

## License

MIT
