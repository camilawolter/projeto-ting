import sys
from pathlib import Path


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        return sys.stderr.write("Formato inválido\n")

    file_patch = Path(path_file)
    try:
        return file_patch.read_text().splitlines()
    except FileNotFoundError:
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
