"""
Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:


Po uruchomieniu programu jesteśmy pytani o typ obliczenia

>> Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:
Następnie pobieramy dwie wartości liczbowe.

Korzystając z biblioteki logging, informujemy użytkownika, jakie działanie wykonamy i jakie będą jego argumenty (np. Dodaję 1 i 3).

Następnie wykonujemy obliczenie i drukujemy rezultat z print.

Do pobierania wartości użyj input. Nie ma potrzeby sprawdzania, czy podane argumenty są liczbami, przewidujemy poprawne uzupełnienie.

Przykładowe wywołanie razem z wartościami wybranymi przez użytkownika może wyglądać tak:

>> Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: 
Podaj składnik 1. 2.3
Podaj składnik 2. 5.4
Dodaję 2.30 i 5.40
Wynik to 7.70
Dla chętnych
Jeśli chcesz usprawnić swoje zadanie, możesz dodać dwa rozszerzenia:

Sprawdzaj, czy podana wartość na pewno jest liczbą.
W wypadku mnożenia i dodawania daj użytkownikowi możliwość wpisania większej ilości argumentów niż tylko dwa, np. możesz dodać do siebie trzy i więcej liczb.
Prześlij link do zdalnego repozytorium z zadaniem Mentorowi. Sprawisz mu frajdę!
"""

import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="log_kalkulator.log")

def math_calculate(select_number, number_1, number_2):
    if select_number == 1:
        logging.info(f"Dodaję {number_1} i {number_2}")
        #print(f"Dodaję {number_1} i {number_2}")
        print(f"Wynik to: {number_1 + number_2}")
    elif select_number == 2:
        logging.info(f"Odejmuję od {number_1}  {number_2}")
        #print(f"Odejmuję od {number_1}  {number_2}")
        print(f"Wynik to: {number_1 - number_2}")
    elif select_number == 3:
        logging.info(f"Mnożę {number_1} razy {number_2}")
        #print(f"Mnożę {number_1} razy {number_2}")
        print(f"Wynik to: {number_1 * number_2}")
    elif select_number == 4:
        logging.info(f"Dzielę {number_1} przez {number_2}")
        #print(f"Dzielę {number_1} przez {number_2}")
        print(f"Wynik to: {number_1 / number_2}")
    
if __name__ == "__main__":
    select_number = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
    number_1 = int(input("Podaj składnik 1: "))
    number_2 = int(input("Podaj składnik 2: "))
    math_calculate(select_number, number_1, number_2)