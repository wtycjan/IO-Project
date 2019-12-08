import glob
from os import *


class FileInDirectory(object):

    def __init__(self):
        self.python_file = []

    def list_directory(self, directory, extd):
        # funkcja, która wyszukuje wszystkie pliki o danym rozszerzeniu(extd) w danym katalogu(directory)
        for x in glob.glob('{}*.{}'.format(directory, extd)):
            self.python_file.append(path.split(x)[1])

        return self.python_file
