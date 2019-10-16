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

                fi.write(element[0])
                fi.write('\n')
                fi.write(str(lines))
                fi.write("\n")
    except IndexError as m:
        print(m)
        print("Lack of file")



#funkcja zlicza ilość różnych linii, jako wartość przyjmuje ścieżke do pliku, zwraca serie
def list_of_lines(file):
    list_of_lines = []
    with open(file, 'r') as f:
        for linia in f:
            list_of_lines.append(linia)

    list_of_lines = pd.Series(list_of_lines)
    unique_values = list_of_lines.value_counts()

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
                fi.write(element[0])
                fi.write('\n')
                fi.write(str(zmienna_do_polaczen[amount]))
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
                                        fi.write("{} - {}".format(first,el_dalej))
                                        fi.write('\n')
        fi.close()

    except IndexError as m:
        print(m)
        print("Lack of file")


