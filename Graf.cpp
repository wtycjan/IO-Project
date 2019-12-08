#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <new>
#include"Header.h"
#include <shlobj.h> 
#include <shlwapi.h> 
#include <shellapi.h> 

using namespace std;

int main()
{
	Funkcje* p = new Funkcje;
	int tekst;
	cout << "Wybierz jedna z opcji:" << endl << "1.Pliki" << endl << "2.Funkcje" << endl << "3.Moduly" << endl << "4.Pochodzenie funkcji" << endl
		<< "5.Pliki i funkcje" << endl << "6.Funkcje i moduly" << endl << "7.Pliki i moduly" << endl
		<< "8.Moduly,pliki i funkcje" << endl << "9.Wszystko" << endl;
	cin >> tekst;
	if (tekst == 1) p->Files();
	else if (tekst == 2) p->Functions();
	else if (tekst == 3) p->Modules();
	else if (tekst == 4) p->Origin();
	else if (tekst == 5) p->PlikiFunkcje();
	else if (tekst == 6) p->FunkcjeModuly();
	else if (tekst == 7) p->PlikiModuly();
	else if (tekst == 8) p->FunkcjeModulyPliki();
	else if (tekst == 9) p->All();
	else if (tekst == 0) p->gregory();
	else cout << "bledne dane" << endl;

	cout << endl << "Graf zostal utworzony w pliku out.png" << endl;

	ShellExecute(0, 0, "C:\\Users\\Tycjan\\source\\repos\\IOprojekt\\IOprojekt\\out.png", 0, 0, SW_SHOW);

	system("PAUSE");

	return 0;
}
