# pylint: disable=C3001
"""A simple script to quickly set up a python project (see README.md)
"""

import ast
from pathlib import Path
from subprocess import PIPE, Popen
from typing import Any, Callable, Iterable, Optional, Union

DEFAULT_MIN_PY_VER = "3.10"

CWD = Path(".")
CHANGELOG_FILE_CONTENT = "# Changelog\n\nAll notable changes to this project will be documented in this file.\n\nThe format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).\n\n<!-- As much as possible use subsections: Added, Removed, Modified, BugFix -->\n\n<!-- ## [0.0.1] - date\n\n__INITIAL RELEASE__ -->"
README_FILE_CONTENT = (
    lambda project_name, repo_url, short_description: f"# [{project_name}]({repo_url}) - {short_description}\n\nPut a description here"
)
GITIGNORE_FILE_CONTENT = "# Byte-compiled / optimized / DLL files\n__pycache__/\n*.py[cod]\n*$py.class\n\n# C extensions\n*.so\n\n# Distribution / packaging\n.Python\nbuild/\ndevelop-eggs/\ndist/\ndownloads/\neggs/\n.eggs/\nlib/\nlib64/\nparts/\nsdist/\nvar/\nwheels/\npip-wheel-metadata/\nshare/python-wheels/\n*.egg-info/\n.installed.cfg\n*.egg\nMANIFEST\n\n# PyInstaller\n#  Usually these files are written by a python script from a template\n#  before PyInstaller builds the exe, so as to inject date/other infos into it.\n*.manifest\n*.spec\n\n# Installer logs\npip-log.txt\npip-delete-this-directory.txt\n\n# Unit test / coverage reports\nhtmlcov/\n.tox/\n.nox/\n.coverage\n.coverage.*\n.cache\nnosetests.xml\ncoverage.xml\n*.cover\n*.py,cover\n.hypothesis/\n.pytest_cache/\n\n# Translations\n*.mo\n*.pot\n\n# Django stuff:\n*.log\nlocal_settings.py\ndb.sqlite3\ndb.sqlite3-journal\n\n# Flask stuff:\ninstance/\n.webassets-cache\n\n# Scrapy stuff:\n.scrapy\n\n# Sphinx documentation\ndocs/_build/\n\n# PyBuilder\ntarget/\n\n# Jupyter Notebook\n.ipynb_checkpoints\n\n# IPython\nprofile_default/\nipython_config.py\n\n# pyenv\n.python-version\n\n# pipenv\n#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.\n#   However, in case of collaboration, if having platform-specific dependencies or dependencies\n#   having no cross-platform support, pipenv may install dependencies that don't work, or not\n#   install all needed dependencies.\n#Pipfile.lock\n\n# PEP 582; used by e.g. github.com/David-OConnor/pyflow\n__pypackages__/\n\n# Celery stuff\ncelerybeat-schedule\ncelerybeat.pid\n\n# SageMath parsed files\n*.sage.py\n\n# Environments\n.env\n.venv\nenv/\nvenv/\nENV/\nenv.bak/\nvenv.bak/\n\n# Spyder project settings\n.spyderproject\n.spyproject\n\n# Rope project settings\n.ropeproject\n\n# mkdocs documentation\n/site\n\n# mypy\n.mypy_cache/\n.dmypy.json\ndmypy.json\n\n# Pyre type checker\n.pyre/\n\n# VSCode local settings\n.vscode/settings.json\n\n# static code analysis report\nanalyze_code.report.txt\n"
VSCODE_SETTING_FILE_CONTENT = '{\n    "[python]": {\n        "editor.defaultFormatter": "ms-python.black-formatter",\n        "editor.formatOnSave": true\n    }\n}'
PYPROJECT_FILE_CONTENT = (
    lambda author, author_email, package_name, repo_url, short_description, min_py_ver: f'[build-system]\nrequires = ["setuptools>=61.0"]\nbuild-backend = "setuptools.build_meta"\n\n[project]\nname = "{package_name}"\nversion = "0.0.1"\nauthors = [\n  {{ name="{author}", email="{author_email}" }},\n]\ndescription = "{short_description}"\nreadme = "README.md"\nlicense = {{ file = "LICENSE" }}\nrequires-python = ">={min_py_ver}"\nclassifiers = [\n    "Programming Language :: Python :: 3",\n]\ndependencies = [\n\n]\n\n[project.urls]\n"Homepage" = "{repo_url}"\n"Bug Tracker" = "{repo_url}/issues"'
)
ANALYZE_CODE_BAT_FILE_CONTENT = '@echo off\nSET report_file=analyze_code.report.txt\n\nsetlocal enabledelayedexpansion enableextensions\nset FILE_LIST=\nfor /R src %%F IN (*.py) do (\n    set FILE_LIST=!FILE_LIST! "%%F"\n)\nset FILE_LIST=%FILE_LIST:~1%\n\nECHO Analyzing with MYPY\nECHO ==== MYPY ==== >%report_file%\nECHO (Disable false positives with inline comment "# type: ignore[<ERROR_NAME>]") >>%report_file%\nmypy %FILE_LIST% >>%report_file%\n\nECHO Analyzing with BANDIT\nECHO ==== BANDIT ==== >>%report_file%\nECHO (Disable false positives with inline comment "# nosec <ERROR_CODE>") >>%report_file%\nbandit %FILE_LIST% 1>>%report_file% 2>NUL\n\nECHO Analyzing with PYLINT\nECHO ==== PYLINT ==== >>%report_file%\npylint %FILE_LIST% >>%report_file%\n\nECHO Analyzing with FLAKE8\nECHO ==== FLAKE8 ==== >>%report_file%\npython -m flake8 %FILE_LIST% >>%report_file%\n'
ANALYZE_CODE_SH_FILE_CONTENT = "report_file=analyze_code.report.txt\n\nFILE_LIST=$(find src -type f -iname \"*.py\" -printf '%p ')\n\necho Analyzing with MYPY\necho ==== MYPY ==== >${report_file}\necho \"(Disable false positives with inline comment '# type: ignore[<ERROR_NAME>]')\" >>${report_file}\nmypy $FILE_LIST >>${report_file}\n\necho Analyzing with BANDIT\necho ==== BANDIT ==== >>${report_file}\necho \"(Disable false positives with inline comment '# nosec <ERROR_CODE>')\" >>${report_file}\nbandit $FILE_LIST 1>>${report_file} 2>NUL\n\necho Analyzing with PYLINT\necho ==== PYLINT ==== >>${report_file}\npylint $FILE_LIST >>${report_file}\n\necho Analyzing with FLAKE8\necho ==== FLAKE8 ==== >>${report_file}\nflake8 $FILE_LIST >>${report_file}\n"
INDEX_RST_FILE_CONTENT = "Welcome to {module_name}'s documentation!\n==================================\n\n.. automodule:: {module_name}\n   :members:\n   :undoc-members:\n   :show-inheritance:\n\n.. toctree::\n   :maxdepth: 2\n   :caption: Contents:\n\nFind more\n---------\n\n* :ref:`genindex`\n* :ref:`modindex`\n* :ref:`search`"
SPHINX_REBUILD_BAT_FILE_CONTENT = (
    lambda project_name, author: f'@echo off\n\necho Rebuilding source directory\nRD /S /Q ".\source"\nsphinx-apidoc -f --maxdepth 4 --separate --doc-project "{project_name}" --doc-author "{author}" --full -o source ../src/{project_name}\npython sphinx-patch-conf.py\n\necho Rebuilding HTML build\nRD /S /Q ".\\build"\nsphinx-build source build\necho Done ! Open build/index.html to see documentation'
)
SPHINX_REBUILD_SH_FILE_CONTENT = (
    lambda project_name, author: f'#! /bin/bash\n\necho Rebuilding source directory\nfind ./source -mindepth 1 -delete 2>/dev/null\nrmdir ./source\nsphinx-apidoc -f --maxdepth 4 --separate --doc-project "{project_name}" --doc-author "{author}" --full -o source ../src/{project_name}\npython3 sphinx-patch-conf.py\n\necho Rebuilding HTML build\nfind ./build -mindepth 1 -delete 2>/dev/null\nrmdir ./build\nsphinx-build source build\necho Done ! Open build/index.html to see documentation'
)
SPHINX_PATCH_CONF_FILE_CONTENT = "from pathlib import Path\n\n\ndef main() -> None:\n    conf_file = Path('./source/conf.py')\n    conf = conf_file.read_text(encoding='utf8')\n    if not 'sys.path.insert' in conf:\n        conf_file.write_text(\n            \"import os\\nimport sys\\nsys.path.insert(0, os.path.abspath('../../src/'))\\n\"\n            + conf.replace(\"html_theme = 'alabaster'\", \"html_theme = 'furo'\"),\n            encoding='utf8'\n        )\n\n\nif __name__ == '__main__':\n    main()\n"


def execute(command) -> dict[str, str]:
    """Passes command to subprocess.Popen, retrieves stdout/stderr and performs
    error management.
    Returns a dictionnary containing stdX.
    Upon command failure, prints exception and returns empty dict."""

    try:
        with Popen(command, stdout=PIPE, stderr=PIPE, shell=False) as process:  # nosec
            # wait and retrieve stdout/err
            _stdout, _stderr = process.communicate()
            # handle text encoding issues and return stdX
            return {
                "stdout": _stdout.decode("utf8", errors="backslashreplace"),
                "stderr": _stderr.decode("utf8", errors="backslashreplace"),
            }
    except Exception as e:
        print(f"execute: Error while executing command '{command}' : {e}")  # type: ignore[str-bytes-safe]
        raise


def get_lice_licenses() -> list[str]:
    """Call lice to get list of supported licenses"""
    caught = None
    stdX = None
    try:
        stdX = execute(["lice", "--licenses"])
        if stdX["stderr"] == "" and len(stdX["stdout"]) > 100:
            return [line.split()[0] for line in stdX["stdout"].splitlines()]
    except Exception as e:
        caught = e
    raise ValueError(
        f"Couldn't get licenses supported by lice, perhaps it's not installed. ({stdX=})"
    ) from caught


def get_lice_license(license_name: str, author: str, project: str) -> list[str]:
    """Call lice to get list of supported licenses"""
    caught = None
    stdX = None
    try:
        stdX = execute(["lice", "-o", author, "-p", project, license_name])
        if stdX["stderr"] == "" and len(stdX["stdout"]) > 100:
            return stdX["stdout"].replace("\r\n", "\n")
    except Exception as e:
        caught = e
    raise ValueError(f"Couldn't get license from lice ({stdX=})") from caught


def user_input(
    prompt: str,
    accepted: Optional[Union[Iterable, Callable]] = None,
    default: Optional[Any] = None,
) -> Any:
    """Asks user for input, with restrictions on accpetable values.
    `prompt`: appropriate text asking the user for input. Should be straightforward and informative about the kind of data that is asked
    `accepted`: either a function testing if the user input is acceptable, or an iterable containing all acceptable values
    `default`: When given, if the user input is not acceptes, default is returned. When abscent, the user will be prompted again until either
    an accepted value is entered or a KeyboardInterrupt is raised.
    Note: this is only designed to retrieve values of the following types: str, int, float
    """

    # Smart prompt reformat
    if default is not None:
        prompt += f" [default:{default}] "
    if prompt[-1] == ":":
        prompt += " "
    elif prompt[-2:] != ": ":
        prompt += ": "

    def acceptable_UI(ui: Any) -> bool:
        if accepted is None:
            return True
        if callable(accepted):
            return accepted(ui)
        return ui in accepted

    while True:
        # main loop: ask user until an acceptable input is received, or a KeyboradInterrupt ends the program
        _user_input = input(prompt)

        # case: raw user input is accepted
        if acceptable_UI(_user_input):
            return _user_input

        # case: processed user input is accepted
        variations = ["int(_user_input)", "float(_user_input)", "_user_input.lower()"]
        for variation in variations:
            try:
                __user_input = ast.literal_eval(variation)
                if acceptable_UI(__user_input):
                    return __user_input
            except (ValueError, AttributeError):
                pass

        # case: user input is not accepted AND there is a default
        if default is not None:
            return default

        # case: user input is not accepted AND there is no default => notify user, ask again
        print(
            f"Invalid input '{_user_input}'. ",
            (
                f" Please choose one of : {accepted}"
                if accepted is not None and not callable(accepted)
                else ""
            ),
        )


def main() -> None:
    """Contains high-level logic"""

    available_licenses = get_lice_licenses()

    # Get project info
    name = user_input("Project name", accepted=lambda x: len(x) > 0 and " " not in x)
    author = user_input("Project author", accepted=lambda x: len(x) > 0)
    author_email = user_input(
        "Project author's email address", accepted=lambda x: len(x) > 0 and "@" in x
    )
    project_repo_site = user_input(
        "Repository site", accepted=lambda x: "." in x, default="https://github.com"
    )
    repo_url = user_input(
        "Project repository URL",
        accepted=lambda x: "." in x and "/" in x,
        default=f"{project_repo_site}/{author}/{name}",
    )
    short_description = user_input(
        "Short project description", accepted=lambda x: len(x) > 0
    )
    is_single_module_package = (
        user_input(
            f"Is {name} a single-module package ? [y/n]",
            accepted=["y", "n"],
            default="n",
        )
        == "y"
    )
    add_vscode_black_settings = (
        user_input(
            "Add .vscode/settings.json file with Black config ? [y/n]",
            accepted=["y", "n"],
            default="n",
        )
        == "y"
    )
    license_name = user_input(
        f"Choose a license [{','.join(available_licenses)}]",
        accepted=available_licenses,
    )
    min_py_ver = user_input(f"Minimum Python version", default=DEFAULT_MIN_PY_VER)

    package_name = f"{name}-{author}"
    print(f"Package name: '{package_name}'")

    # create file structure (raises IOError on existing dirs)
    root_path: Path = CWD / name
    src_path = root_path / "src"
    module_path = src_path if is_single_module_package else src_path / name
    docs_path = root_path / "docs"
    root_path.mkdir()
    src_path.mkdir()
    if not is_single_module_package:
        module_path.mkdir()
    docs_path.mkdir()

    # Create standard files
    (root_path / "CHANGELOG.md").write_text(CHANGELOG_FILE_CONTENT, encoding="utf8")
    (root_path / "LICENSE").write_text(
        get_lice_license(license_name, author, name), encoding="utf8"
    )
    (root_path / "README.md").write_text(
        README_FILE_CONTENT(name, repo_url, short_description), encoding="utf8"
    )
    if is_single_module_package:
        (module_path / (name + ".py")).touch()
    else:
        (module_path / "__init__.py").touch()

    # Create Python-specific gitignore file
    (root_path / ".gitignore").write_text(GITIGNORE_FILE_CONTENT, encoding="utf8")

    # Create Pypi package config file
    (root_path / "pyproject.toml").write_text(
        PYPROJECT_FILE_CONTENT(
            author, author_email, package_name, repo_url, short_description, min_py_ver
        ),
        encoding="utf8",
    )

    # Create code analysis files
    (root_path / "analyze_code.bat").write_text(
        ANALYZE_CODE_BAT_FILE_CONTENT, encoding="utf8", newline="\r\n"
    )
    (root_path / "analyze_code.sh").write_text(
        ANALYZE_CODE_SH_FILE_CONTENT, encoding="utf8", newline="\n"
    )
    (root_path / "requirements-analyze.txt").write_text(
        "mypy\nbandit\npylint\nflake8", encoding="utf8"
    )

    # Create documentation-related files
    (root_path / "requirements-documentation.txt").write_text(
        "furo>=2023\nSphinx>=6.1.3", encoding="utf8"
    )
    (docs_path / "sphinx-full-rebuild.bat").write_text(
        SPHINX_REBUILD_BAT_FILE_CONTENT(name, author), encoding="utf8", newline="\r\n"
    )
    (docs_path / "sphinx-full-rebuild.sh").write_text(
        SPHINX_REBUILD_SH_FILE_CONTENT(name, author), encoding="utf8", newline="\n"
    )
    (docs_path / "sphinx-patch-conf.py").write_text(
        SPHINX_PATCH_CONF_FILE_CONTENT, encoding="utf8"
    )

    # Conditionally add VSCode Black config
    if add_vscode_black_settings:
        print(
            "You will need Microsoft's Black extension 'Black Formatter' for VSCode: https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter"
        )
        vscode_dir_path = root_path / ".vscode"
        vscode_dir_path.mkdir()
        (vscode_dir_path / "settings.json").write_text(
            VSCODE_SETTING_FILE_CONTENT, encoding="utf8"
        )


if __name__ == "__main__":
    main()
    print("END OF PROGRAM")
