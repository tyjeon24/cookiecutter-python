from pathlib import Path
import shutil

template_dir = Path("../{{cookiecutter.project_name}}")
project_dir_name = Path().absolute().parent.name


def update_pyproject():
    toml_target = Path("../pyproject.toml")
    toml_template = Path("pyproject.toml")

    toml_target.write_text(toml_target.read_text() + toml_template.read_text())


def write_file(source, target):
    target.write_text(source.read_text())
    print(f"Moved {source.absolute()} to {target.absolute()}")


def setup_logging_config():
    init_template = Path("src/{{cookiecutter.project_name}}/__init__.py")
    init_target = Path(f"../src/{project_dir_name}/{init_template.name}")

    logging_template = Path("src/{{cookiecutter.project_name}}/logging_config.py")
    logging_target = Path(f"../src/{project_dir_name}/{logging_template.name}")

    write_file(init_template, init_target)
    write_file(logging_template, logging_target)


def setup_pre_commit():
    pre_commit_template = Path(".pre-commit-config.yaml")
    pre_commit_target = Path(f"../.pre-commit-config.yaml")

    write_file(pre_commit_template, pre_commit_target)


update_pyproject()
setup_logging_config()
setup_pre_commit()

shutil.rmtree(template_dir)
