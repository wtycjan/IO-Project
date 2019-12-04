import functions
import python_files

result = python_files.list_directory('.\\', 'py')
print(result)
functions.counting_lines_of_code(result)
functions.checking_connections_between_files(result)

functions.checking_weight_of_connections_between_files(result)

function_list1 = functions.checking_connections_between_functions(result)
function_list2 = functions.checking_weight_of_connections_between_functions(result, function_list1)
function_list3=functions.checking_functions_origins(result,function_list1)#lista z zrodlem danej funkcji

functions.write_to_file_fun_data(function_list1, function_list2)

x = functions.counting_repetitive_lines('connect_weight.txt')

weight_list = list(x)

with open('graf.txt', 'a') as f:
    for el in weight_list:
        f.write(str(el))
        f.write('\n')
    f.write("dane")
with open('function_weight.txt', 'a') as f:
    for el in function_list1:
        f.write(el)
        f.write('\n')
    f.write("dane")
    f.write('\n')
with open('function_weight.txt', 'a') as f:
    for el in range(int(len(function_list1)/2)):
        f.write(str(0))
        f.write('\n')
    f.write("dane")
    f.write('\n')
modul_list = functions.searching_for_used_modules(result)
functions.checking_connections_between_modules(result, modul_list)
with open('fun_graf_modul.txt','w') as f:
    f.write('FUNCTION_WEIGHT')
    f.write('\n')
    with open('function_weight.txt','r') as fw:
        for line in fw:
            f.write(line)
    fw.close()
    f.write("FUNCTION_ORIGIN")
    f.write('\n')
    for el in function_list3:
        f.write(el)
        f.write('\n')
    f.write('MODUL_LIST')
    f.write('\n')
    with open('modul.txt','r') as m:
        for line in m:
            f.write(line)
    m.close()
    f.write('GRAF')
    f.write('\n')
    with open('graf.txt','r') as g:
        for line in g:
            f.write(line)
    g.close()
f.close()