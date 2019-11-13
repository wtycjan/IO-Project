#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <new>
#include"Header.h"


using namespace std;

int main()
{
	string tekst;
	cout << "funkcje, pliki czy moduly?" << endl;
	cin >> tekst;
	if (tekst == "pliki") polaczenia("graf.txt");
	else if (tekst == "funkcje") polaczenia("function_weight.txt");
	else if (tekst == "moduly") modulf("modul.txt");
	else cout << "bledne dane" << endl;;

	system("PAUSE");
	return 0;
}
