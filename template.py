import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "cnnClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
    "templates/index.html",
    "README.md",
    f"src/{project_name}/entity/config_entity.py"
    f"src/{project_name}/pipeline/data_ingestion.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/components/data_ingestion.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    dir, filename = os.path.split(filepath)
    if dir != "":
        os.makedirs(dir, exist_ok=True)
        logging.info(f"Creating directory: {dir} for the file: {filename}")
        
    if not os.path.exists(filepath) or (os.path.getsize(filepath == 0)):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filename} inside the directory: {dir}")
    else:
        logging.info(f"File {filename} already exists inside the directory: {dir}")