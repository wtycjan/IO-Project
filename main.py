import functions
import python_files

result = python_files.list_directory('.\\', 'py')

functions.counting_lines_of_code(result)
functions.checking_connections_between_files(result)

functions.checking_weight_of_connections_between_files(result)
function_list1 = functions.checking_connections_between_functions(result)
function_list2 = functions.checking_weight_of_connections_between_functions(result, function_list1)
functions.write_to_file_fun_data(function_list1, function_list2)
x = functions.counting_repetitive_lines('connect_weight.txt')
weight_list = list(x)
weight_list = functions.final_weight(weight_list)
with open('graf.txt', 'a') as f:
    for el in weight_list:
        f.write(str(el))
        f.write('\n')
with open('function_weight.txt', 'a') as f:
    for el in function_list1:
        f.write(el)
        f.write('\n')
with open('function_weight.txt', 'a') as f:
    for el in function_list1:
        f.write(str(0))
        f.write('\n')

modul_list = functions.searching_for_used_modules(result)
modul_list = functions.checking_connections_between_modules(result)