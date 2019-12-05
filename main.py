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
