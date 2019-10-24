import functions
import python_files


result = python_files.list_directory('.\\', 'py')

functions.how_many_lines(result)
functions.file_connect(result)

functions.file_connect_weight(result)
function_list1 = functions.function_connect(result)
function_list2 = functions.function_connect_weight(result, function_list1)
functions.write_to_file_fun_data(function_list1,function_list2)
x = functions.list_of_lines('connect_weight.txt')
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



