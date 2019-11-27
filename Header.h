#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <new>


using namespace std;

class Dane
{
public:
	int i = 0;		//zmienne pomocnicze
	int j = 0;
	int igraf = 0;

	int rozmiar_pliku = 0;
	string znak = "->";
	const string quote = "\"";
	string linia;
	string linia2;
	fstream dane;
	int rozmiar_dynamicznej = 0;
	

	string graph = "digraph G {";
	string dotPath = "C:\\Users\\Tycjan\\Documents\\release\\bin\\dot.exe"; //link do biblioteki
	string tempFile = "temp.dot";
	string outFile = "out.png";
};

class Funkcje : public Dane
{
public:
	void draw() {

		graph += "}";
		cout << graph << endl;
		ofstream out;
		out.open(tempFile.c_str(), std::ios::out);
		out << graph << std::endl;
		out.close();

		system((dotPath + " " + tempFile + " -Tpng -o " + outFile).c_str());	//tworzenie grafu
	}
	void polaczenia(string notatnik) {

		
		rozmiar_dynamicznej = 0;	//zerujemy rozmiar dla wielukrotnego wywolania funkcji

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
				linie[i] = linia;
				i++;
				if (linia == "dane") break;
			}

			i = 0;
			while (getline(dane, linia))          //petla zczytujaca poloczenia miedzy plikami
			{
				poloczenia[i] = linia;
				i++;
				if (linia == "dane") break;
			}

			i = 0;
			while (getline(dane, linia))         //petla zczytujaca wagi
			{
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
			for (j = 0; j < rozmiar_dynamicznej - 1; j++)	//all to sa te dlugie stringi, które wsadzamy do grafu
			{											//tworzymy ich tyle ile jest polaczen


				if (wagi[j] == "0")								//sprawdzamy czy musimy tworzyc polaczenie czy wolny wezel
				{
					all[j] = poloczenia[i] + "_" + linie[i] + ";\n" + poloczenia[i + 1] + "_" + linie[i + 1];
					grafs[j] = all[j] + ";\n";
					i = i + 2;
				}
				else {

					all[j] = poloczenia[i] + "_" + linie[i] + znak + poloczenia[i + 1] + "_" + linie[i + 1];
					grafs[j] = all[j] + "[label = " + wagi[j] + "];\n";
					i = i + 2;
				}
			}


			
			for (igraf = 0; igraf < rozmiar_dynamicznej; igraf++)	// tworzenie polecenia do stworzenia grafu w petli
			{
				graph += grafs[igraf];
			}

			cout << graph;
			delete[] linie;
			delete[] poloczenia;
			delete[] wagi;
		}

		dane.close();
	}
	void modulf(string notatnik) {
		
		rozmiar_pliku = 0;
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
				linie[i] = linia;
				i++;
				rozmiar_dynamicznej++;			//licznik lin jest jednoznaczny z iloscia polaczen
				if (linia == "dane") break;
			}





			string* all = new string[rozmiar_dynamicznej];


			all[0] = quote + linie[0] + quote + znak + linie[1];
			all[1] = quote + " " + linie[3] + quote + znak + linie[1];		//tworzenie zmiennych do grafu
			all[2] = linie[2] + znak + quote + linie[0] + quote;

			all[3] = quote + linie[4] + quote + znak + linie[5];	//druga czesc
			all[4] = linie[6] + znak + quote + linie[4] + quote;
			all[5] = linie[7] + znak + linie[5];




			graph += all[0] + " [ label = " + wagi[0] + "  ];\n"  //Funkcja rysujaca gra
				"" + all[1] + "[label = " + wagi[0] + "]; \n"
				"" + all[2] + "[label = " + wagi[0] + "]; \n"
				"" + all[3] + "[label = " + wagi[0] + "]; \n"
				"" + all[4] + "[label = " + wagi[0] + "]; \n"
				"" + all[5] + "[label = " + wagi[0] + "]; \n";
				
			dane.close();
		}
	}

	void Functions(string notatnik)
	{
		polaczenia(notatnik);
		draw();
	}
	void Files(string notatnik)
	{
		polaczenia(notatnik);
		draw();
	}
	void Modules(string notatnik)
	{
		modulf(notatnik);
		draw();
	}
	void PlikiFunkcje(string notatnik1, string notatnik2)
	{
		polaczenia(notatnik1);
		polaczenia(notatnik2);
		draw();

	}
	void PlikiModuly(string notatnik1, string notatnik2)
	{
		polaczenia(notatnik1);
		modulf(notatnik2);
		draw();
	}
	void FunkcjeModuly(string notatnik1, string notatnik2)
	{
		polaczenia(notatnik1);
		modulf(notatnik2);
		draw();
	}
	void FunkcjeModulyPliki(string notatnik1, string notatnik2,string notatnik3)
	{
		polaczenia(notatnik1);
		modulf(notatnik2);
		polaczenia(notatnik3);
		draw();
	}
};
