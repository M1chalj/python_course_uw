import json
import os
from pathlib import Path

JUPYTER_FILE_EXTENSION = '.ipynb'
PYTHON_FILE_EXTENSION = '.py'


def cell_to_string(cell):
    if cell['cell_type'] == 'code':
        sep = ''
        pref = '#%%\n'
    else:  # cell['cell_type'] == 'markdown'
        sep = '# '
        pref = '# '
    return pref + sep.join(cell['source']) + '\n'


def jupyter_to_python(jupyter_file, python_file):
    with open(jupyter_file, 'r') as file:
        dane = json.load(file)

    cells = dane['cells']

    with open(python_file, 'w') as file:
        print('\n'.join(map(cell_to_string, cells)), file=file)


def count_exercises(jupyter_file):
    with open(jupyter_file, 'r') as file:
        dane = json.load(file)

    cells = dane['cells']

    return sum(1 for _ in filter(
        lambda cell: cell['cell_type'] == 'markdown' and len(cell['source']) > 0 and '# Ćwiczenie' in cell['source'][0],
        cells))


filename = input("Podaj nazwę pliku (bez rozszerzenia):")
path_to_file = os.path.join(os.getcwd(), filename)
path_to_jupyter_file = path_to_file + JUPYTER_FILE_EXTENSION
path_to_python_file = path_to_file + PYTHON_FILE_EXTENSION

if not Path(path_to_jupyter_file).exists():
    print("Niepoprawna nazwa pliku")
    exit(0)

jupyter_to_python(path_to_jupyter_file, path_to_python_file)

print("Liczba ćwiczeń:", count_exercises(path_to_jupyter_file))
