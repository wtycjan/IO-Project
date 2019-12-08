import FilesClass
import FunctionsClass
import ModulesClass


class Registration(FilesClass.Files, FunctionsClass.Functions, ModulesClass.Modules):

    def __init__(self):
        pass

    @classmethod
    def write_to_file(cls, *args):
        with open('graf_jozin.txt', 'a') as fi:
            for list in args:
                for el in list:
                    fi.write(el)
                    fi.write("\n")
            fi.write("dane\n")