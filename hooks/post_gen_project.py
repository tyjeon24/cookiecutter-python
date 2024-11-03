from pathlib import Path
import shutil

template_dir = Path("../{{cookiecutter.project_name}}")
project_dir_name = Path().absolute().parent.name
 
def update_pyproject():
    toml_target = Path("../pyproject.toml")
    toml_template = Path("pyproject.toml")

    toml_target.write_text(toml_target.read_text() + toml_template.read_text())

def setup_logging_config():
    init_template = Path("src/{{cookiecutter.project_name}}/__init__.py")
    logging_template = Path("src/{{cookiecutter.project_name}}/logging_config.py")
    
    init_target = Path(f"../src/{project_dir_name}/{init_template.name}")
    logging_target = Path(f"../src/{project_dir_name}/{logging_template.name}")
    
    init_target.write_text(init_template.read_text())
    logging_target.write_text(logging_template.read_text())

update_pyproject()
setup_logging_config()

shutil.rmtree(template_dir)