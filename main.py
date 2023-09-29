# MBAIGOLNOUDJI CHRISTIAN MASTER II Data Analyst

from pathlib import Path
import shutil
import pandas as pd

# creer une liste de repertoire
def create_repertories(dir_list):
    list(map(lambda x: Path(x).mkdir(parents=True, exist_ok=True), dir_list))

#methodes pour creer une liste de fichier
def create_files(file_list):
    list(map(lambda x: Path(x).touch(exist_ok=True), file_list))

#definir la liste des dossiers
def dir_list():
    return ["data/cleaned","data/processed","data/raw", "docs", "models", "notebooks", "reports", "src"]

#definir la liste des fichiers
def file_list():
    return ["LICENSE", "Makefile", "README.md","notebooks/main.ipynb", ".gitignore", "requirements.txt","src/utils.py","src/process.py","src/train.py"]

#copier le fichier csc titanic de mon document vers le dossier raw du dossier
def get_rawdata():
    source_path='C:\\Users\\NOUDJICHRIS\\Documents\\titanic.csv'
    destination_path ='C:\\Users\\NOUDJICHRIS\\Documents\\IA BD II\\Outil versioning\\Examen Outil Versioning\\data\\raw'
    shutil.copy(source_path,destination_path)

#nettoyer les données
def clean_data():
    # Identification des valeurs manquantes
    df = pd.read_csv("data/raw/titanic.csv")
    missing_values = df.isnull().sum()

    # Suppression des données dupliquées
    df.drop_duplicates(inplace=True)

    # Sauvegarder les données nettoyées dans le dossier cleaned data
    df.to_csv("data/cleaned/titanic.csv")