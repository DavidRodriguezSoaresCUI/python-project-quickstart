# pylint: disable=C3001
"""A simple script to quickly set up a python project (see README.md)
"""

import ast
from pathlib import Path
from typing import Any, Callable, Iterable, Optional, Union


CWD = Path(".")
CHANGELOG_FILE_CONTENT = "# Changelog\n\nAll notable changes to this project will be documented in this file.\n\nThe format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).\n\n<!-- As much as possible use subsections: Added, Removed, Modified, BugFix -->\n\n<!-- ## [0.1] - date\n\n__INITIAL RELEASE__ -->"
LICENSE_FILE_CONTENT = 'CC0 1.0 Universal\n\nStatement of Purpose\n\nThe laws of most jurisdictions throughout the world automatically confer exclusive Copyright and Related Rights (defined below) upon the creator and subsequent owner(s) (each and all, an "owner") of an original work of authorship and/or a database (each, a "Work").\n\nCertain owners wish to permanently relinquish those rights to a Work for the purpose of contributing to a commons of creative, cultural and scientific works ("Commons") that the public can reliably and without fear of later claims of infringement build upon, modify, incorporate in other works, reuse and redistribute as freely as possible in any form whatsoever and for any purposes, including without limitation commercial purposes. These owners may contribute to the Commons to promote the ideal of a free culture and the further production of creative, cultural and scientific works, or to gain reputation or greater distribution for their Work in part through the use and efforts of others.\n\nFor these and/or other purposes and motivations, and without any expectation of additional consideration or compensation, the person associating CC0 with a Work (the "Affirmer"), to the extent that he or she is an owner of Copyright and Related Rights in the Work, voluntarily elects to apply CC0 to the Work and publicly distribute the Work under its terms, with knowledge of his or her Copyright and Related Rights in the Work and the meaning and intended legal effect of CC0 on those rights.\n\n1. Copyright and Related Rights. A Work made available under CC0 may be protected by copyright and related or neighboring rights ("Copyright and Related Rights"). Copyright and Related Rights include, but are not limited to, the following:\n\n    the right to reproduce, adapt, distribute, perform, display, communicate, and translate a Work;\n    moral rights retained by the original author(s) and/or performer(s);\n    publicity and privacy rights pertaining to a person\'s image or likeness depicted in a Work;\n    rights protecting against unfair competition in regards to a Work, subject to the limitations in paragraph 4(a), below;\n    rights protecting the extraction, dissemination, use and reuse of data in a Work;\n    database rights (such as those arising under Directive 96/9/EC of the European Parliament and of the Council of 11 March 1996 on the legal protection of databases, and under any national implementation thereof, including any amended or successor version of such directive); and\n    other similar, equivalent or corresponding rights throughout the world based on applicable law or treaty, and any national implementations thereof.\n\n2. Waiver. To the greatest extent permitted by, but not in contravention of, applicable law, Affirmer hereby overtly, fully, permanently, irrevocably and unconditionally waives, abandons, and surrenders all of Affirmer\'s Copyright and Related Rights and associated claims and causes of action, whether now known or unknown (including existing as well as future claims and causes of action), in the Work (i) in all territories worldwide, (ii) for the maximum duration provided by applicable law or treaty (including future time extensions), (iii) in any current or future medium and for any number of copies, and (iv) for any purpose whatsoever, including without limitation commercial, advertising or promotional purposes (the "Waiver"). Affirmer makes the Waiver for the benefit of each member of the public at large and to the detriment of Affirmer\'s heirs and successors, fully intending that such Waiver shall not be subject to revocation, rescission, cancellation, termination, or any other legal or equitable action to disrupt the quiet enjoyment of the Work by the public as contemplated by Affirmer\'s express Statement of Purpose.\n\n3. Public License Fallback. Should any part of the Waiver for any reason be judged legally invalid or ineffective under applicable law, then the Waiver shall be preserved to the maximum extent permitted taking into account Affirmer\'s express Statement of Purpose. In addition, to the extent the Waiver is so judged Affirmer hereby grants to each affected person a royalty-free, non transferable, non sublicensable, non exclusive, irrevocable and unconditional license to exercise Affirmer\'s Copyright and Related Rights in the Work (i) in all territories worldwide, (ii) for the maximum duration provided by applicable law or treaty (including future time extensions), (iii) in any current or future medium and for any number of copies, and (iv) for any purpose whatsoever, including without limitation commercial, advertising or promotional purposes (the "License"). The License shall be deemed effective as of the date CC0 was applied by Affirmer to the Work. Should any part of the License for any reason be judged legally invalid or ineffective under applicable law, such partial invalidity or ineffectiveness shall not invalidate the remainder of the License, and in such case Affirmer hereby affirms that he or she will not (i) exercise any of his or her remaining Copyright and Related Rights in the Work or (ii) assert any associated claims and causes of action with respect to the Work, in either case contrary to Affirmer\'s express Statement of Purpose.\n\n4. Limitations and Disclaimers.\n\n    No trademark or patent rights held by Affirmer are waived, abandoned, surrendered, licensed or otherwise affected by this document.\n    Affirmer offers the Work as-is and makes no representations or warranties of any kind concerning the Work, express, implied, statutory or otherwise, including without limitation warranties of title, merchantability, fitness for a particular purpose, non infringement, or the absence of latent or other defects, accuracy, or the present or absence of errors, whether or not discoverable, all to the greatest extent permissible under applicable law.\n    Affirmer disclaims responsibility for clearing rights of other persons that may apply to the Work or any use thereof, including without limitation any person\'s Copyright and Related Rights in the Work. Further, Affirmer disclaims responsibility for obtaining any necessary consents, permissions or other rights required for any use of the Work.\n    Affirmer understands and acknowledges that Creative Commons is not a party to this document and has no duty or obligation with respect to this CC0 or use of the Work.'
README_FILE_CONTENT = (
    lambda project_name, repo_url, short_description: f"# [{project_name}]({repo_url}) - {short_description}\n\nPut a description here"
)
GITIGNORE_FILE_CONTENT = "# Byte-compiled / optimized / DLL files\n__pycache__/\n*.py[cod]\n*$py.class\n\n# C extensions\n*.so\n\n# Distribution / packaging\n.Python\nbuild/\ndevelop-eggs/\ndist/\ndownloads/\neggs/\n.eggs/\nlib/\nlib64/\nparts/\nsdist/\nvar/\nwheels/\npip-wheel-metadata/\nshare/python-wheels/\n*.egg-info/\n.installed.cfg\n*.egg\nMANIFEST\n\n# PyInstaller\n#  Usually these files are written by a python script from a template\n#  before PyInstaller builds the exe, so as to inject date/other infos into it.\n*.manifest\n*.spec\n\n# Installer logs\npip-log.txt\npip-delete-this-directory.txt\n\n# Unit test / coverage reports\nhtmlcov/\n.tox/\n.nox/\n.coverage\n.coverage.*\n.cache\nnosetests.xml\ncoverage.xml\n*.cover\n*.py,cover\n.hypothesis/\n.pytest_cache/\n\n# Translations\n*.mo\n*.pot\n\n# Django stuff:\n*.log\nlocal_settings.py\ndb.sqlite3\ndb.sqlite3-journal\n\n# Flask stuff:\ninstance/\n.webassets-cache\n\n# Scrapy stuff:\n.scrapy\n\n# Sphinx documentation\ndocs/_build/\n\n# PyBuilder\ntarget/\n\n# Jupyter Notebook\n.ipynb_checkpoints\n\n# IPython\nprofile_default/\nipython_config.py\n\n# pyenv\n.python-version\n\n# pipenv\n#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.\n#   However, in case of collaboration, if having platform-specific dependencies or dependencies\n#   having no cross-platform support, pipenv may install dependencies that don't work, or not\n#   install all needed dependencies.\n#Pipfile.lock\n\n# PEP 582; used by e.g. github.com/David-OConnor/pyflow\n__pypackages__/\n\n# Celery stuff\ncelerybeat-schedule\ncelerybeat.pid\n\n# SageMath parsed files\n*.sage.py\n\n# Environments\n.env\n.venv\nenv/\nvenv/\nENV/\nenv.bak/\nvenv.bak/\n\n# Spyder project settings\n.spyderproject\n.spyproject\n\n# Rope project settings\n.ropeproject\n\n# mkdocs documentation\n/site\n\n# mypy\n.mypy_cache/\n.dmypy.json\ndmypy.json\n\n# Pyre type checker\n.pyre/\n\n# VSCode local settings\n.vscode/settings.json\n\n# static code analysis report\nanalyze_code.report.txt\n"
VSCODE_SETTING_FILE_CONTENT = '{\n    "[python]": {\n        "editor.defaultFormatter": "ms-python.black-formatter",\n        "editor.formatOnSave": true\n    }\n}'
PYPROJECT_FILE_CONTENT = (
    lambda author, author_email, package_name, repo_url, short_description: f'[build-system]\nrequires = ["setuptools>=61.0"]\nbuild-backend = "setuptools.build_meta"\n\n[project]\nname = "{package_name}"\nversion = "0.1"\nauthors = [\n  {{ name="{author}", email="{author_email}" }},\n]\ndescription = "{short_description}"\nreadme = "README.md"\nlicense = {{ file = "LICENSE" }}\nrequires-python = ">=3.7"\nclassifiers = [\n    "Development Status :: 3 - Alpha",\n    "Programming Language :: Python :: 3",\n    "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",\n    "Operating System :: OS Independent",\n]\n\n[project.urls]\n"Homepage" = "{repo_url}"\n"Bug Tracker" = "{repo_url}/issues"'
)
ANALYZE_CODE_BAT_FILE_CONTENT = '@echo off\nSET report_file=analyze_code.report.txt\n\nsetlocal enabledelayedexpansion enableextensions\nset FILE_LIST=\nfor /R . %%F IN (*.py) do (\n    set FILE_LIST=!FILE_LIST! "%%F"\n)\nset FILE_LIST=%FILE_LIST:~1%\n\nECHO Analyzing with MYPY\nECHO ==== MYPY ==== >%report_file%\nECHO (Disable false positives with inline comment "# type: ignore[<ERROR_NAME>]") >>%report_file%\nmypy %FILE_LIST% >>%report_file%\n\nECHO Analyzing with BANDIT\nECHO ==== BANDIT ==== >>%report_file%\nECHO (Disable false positives with inline comment "# nosec <ERROR_CODE>") >>%report_file%\nbandit %FILE_LIST% 1>>%report_file% 2>NUL\n\nECHO Analyzing with PYLINT\nECHO ==== PYLINT ==== >>%report_file%\npylint %FILE_LIST% >>%report_file%\n\nECHO Analyzing with FLAKE8\nECHO ==== FLAKE8 ==== >>%report_file%\npython -m flake8 %FILE_LIST% >>%report_file%\n'
ANALYZE_CODE_SH_FILE_CONTENT = "report_file=analyze_code.report.txt\n\nFILE_LIST=$(find src -type f -iname \"*.py\" -printf '%p ')\n\necho Analyzing with MYPY\necho ==== MYPY ==== >${report_file}\necho \"(Disable false positives with inline comment '# type: ignore[<ERROR_NAME>]')\" >>${report_file}\nmypy $FILE_LIST >>${report_file}\n\necho Analyzing with BANDIT\necho ==== BANDIT ==== >>${report_file}\necho \"(Disable false positives with inline comment '# nosec <ERROR_CODE>')\" >>${report_file}\nbandit $FILE_LIST 1>>${report_file} 2>NUL\n\necho Analyzing with PYLINT\necho ==== PYLINT ==== >>${report_file}\npylint $FILE_LIST >>${report_file}\n\necho Analyzing with FLAKE8\necho ==== FLAKE8 ==== >>${report_file}\nflake8 $FILE_LIST >>${report_file}\n"
INDEX_RST_FILE_CONTENT = "Welcome to {module_name}'s documentation!\n==================================\n\n.. automodule:: {module_name}\n   :members:\n   :undoc-members:\n   :show-inheritance:\n\n.. toctree::\n   :maxdepth: 2\n   :caption: Contents:\n\nFind more\n---------\n\n* :ref:`genindex`\n* :ref:`modindex`\n* :ref:`search`"
SPHINX_REBUILD_BAT_FILE_CONTENT = (
    lambda project_name, author: f'@echo off\n\necho Rebuilding source directory\nRD /S /Q ".\source"\nsphinx-apidoc -f --maxdepth 4 --separate --doc-project "{project_name}" --doc-author "{author}" --full -o source ../src/FFmpyg\npython sphinx-patch-conf.py\n\necho Rebuilding HTML build\nRD /S /Q ".\\build"\nsphinx-build source build\necho Done ! Open build/index.html to see documentation'
)
SPHINX_REBUILD_SH_FILE_CONTENT = (
    lambda project_name, author: f'#! /bin/bash\n\necho Rebuilding source directory\nfind ./source -mindepth 1 -delete 2>/dev/null\nrmdir ./source\nsphinx-apidoc -f --maxdepth 4 --separate --doc-project "{project_name}" --doc-author "{author}" --full -o source ../src/FFmpyg\npython3 sphinx-patch-conf.py\n\necho Rebuilding HTML build\nfind ./build -mindepth 1 -delete 2>/dev/null\nrmdir ./build\nsphinx-build source build\necho Done ! Open build/index.html to see documentation'
)
SPHINX_PATCH_CONF_FILE_CONTENT = "from pathlib import Path\n\n\ndef main() -> None:\n    conf_file = Path('./source/conf.py')\n    conf = conf_file.read_text(encoding='utf8')\n    if not 'sys.path.insert' in conf:\n        conf_file.write_text(\n            \"import os\\nimport sys\\nsys.path.insert(0, os.path.abspath('../../src/'))\\n\"\n            + conf.replace(\"html_theme = 'alabaster'\", \"html_theme = 'furo'\"),\n            encoding='utf8'\n        )\n\n\nif __name__ == '__main__':\n    main()\n"


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
    add_vscode_black_settings = (
        user_input(
            "Add .vscode/settings.json file with Black config [y/n]",
            accepted=["y", "n"],
            default="n",
        )
        == "y"
    )
    # add_vscode_black_settings = True
    package_name = f"{name}_{author}"
    print(f"Package name: '{package_name}'")

    # create file structure (raises IOError on existing dirs)
    root_path: Path = CWD / name
    src_path = root_path / "src"
    module_path = src_path / package_name
    docs_path = root_path / "docs"
    root_path.mkdir()
    src_path.mkdir()
    module_path.mkdir()
    docs_path.mkdir()

    # Create standard files
    (root_path / "CHANGELOG.md").write_text(CHANGELOG_FILE_CONTENT, encoding="utf8")
    (root_path / "LICENSE").write_text(LICENSE_FILE_CONTENT, encoding="utf8")
    (root_path / "README.md").write_text(
        README_FILE_CONTENT(name, repo_url, short_description), encoding="utf8"
    )
    (module_path / "__init__.py").touch()

    # Create Python-specific gitignore file
    (root_path / ".gitignore").write_text(GITIGNORE_FILE_CONTENT, encoding="utf8")

    # Create Pypi package config file
    (root_path / "pyproject.toml").write_text(
        PYPROJECT_FILE_CONTENT(
            author, author_email, package_name, repo_url, short_description
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
