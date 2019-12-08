import functions


class Functions(object):

    def __init__(self):
        Functions.functionsConnectionList = []
        Functions.functionsConnectionWeight = []

    FunctionsConnectionList = []
    FunctionsConnectionWeight = []

    @classmethod
    def checking_connections_between_functions1(cls, file_list):  # funkcja sprawdzająca jak funkcje są połączone z sobą
        try:
            functions_list = []
            for actually_file in file_list:
                with open(actually_file, 'r') as f:
                    numbers_of_code_lines_of_actually_file = functions.counting_lines_of_code(actually_file)
                    for line in f:
                        split_text = line.split()
                        if split_text and split_text[0] == "def":
                            tmp = split_text[1].split('(')
                            if tmp[0] != "__init__":
                                functions_list.append(tmp[0])

            return functions_list

        except IndexError as m:
            print(m)
            print("Lack of file")

    @classmethod
    def checking_connections_between_functions(cls, file_list,
                                               weight_list):  # funkcja sprawdzająca jak funkcje są połączone z sobą
        try:
            i = 0
            for actually_file in file_list:
                element = actually_file.split(".")
                with open(actually_file, 'r') as f:
                    numbers_of_code_lines_of_actually_file = functions.counting_lines_of_code(actually_file)
                    for line in f:
                        split_text = line.split()
                        if split_text and split_text[0] == "def":
                            tmp = split_text[1].split('(')
                            if tmp[0] != "__init__":
                                Functions.functionsConnectionList.append(tmp[0] + "[{}]".format(str(weight_list[i])))
                                Functions.functionsConnectionList.append(
                                    element[0] + "[{}]".format(numbers_of_code_lines_of_actually_file))
                                i += 1
            for el in range(int(len(Functions.functionsConnectionList) / 2)):
                Functions.functionsConnectionWeight.append(str(1))


        except IndexError as m:
            print(m)
            print("Lack of file")

    def checking_weight_of_connections_between_functions(self, file_list,
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

    # @classmethod
    # def checking_weight_of_connections_between_functions(cls, file_list,
    #                                                      function_list):  # funkcja sprawdzająca wagi połączeń między funkcjami
    #     try:
    #         for actually_file in file_list:
    #             actually_function_list = []
    #             with open(actually_file, 'r') as f:
    #                 for line in f:
    #                     split_text = line.split()
    #                     if split_text and split_text[0] != 'import':
    #                         if split_text[0] == "def":
    #                             for line1 in f:
    #                                 split_text = line1.split()
    #                                 if split_text and split_text[0] != 'import':
    #                                     for element1 in actually_function_list:
    #                                         if split_text[0] == "def" and split_text[1] == element1:
    #                                             print(element1)
    #
    #
    #                                 else:
    #                                     actually_function_list.append('xd')
    #                                     cls.checking_weight_of_connections_between_functions(file_list,
    #                                                                                          function_list)
    #
    #
    #
    #
    #
    #     except IndexError as m:
    #         print(m)
    #         print("Lack of file")