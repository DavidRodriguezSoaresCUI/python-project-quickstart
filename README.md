# Python Project Quickstart

A simple script to quickly set up a python project with:

- standard structure:
  - `src` and `docs` directories
  - `CHANGELOG.md`, `LICENSE` and `README.md` files
- Python-specific `.gitignore` entries
- Pypi package config file `pyproject.toml`
- Static code analysis script `analyze_code` (Windows `bat` and POSIX `sh`)
- Documentation requirements file and scripts (Windows `bat` and POSIX `sh`)
- Optional [Black formatter](https://github.com/psf/black) settings for VSCode (requires [Microsoft's Black extension 'Black Formatter' for VSCode](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter))


## Respecting naming conventions

This script attempts to produce projects compliant with naming conventions :

- [PEP-423](https://peps.python.org/pep-0423)
- [PEP-8](https://peps.python.org/pep-0008)

This is implemented by :

- Recommending one word names
- Enforcing lowercase names
- Enforcing dot-separated prefix namespace for distribution/project names
- Enforcing hyphen-separated distribution/project names
- Enforcing underscore-separated package names