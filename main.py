import functions
import python_files


result = python_files.list_directory('.\\', 'py')

functions.how_many_lines(result)
functions.file_connect(result)

functions.file_connect_weight(result)
x = functions.list_of_lines('connect_weight.txt')
final_weight = list(x)
temp = final_weight[1]
final_weight[1] = final_weight[0]
final_weight[0] = temp
with open('graf.txt', 'a') as f:
    for el in final_weight:
        f.write(str(el))
        f.write('\n')


