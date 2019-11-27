#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <new>
#include"Header.h"


using namespace std;

int main()
{
	Funkcje* p = new Funkcje;
	int tekst;
	cout << "Wybierz jedna z opcji:" << endl << "1.Pliki" << endl << "2.Funkcje" <<endl<< "3.Moduly" << endl << "4.Pliki i funkcje" << endl 
		<< "5.Funkcje i moduly" << endl << "6.Pliki i moduly" << endl << "7.Moduly,pliki i funkcje"<<endl;
	cin >> tekst;
	if (tekst == 1) p->Files("graf.txt");
	else if (tekst == 2) p->Functions("function_weight.txt");
	else if (tekst == 3) p->Modules("modul.txt");
	else if (tekst == 4) p->PlikiFunkcje("graf.txt","function_weight.txt");
	else if (tekst == 5) p->FunkcjeModuly("function_weight.txt","modul.txt");
	else if (tekst == 6) p->PlikiModuly("graf.txt","modul.txt");
	else if (tekst == 7) p->FunkcjeModulyPliki("function_weight.txt", "modul.txt", "graf.txt");
	else cout << "bledne dane" << endl;

	cout <<endl<< "Graf zostal utworzony w pliku out.png"<<endl;

	system("PAUSE");
	return 0;
}
