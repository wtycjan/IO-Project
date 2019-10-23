import python_files
import pandas as pd

result2 = python_files.list_directory('.\\', 'py')

my_catalogs = []
for el in result2:
    my_catalogs.append(el.split('.')[0])


def how_many_lines(file):

    try:
        for el in file:
            element = el.split('.')
            with open(el, 'r') as f:
                lines = 0
                for line in f:
                    if line != '\n':
                        lines += 1

            with open('graf.txt', 'a') as fi:

                fi.write("\""+element[0]+".py\"")
                fi.write('\n')
                fi.write(str(lines))
                fi.write("\n")
    except IndexError as m:
        print(m)
        print("Lack of file")



#funkcja zlicza ilość różnych linii, jako wartość przyjmuje ścieżke do pliku, zwraca serie
def list_of_lines(file):
    list_of_lines1 = []
    with open(file, 'r') as f:
        for linia in f:
            list_of_lines1.append(linia)

    list_of_lines1 = pd.Series(list_of_lines1)
    unique_values = list_of_lines1.value_counts()

    return(unique_values)


def file_connect(file):
    try:
        for first in file:
            element = first.split(".")
            zmienna_do_polaczen = []
            with open(first, 'r') as f:
                for line in f:
                    polaczenia = line.split()
                    if polaczenia and (polaczenia[0] == 'import'):
                        for plik in my_catalogs:
                            if polaczenia[1] == plik:
                                zmienna_do_polaczen.append(polaczenia[1])
            fi = open('graf.txt', 'a')
            for amount in range(len(zmienna_do_polaczen)):
                fi.write("\""+element[0]+".py\"")
                fi.write('\n')
                fi.write("\""+str(zmienna_do_polaczen[amount])+".py\"")
                fi.write('\n')
            fi.close()

    except IndexError as m:
        print(m)
        print("Lack of file")


def file_connect_weight(file):
    try:
        fi = open('connect_weight.txt', 'a')
        for first in file:
            with open(first, 'r') as f:
                for line in f:
                    polaczenia = line.split()
                    if polaczenia and polaczenia[0] != 'import':
                        for el in polaczenia:
                            polaczenia_dalej = el.split('.')
                            for el_dalej in polaczenia_dalej:
                                for plik in my_catalogs:
                                    if el_dalej == plik:
                                        fi.write("{} - {}.py".format(first,el_dalej))
                                        fi.write('\n')
        fi.close()

    except IndexError as m:
        print(m)
        print("Lack of file")

def function_connect(file):
    try:
        functions_list = []
        for first in file:
            with open(first, 'r') as f:
                for line in f:
                    poloczenia = line.split()
                    if poloczenia and poloczenia[0] == "def":
                        pom = poloczenia[1].split('(')
                        functions_list.append(pom[0])

        return functions_list

    except IndexError as m:
        print(m)
        print("Lack of file")

def function_connect_weight(file, function_list):
    try:
        how_many_function = []
        for cos in function_list:
            for first in file:
                with open(first, 'r') as f:
                    for line in f:
                        polaczenia = line.split()
                        if polaczenia and polaczenia[0] != 'import':
                            for el in polaczenia:
                                polaczenia_dalej = el.split('.')
                                for el_dalej in polaczenia_dalej:
                                    polaczenia_dalej1 = el_dalej.split('(')
                                    if cos == polaczenia_dalej1[0]:
                                        how_many_function.append(polaczenia_dalej1[0])
        return how_many_function


    except IndexError as m:
        print(m)
        print("Lack of file")

def write_to_file_fun_data(list1,list2):
    fun_info = []
    fi = open('function_weight.txt', 'a')
    for el in list1:
        licznik = -1
        for element in list2:
            if el == element:
                licznik += 1
        fi.write(el)
        fi.write("\n")
        fi.write(str(licznik))
        fi.write("\n")
    fi.close()