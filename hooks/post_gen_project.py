from pathlib import Path
import shutil

ROOT = Path().absolute().parent
COOKIECUTTER_ROOT = Path().absolute()


def update_pyproject():
    toml_from = COOKIECUTTER_ROOT / Path("pyproject.toml")
    toml_to = ROOT / Path("pyproject.toml")

    toml_to.write_text(toml_to.read_text() + toml_from.read_text())
    print(f"[Update] {toml_to.absolute()}")


def setup_logging_config():
    config_dir_cookiecutter = COOKIECUTTER_ROOT / Path("config")
    config_dir = ROOT / Path("config")
    config_dir.mkdir()

    init_from = config_dir_cookiecutter / Path("__init__.py")
    init_to = config_dir / Path("__init__.py")
    init_to.write_text(init_from.read_text())
    print(f"[Add] {init_to.absolute()}")

    logging_from = config_dir_cookiecutter / Path("logging_config.py")
    logging_to = config_dir / Path("logging_config.py")
    logging_to.write_text(logging_from.read_text())
    print(f"[Add] {logging_to.absolute()}")


def setup_pre_commit():
    pre_commit_from = COOKIECUTTER_ROOT / Path(".pre-commit-config.yaml")
    pre_commit_to = ROOT / Path(".pre-commit-config.yaml")
    pre_commit_to.write_text(pre_commit_from.read_text())
    print(f"[Add] {pre_commit_to.absolute()}")


update_pyproject()
setup_logging_config()
setup_pre_commit()


shutil.rmtree(COOKIECUTTER_ROOT)
