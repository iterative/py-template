import shutil
from pathlib import Path


if not {{cookiecutter.docs}}:  # noqa: F821
    shutil.rmtree("docs")
    (Path(".github") / "workflows" / "docs.yml").unlink()
    Path("mkdocs.yml").unlink()
