# MBAIGOLNOUDJI CHRISTIAN MASTER II Data Analyst

from pathlib import Path
import shutil
import pandas as pd

# MBAIGOLNOUDJI CHRISTIAN MASTER II Data Analyst
def create_repertories(dir_list):
    list(map(lambda x: Path(x).mkdir(parents=True, exist_ok=True), dir_list))

def create_files(file_list):
    list(map(lambda x: Path(x).touch(exist_ok=True), file_list))

def dir_list():
    return ["data/cleaned","data/processed","data/raw", "docs", "models", "notebooks", "reports", "src"]
def file_list():
    return ["LICENSE", "Makefile", "README.md","notebooks/main.ipynb", ".gitignore", "requirements.txt","src/utils.py","src/process.py","src/train.py"]
