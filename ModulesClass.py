import functions

class Modules(object):

    def __init__(self):
        Modules.modulConnectionList = []
        Modules.modulConnectionWeight = []

    ModulConnectionList = []
    ModulConnectionWeight = []

    @classmethod
    def searching_for_used_modules(cls, file_list):  # funkcja do wykusziwania zależności między modułami
        names_from_import = []  # lista zawierająca wszystkie nazwy pochodzące z "import" , oraz "from"
        modul_list = []  # lista zawierająca wszystkie moduły
        temporary_list = []  # lista chwilowo przechowująca wartości
        list_of_fileName = []  # lista zawierająca nazwy plików
        for actually_file in file_list:
            text_split = actually_file.split('.')
            list_of_fileName.append(text_split[0])
            with open(actually_file, 'r') as f:
                for line in f:
                    text_split = line.split()
                    if text_split and (text_split[0] == 'import' or text_split[0] == 'from'):
                        names_from_import.append(text_split[1])
        names_from_import = (list(set(names_from_import)))
        for element_of_file in list_of_fileName:  # pętla wyodrędbniająca moduły z listy importów
            for element_of_imports in names_from_import:
                if element_of_file == element_of_imports:
                    temporary_list.append(element_of_file)
        list_of_file_name = temporary_list
        for element_of_file in list_of_file_name:
            for element_of_imports in names_from_import:
                if element_of_file == element_of_imports:
                    names_from_import.remove(element_of_file)
        modul_list = names_from_import
        del temporary_list
        del names_from_import
        del list_of_fileName

        return modul_list

    @classmethod
    def checking_connections_between_modules(cls, file_list,
                                             modul_list):  # funkcja sprawdzająca zależności logiczne między modułami
        final_list = []
        weight_list = []
        for actually_modul in modul_list:
            counter = 0
            for actually_file in file_list:
                with open(actually_file, 'r') as f:
                    numbers_of_code_lines_of_actually_file = functions.counting_lines_of_code(actually_file)
                    actually_file = actually_file.split('.')
                    for line in f:
                        text_split = line.split()
                        if text_split and text_split[0] == 'def':
                            name_of_function = text_split[1]
                            name_of_function = name_of_function.split("(")
                            name_of_function = name_of_function[0]
                        for el in text_split:
                            text_split_next_lvl = el.split('.')
                            if text_split_next_lvl[0] == actually_modul and (len(text_split_next_lvl) > 1):
                                counter += 1
                                text_split_final_lvl = text_split_next_lvl[1].split('(')
                                Modules.modulConnectionList.append(actually_file[0] + "[{}]".format(numbers_of_code_lines_of_actually_file))
                                Modules.modulConnectionList.append(actually_modul)
                                Modules.modulConnectionList.append(name_of_function)
                                Modules.modulConnectionList.append(text_split_final_lvl[0])
                                Modules.modulConnectionWeight.append(str(counter))
                                Modules.modulConnectionWeight.append(str(counter))
