import pandas

import python_files

result2 = python_files.list_directory('.\\', 'py')  # przeszukanie katalogu ,aby znaleźć pliki z rozszerzeniem py

my_catalogs = []  # lista przechowująca liste plików
for el in result2:
    my_catalogs.append(el.split('.')[0])


def counting_lines_of_code(file_list):  # funkcja podająca rozmiar pliku w linijkach kodu
    try:
        for el in file_list:
            element = el.split('.')
            with open(el, 'r') as f:
                lines = 0
                for line in f:
                    if line != '\n':
                        lines += 1

            with open('graf.txt', 'a') as fi:

                fi.write("\"" + element[0] + ".py\"")
                fi.write('\n')
                fi.write(str(lines))
                fi.write("\n")
    except IndexError as m:
        print(m)
        print("Lack of file")


def counting_repetitive_lines(
        file_list):  # funkcja zlicza ilość różnych linii, jako wartość przyjmuje ścieżke do pliku, zwraca serie
    list_of_lines1 = []
    with open(file_list, 'r') as f:
        for linia in f:
            list_of_lines1.append(linia)

    list_of_lines1 = pandas.Series(list_of_lines1)
    unique_values = list_of_lines1.value_counts()

    return (unique_values)


def checking_connections_between_files(file_list):  # funkcja, która sprawdza jakie pliki są z sobą połaczone
    try:
        for actually_file in file_list:
            element = actually_file.split(".")
            connect_file_list = []
            with open(actually_file, 'r') as f:
                for line in f:
                    split_text = line.split()
                    if split_text and (split_text[0] == 'import'):
                        for file in my_catalogs:
                            if split_text[1] == file:
                                connect_file_list.append(split_text[1])
            fi = open('graf.txt', 'a')
            for amount in range(len(connect_file_list)):
                fi.write("\"" + element[0] + ".py\"")
                fi.write('\n')
                fi.write("\"" + str(connect_file_list[amount]) + ".py\"")
                fi.write('\n')
            fi.close()

    except IndexError as m:
        print(m)
        print("Lack of file")


def checking_weight_of_connections_between_files(file_list):  # funkcja sprawdzająca jak pliki są połaczone z sobą
    try:
        fi = open('connect_weight.txt', 'a')
        for actually_file in file_list:
            with open(actually_file, 'r') as f:
                for line in f:
                    split_text = line.split()  # zmienna zawierająca elemnty danej linijki kodu
                    if split_text and split_text[0] != 'import':
                        for el in split_text:
                            split_text_next_lvl = el.split('.')  # zmienna zawierająca elementy z zmiennej polaczenia
                            for el_next in split_text_next_lvl:
                                for file in my_catalogs:
                                    if el_next == file:
                                        fi.write("{} - {}.py".format(actually_file, el_next))
                                        fi.write('\n')
        fi.close()

    except IndexError as m:
        print(m)
        print("Lack of file")


def checking_connections_between_functions(file_list):  # funkcja sprawdzająca jak funkcje są połączone z sobą
    try:
        functions_list = []
        for actually_file in file_list:
            with open(actually_file, 'r') as f:
                for line in f:
                    split_text = line.split()
                    if split_text and split_text[0] == "def":
                        tmp = split_text[1].split('(')
                        functions_list.append(tmp[0])

        return functions_list

    except IndexError as m:
        print(m)
        print("Lack of file")


def checking_weight_of_connections_between_functions(file_list,
                                                     function_list):  # funkcja sprawdzająca wagi połączeń między funkcjami
    try:
        how_many_function = []
        for actually_fun in function_list:
            for actually_file in file_list:
                with open(actually_file, 'r') as f:
                    for line in f:
                        split_text = line.split()
                        if split_text and split_text[0] != 'import':
                            for el in split_text:
                                split_text_next_lvl = el.split('.')
                                for el_next in split_text_next_lvl:
                                    split_text_final_lvl = el_next.split('(')
                                    if actually_fun == split_text_final_lvl[0]:
                                        how_many_function.append(split_text_final_lvl[0])
        return how_many_function

    except IndexError as m:
        print(m)
        print("Lack of file")


def final_weight(weight_list):
    temp = weight_list[1]
    weight_list[1] = weight_list[0]
    weight_list[0] = temp
    return weight_list


def write_to_file_fun_data(list1, list2):
    fi = open('function_weight.txt', 'a')
    for el in list1:
        counter = -1
        for element in list2:
            if el == element:
                counter += 1
        fi.write(el)
        fi.write("\n")
        fi.write(str(counter))
        fi.write("\n")
    fi.close()


def searching_for_used_modules(file_list):  # funkcja do wykusziwania zależności między modułami
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


def checking_connections_between_modules(file_list):
    final_list = []
    modul_list = searching_for_used_modules(file_list)
    for actually_modul in modul_list:
        for actually_file in file_list:
            with open(actually_file, 'r') as f:
                for line in f:
                    text_split = line.split()
                    for el in text_split:
                        text_split_next_lvl = el.split('.')
                        if text_split_next_lvl[0] == actually_modul and (len(text_split_next_lvl) > 1):
                            text_split_final_lvl = text_split_next_lvl[1].split('(')
                            final_list.append(actually_file)
                            final_list.append(actually_modul)
                            final_list.append(text_split_final_lvl[0])
                            final_list.append("|")
    return final_list
