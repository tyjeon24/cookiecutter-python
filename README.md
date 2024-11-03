# cookiecutter-python

```
python -m cookiecutter https://github.com/tyjeon24/cookiecutter-python
```

1. `pyproject.toml`
   1. Setup dev dependencies : pytest, ipykernel and ruff
   2. Setup ruff config
   3. Add pdm source for CUDA 11.8
2. `src/project/`
   1. `__init__.py, logging_config.py`: Setup logging config