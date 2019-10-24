#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <string>
using namespace std;

int i = 1;
string lin1, lin2, lin3,lin4,lin5,lin6,lin7,lin8;  //zmienne odpowiadajace za dane ilosc linii w kodzie,zalezy do ilu plikow sie odnosimy
string pol11, pol12, pol21, pol22, pol31, pol32,pol41,pol42; //zmienne odpowiadajace za polaczenia
string wag1, wag2, wag3;  //zmienne odpowiadajace za wagi poloczen
string all1, all2, all3;
string znak = "->";
string linia;
fstream dane;

void pliki() {

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
	all1 = lin1 + znak + lin3;
	all2 = lin2 + znak + lin1;
	all3 = lin2 + znak + lin3;

}
void graf_pliki() {
	string graph =          //Funkcja rysujaca graf
		"digraph G {" + lin1 + " [ xlabel = " + pol11 + "  ];\n"
		"" + lin3 + "[xlabel = " + pol12 + "]; \n"
		"" + lin2 + "[xlabel = " + pol21 + "]; \n"
		//"" + all1 + "[label = " + wag1 + "]; \n"
		//"" + all2 + " [label = " + wag2 + " ];\n"
	//	"" + all3 + "[label =" + wag3 + " ];\n"
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
}
void funkcje() {

	i = 0;
	dane.open("function_weight.txt", ios::in);  //txt od Grzesia

	if (dane.good() == false)
	{
		cout << "Nie mozna otworzyc pliku";
		exit(0);
	}
	else
	{
		while (i < 25) //petla odczytujaca przypisujaca ilosci linni do intow a polaczenia do stringow
		{
			getline(dane, linia);
			cout << linia << endl;
			switch (i)
			{
			case 2: lin1 = linia; break;
			case 4: lin2 = linia; break;
			case 6: lin3 = linia; break;
			case 8: lin4 = linia; break;
			case 10: lin5 = linia; break;
			case 12: lin6 = linia; break;
			case 14: lin7 = linia; break;
			case 16: lin8 = linia; break;
				//tutaj koncza sie ilosci linii a zaczynaja polaczenia
			case 17: pol11 = linia; ; break;
			case 18: pol12 = linia; ; break;
			case 19: pol21 = linia; ; break;
			case 20: pol22 = linia; ; break;
			case 21: pol31 = linia; ; break;
			case 22: pol32 = linia; ; break;
			case 23: pol41 = linia; ; break;
			case 24: pol42 = linia; ; break;
			
			}
			i++;
		}
	}


}
void graf_funkcje() {
	string graph =          //Funkcja rysujaca graf
		"digraph G {" + lin1 + " [ xlabel = " + pol11 + "  ];\n"
		"" + lin2 + "[xlabel = " + pol12 + "]; \n"
		"" + lin3 + "[xlabel = " + pol21 + "]; \n"
		"" + lin4 + "[xlabel = " + pol22 + "]; \n"
		"" + lin5 + "[xlabel = " + pol31 + "]; \n"
		"" + lin6 + "[xlabel = " + pol32 + "]; \n"
		"" + lin7 + "[xlabel = " + pol41 + "]; \n"
		"" + lin8 + "[xlabel = " + pol42 + "]; \n"
		"}";

	string dotPath = "C:\\Users\\Tycjan\\Downloads\\release\\bin\\dot.exe";
	string tempFile = "temp2.dot";
	string outFile = "out2.png";

	ofstream out;
	out.open(tempFile.c_str(), std::ios::out);
	out << graph << std::endl;
	out.close();

	cout << lin5 << pol41;


	system((dotPath + " " + tempFile + " -Tpng -o " + outFile).c_str());

	dane.close();
}

int main() {

	pliki();
	graf_pliki();
	funkcje();
	graf_funkcje();


	return 0;
}
