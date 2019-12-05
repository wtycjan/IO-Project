import python_files

Files_with_code = python_files.FileInDirectory()

result2 = Files_with_code.list_directory('.\\', 'py')  # przeszukanie katalogu ,aby znaleźć pliki z rozszerzeniem py

my_catalogs = []  # lista przechowująca liste plików
for el in result2:
    my_catalogs.append(el.split('.')[0])


def counting_lines_of_code(el):  # funkcja podająca rozmiar pliku w linijkach kodu
    try:
        with open(el, 'r') as f:
            lines = 0
            for line in f:
                if line != '\n':
                    lines += 1
            return lines

    except IndexError as m:
        print(m)
        print("Lack of file")


def write_to_file_fun_data(list1, list2):
    fi = open('function_weight.txt', 'a')
    for el in list1:
        counter = 0
        for element in list2:
            if el == element:
                counter += 1
        # fi.write(el)
        # fi.write("\n")
        fi.write(str(counter))
        fi.write("\n")
    fi.write("dane")
    fi.write("\n")
    fi.close()
