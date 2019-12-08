<<<<<<< HEAD
import FilesClass
import FunctionsClass
import ModulesClass
import RegistrationClass
import python_files
import functions


def main():
    modul = ModulesClass.Modules()
    fun = FunctionsClass.Functions()
    file = FilesClass.Files()
    register = RegistrationClass.Registration()

    Files_with_code = python_files.FileInDirectory()
    result = Files_with_code.list_directory('.\\', 'py')

    FilesClass.Files.checking_connections_between_files(result)

    function_list1 = FunctionsClass.Functions.checking_connections_between_functions1(result)
    function_list2 = fun.checking_weight_of_connections_between_functions(result, function_list1)
    weight_fun = functions.write_to_file_fun_data(function_list1, function_list2)
    FunctionsClass.Functions.checking_connections_between_functions(result,weight_fun)

    modul_list = ModulesClass.Modules.searching_for_used_modules(result)
    ModulesClass.Modules.checking_connections_between_modules(result, modul_list)
    RegistrationClass.Registration.write_to_file(FilesClass.Files.filesConnectionList,
                                                 FunctionsClass.Functions.functionsConnectionList,
                                                 ModulesClass.Modules.modulConnectionList)

    RegistrationClass.Registration.write_to_file(
        FilesClass.Files.filesConnectionWeight,
        FunctionsClass.Functions.functionsConnectionWeight,
        ModulesClass.Modules.modulConnectionWeight)


main()
=======
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
>>>>>>> origin/master
