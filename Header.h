#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <new>


using namespace std;

int i = 0;		//zmienne pomocnicze
int j = 0;
int igraf = 0;



void polaczenia(string notatnik) {

	
	int rozmiar_pliku=0;
	string znak = "->";
	string linia;
	string linia2;

	int rozmiar_dynamicznej = 0;
	fstream dane;
	dane.open(notatnik, ios::in);  //txt od Grzesia

	if (dane.good() == false)
	{
		cout << "Nie mozna otworzyc pliku";
		exit(0);
	}
	else
	{
		ifstream file(notatnik);		//sprawdzanie rozmiaru pliku do stworzenia tablic dynamicznych
		while (getline(file, linia2))
			rozmiar_pliku++;

		string* grafs = new string[rozmiar_pliku];	// stringi potrzebne do rysowania grafu w petli
		string* linie = new string[rozmiar_pliku]; //tablica do linii
		string* poloczenia = new string[rozmiar_pliku];//tablica do poloczen
		string* wagi = new string[rozmiar_pliku]();//tablica do wag
		for (int i = 0; i < rozmiar_pliku; i++)
			wagi[i] = "0";			//zerujemy tablice wag



		i = 0;

		while (getline(dane, linia))          //petla zczutyjaca ilosc linie
		{
			cout << linia << endl;
			linie[i] = linia;
			i++;
			if (linia == "dane") break;
		}

		i = 0;
		while (getline(dane, linia))          //petla zczytujaca poloczenia miedzy plikami
		{
			cout << linia << endl;
			poloczenia[i] = linia;
			i++;
			if (linia == "dane") break;
		}

		i = 0;
		while (getline(dane, linia))         //petla zczytujaca wagi
		{
			cout << linia << endl;
			wagi[i] = linia;	
			rozmiar_dynamicznej++;			//licznik wag jest jednoznaczny z iloscia polaczen
			if (linia == "dane")
			{	
				wagi[i] = "0";		//waga od i zeby nie byla rowna "dane"
				break;			
			}
			i++;
		}
			
		string* all = new string[rozmiar_dynamicznej];

		i = 0;
		for (j = 0; j < rozmiar_dynamicznej-1; j++)	//all to sa te dlugie stringi, które wsadzamy do grafu
		{											//tworzymy ich tyle ile jest polaczen


			if (wagi[j] == "0")								//sprawdzamy czy musimy tworzyc polaczenie czy wolny wezel
			{
				all[j] = poloczenia[i] + "_" + linie[i] + ";\n"+poloczenia[i+1] + "_" + linie[i+1];
				grafs[j] = all[j] + ";\n";
				i=i+2;
			}
			else {
				
				all[j] = poloczenia[i] + "_" + linie[i] + znak + poloczenia[i + 1] + "_" + linie[i + 1];
				grafs[j] = all[j] + "[label = " + wagi[j] + "];\n";
				i = i + 2;
			}
		}


		string graph = "digraph G {";
		for (igraf = 0; igraf < rozmiar_dynamicznej; igraf++)	// tworzenie polecenia do stworzenia grafu w petli
		{
			graph += grafs[igraf];
		}
		graph += "}";

		
		string dotPath = "C:\\Users\\Tycjan\\Documents\\release\\bin\\dot.exe"; //link do biblioteki
		string tempFile = "temp.dot";
		string outFile = "out.png";

		ofstream out;
		out.open(tempFile.c_str(), std::ios::out);
		out << graph << std::endl;
		out.close();

		system((dotPath + " " + tempFile + " -Tpng -o " + outFile).c_str());	//tworzenie grafu
		dane.close();

		delete[] linie;
		delete[] poloczenia;
		delete[] wagi;
	}

}

void modulf(string notatnik) {
	const string quote = "\"";
	int rozmiar_pliku = 0;
	string znak = "->";
	string linia;
	string linia2;

	int rozmiar_dynamicznej = 0;
	fstream dane;
	dane.open(notatnik, ios::in);  //txt od Grzesia

	if (dane.good() == false)
	{
		cout << "Nie mozna otworzyc pliku";
		exit(0);
	}
	else
	{
		ifstream file(notatnik);		//sprawdzanie rozmiaru pliku do stworzenia tablic dynamicznych
		while (getline(file, linia2))
			rozmiar_pliku++;

		string* grafs = new string[rozmiar_pliku];	// stringi potrzebne do rysowania grafu w petli
		string* linie = new string[rozmiar_pliku]; //tablica do linii
		string* wagi = new string[rozmiar_pliku]();//tablica do wag
		for (int i = 0; i < rozmiar_pliku; i++)
			wagi[i] = "0";			//zerujemy tablice wag



		i = 0;
		while (getline(dane, linia))         //petla zczytujaca wagi
		{
			cout << linia << endl;
			wagi[i] = linia;
					
			if (linia == "dane")
			{
				wagi[i] = "0";		//waga od i zeby nie byla rowna "dane"
				break;
			}
			i++;
		}
		i = 0;
		while (getline(dane, linia))          //petla zczutyjaca ilosc linie
		{
			cout << linia << endl;
			linie[i] = linia;
			i++;
			rozmiar_dynamicznej++;			//licznik lin jest jednoznaczny z iloscia polaczen
			if (linia == "dane") break;
		}

		



		string* all = new string[rozmiar_dynamicznej];


		all[0] =quote+ linie[0]+quote + znak + linie[1];
		all[1] = quote + " "+linie[3]+quote +  znak + linie[1];		//tworzenie zmiennych do grafu
		all[2] = linie[2]  + znak + quote+linie[0]+quote;

		all[3] =quote+ linie[4] +quote + znak + linie[5] ;	//druga czesc
		all[4] = linie[6]  + znak +quote+ linie[4] +quote;
		all[5] = linie[7] + znak + linie[5];




	string graph =          //Funkcja rysujaca graf
		"digraph G {"+ all[0] + " [ label = " + wagi[0] + "  ];\n"
		"" + all[1] + "[label = " + wagi[0] + "]; \n"
		""+ all[2] + "[label = " + wagi[0] + "]; \n"
		"" + all[3] + "[label = " + wagi[0] + "]; \n"
		"" + all[4] + "[label = " + wagi[0] + "]; \n"
		"" + all[5] + "[label = " + wagi[0] + "]; \n"
		"}";

	string dotPath = "C:\\Users\\Tycjan\\Documents\\release\\bin\\dot.exe";
	string tempFile = "temp.dot";
	string outFile = "out.png";

	ofstream out;
	out.open(tempFile.c_str(), std::ios::out);
	out << graph << std::endl;
	out.close();


	system((dotPath + " " + tempFile + " -Tpng -o " + outFile).c_str());

	dane.close();
	}

}
