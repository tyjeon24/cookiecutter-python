from pathlib import Path
import shutil

ROOT = Path().absolute().parent  # Target project root. - /project
COOKIECUTTER_ROOT = Path().absolute()  # Created directory. - /project/created


def update_pyproject():
    toml_from = COOKIECUTTER_ROOT / Path("pyproject.toml")
    toml_to = ROOT / Path("pyproject.toml")

    toml_to.write_text(
        toml_to.read_text(encoding="utf-8") + toml_from.read_text(encoding="utf-8"),
        encoding="utf-8",
    )
    print(f"[Update] {toml_to.absolute()}")


def setup_logging_config():
    config_dir_cookiecutter = COOKIECUTTER_ROOT / Path("config")
    config_dir = ROOT / Path("config")
    config_dir.mkdir(exist_ok=True)

    init_from = config_dir_cookiecutter / Path("__init__.py")
    init_to = config_dir / Path("__init__.py")
    init_to.write_text(init_from.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"[Add] {init_to.absolute()}")

    logging_from = config_dir_cookiecutter / Path("logging_config.py")
    logging_to = config_dir / Path("logging_config.py")
    logging_to.write_text(logging_from.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"[Add] {logging_to.absolute()}")


def setup_src_init():
    src_dir_cookiecutter = COOKIECUTTER_ROOT / Path("src")
    src_dir = ROOT / Path("src", ROOT.name)

    src_init_from = src_dir_cookiecutter / Path("__init__.py")
    src_init_to = src_dir / Path("__init__.py")
    src_init_to.write_text(src_init_from.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"[Add] {src_init_to.absolute()}")


def setup_pre_commit():
    pre_commit_from = COOKIECUTTER_ROOT / Path(".pre-commit-config.yaml")
    pre_commit_to = ROOT / Path(".pre-commit-config.yaml")
    pre_commit_to.write_text(
        pre_commit_from.read_text(encoding="utf-8"), encoding="utf-8"
    )
    print(f"[Add] {pre_commit_to.absolute()}")


update_pyproject()
setup_logging_config()
setup_src_init()
setup_pre_commit()


shutil.rmtree(COOKIECUTTER_ROOT)
