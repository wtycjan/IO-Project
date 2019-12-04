import glob
from os import *
def list_directory(directory, extd):
    # funkcja, która wyszukuje wszystkie pliki o danym rozszerzeniu(extd) w danym katalogu(directory)
    python_file = []
    for x in glob.glob('{}*.{}'.format(directory, extd)):
        python_file.append(path.split(x)[1])

    return python_file