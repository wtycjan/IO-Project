#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <string>
using namespace std;

int main() {

	int i = 1;
	string lin1, lin2, lin3;//zmienne odpowiadajace za dane ilosc linii w kodzie,zalezy do ilu plikow sie odnosimy
	string pol11, pol12, pol21, pol22, pol31, pol32; //zmienne odpowiadajace za polaczenia
	string wag1, wag2, wag3; //zmienne odpowiadajace za wagi poloczen
	string all1, all2, all3;
	string znak = "->";
	string linia;

	fstream dane;
	dane.open("graf.txt", ios::in);  //txt od Grzesia

	if (dane.good() == false)
	{
		cout << "Nie mozna otworzyc pliku";
		exit(0);
	}
	else
	{
		while (i < 16) //petla odczytujaca przypisujaca ilosci linni do intow a polaczenia do stringow
		{
			getline(dane, linia);
			cout << linia << endl;
			switch (i)
			{
			case 2: lin1 = linia; break;
			case 4: lin2 = linia; break;
			case 6: lin3 = linia; break;
				//tutaj koncza sie ilosci linii a zaczynaja polaczenia
			case 7: pol11 = linia; ; break;
			case 8: pol12 = linia; ; break;
			case 9: pol21 = linia; ; break;
			case 10: pol22 = linia; ; break;
			case 11: pol31 = linia; ; break;
			case 12: pol32 = linia; ; break;
				//tutaj koncza sie polaczenia a zaczyna ich waga
			case 13: wag1 = linia; break;
			case 14: wag2 = linia; break;
			case 15: wag3 = linia; break;
			}
			i++;
		}
	}


	//dodawanie do siebie stringowstringow
	all1 = pol11 + lin1 + znak + pol12 + lin3;
	all2 = pol21 + lin2 + znak + pol22 + lin1;
	all3 = pol31 + lin2 + znak + pol32 + lin3;


	string graph =          //Funkcja rysujaca graf
		"digraph G {" + all1 + " [ label = " + wag1 + " ];\n"
			""+all2+" [label = "+wag3+" ];\n"
			""+all3+"[label ="+wag2+" ];\n"
		"}";

	string dotPath = "C:\\Users\\Tycjan\\Downloads\\release\\bin\\dot.exe";
	string tempFile = "temp.dot";
	string outFile = "out.png";

	ofstream out;
	out.open(tempFile.c_str(), std::ios::out);
	out << graph << std::endl;
	out.close();

	system((dotPath + " " + tempFile + " -Tpng -o " + outFile).c_str());

	dane.close();
	return 0;
}

