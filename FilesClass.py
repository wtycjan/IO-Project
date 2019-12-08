import functions


class Files(object):

    def __init__(self):
        Files.filesConnectionList = []
        Files.filesConnectionWeight = []

    FilesConnectionList = []
    FilesConnectionWeight = []

    @classmethod
    def checking_weight_of_connections_between_files(cls,
                                                     actually_file,
                                                     connect_file):  # funkcja sprawdzająca jak pliki są połaczone z sobą
        try:
            with open(actually_file, 'r') as f:
                weight = 0
                for line in f:
                    split_text = line.split()  # zmienna zawierająca elemnty danej linijki kodu
                    if split_text and split_text[0] != 'import':
                        for el in split_text:
                            split_text_next_lvl = el.split(
                                '.')  # zmienna zawierająca elementy z zmiennej polaczenia
                            for el_next in split_text_next_lvl:
                                if el_next == str(connect_file):
                                    weight += 1
            return weight


        except IndexError as m:
            print(m)
            print("Lack of file")

    @classmethod
    def checking_connections_between_files(cls, file_list):  # funkcja, która sprawdza jakie pliki są z sobą połaczone
        try:
            for actually_file in file_list:
                element = actually_file.split(".")
                connect_file_list = []
                with open(actually_file, 'r') as f:
                    numbers_of_code_lines_of_actually_file = functions.counting_lines_of_code(actually_file)
                    for line in f:
                        split_text = line.split()
                        if split_text and (split_text[0] == 'import' or split_text[0] == "from"):
                            for file in functions.my_catalogs:
                                if split_text[1] == file:
                                    connect_file_list.append(split_text[1])
                for amount in range(len(connect_file_list)):
                    numbers_of_code_lines_of_actually_connected_file = functions.counting_lines_of_code(
                        connect_file_list[amount] + ".py")
                    file_connection_weight = cls.checking_weight_of_connections_between_files(actually_file,
                                                                                              connect_file_list[amount])

                    Files.filesConnectionList.append(element[0] + "[{}]".format(numbers_of_code_lines_of_actually_file))
                    Files.filesConnectionList.append(str(
                        connect_file_list[amount]) + "[{}]".format(numbers_of_code_lines_of_actually_connected_file))
                    Files.filesConnectionWeight.append(str(file_connection_weight))

        except IndexError as m:
            print(m)
            print("Lack of file")