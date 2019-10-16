from os import *
import glob


def list_directory(directory, extd):
    python_file = []
    for x in glob.glob('{}*.{}'.format(directory, extd)):
        python_file.append(path.split(x)[1])

    return python_file
