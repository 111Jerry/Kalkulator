"""
import sys

def customized_hello(first_name, last_name, gender_pref):
    print("Hello %s %s %s!" % (gender_pref, first_name, last_name))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        exit(1)
    first_name = sys.argv[1]
    last_name = sys.argv[2]
    gender_pref = sys.argv[3]
    customized_hello(gender_pref, first_name, last_name)
"""
"""
import sys

def print_maturity(age):
    if age >= 18:
        print("You are an adult")
    else:
        print("You are a kiddo!")

if __name__ == "__main__":
    age = int(sys.argv[1])
    print_maturity(age)
    print("The program was called with this parameters %s" % sys.argv[1:])
    print("The first parameter is %s" % sys.argv[1])

"""
"""
with open("names.txt", 'r') as read_file:
    for line in read_file.read().splitlines():
        print(line)
"""
"""
Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:


Po uruchomieniu programu jesteśmy pytani o typ obliczenia

>> Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:
Następnie pobieramy dwie wartości liczbowe.

Korzystając z biblioteki logging, informujemy użytkownika, jakie działanie wykonamy i jakie będą jego argumenty (np. Dodaję 1 i 3).

Następnie wykonujemy obliczenie i drukujemy rezultat z print.

Do pobierania wartości użyj input. Nie ma potrzeby sprawdzania, czy podane argumenty są liczbami, przewidujemy poprawne uzupełnienie.

Przykładowe wywołanie razem z wartościami wybranymi przez użytkownika może wyglądać tak:

>> Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: 1
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
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="log_kalkulator.log")
result = 0
def math_calculate(select_number, number_1, number_2):
    if select_number == 1:
        print("Dodaję {} i {}".format(number_1, number_2))
        result = number_1 + number_2
        print(f"Wynik to {result}")
        #logging.info("Dodaję {} i {}".format(number_1, number_2))
    elif select_number == 2:
        print("Odejmuję {} od {}".format(number_1, number_2))
        result = number_1 - number_2
        print(f"Wynik to: {result}")
        #logging.info("Odejmuję {} od {}".format(number_1, number_2))
    elif select_number == 3:
        print("Mnożę {} razy {}".format(number_1, number_2))
        result = number_1 * number_2
        print(f"Wynik to: {result}")
        #logging.info("Mnożę {} razy {}".format(number_1, number_2))
    elif select_number == 4:
        print("Dzielę {} przez {}".format(number_1, number_2))
        print(f"Wynik to: {result}")
        result = number_1 / number_2
        #logging.info("Dzielę {} przez {}".format(number_1, number_2))

if __name__ == "__main__":
    #logging.debug("The program was called with this parameters %s" % sys.argv[1:])
    #logging.debug("First parameter is %s" % sys.argv[1])
    ##select_number = int(sys.argv[1])
    #number_1 = int(sys.argv[2])
    #number_2 = int(sys.argv[3])
    select_number = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
    number_1 = input("Podaj składnik 1: ")
    number_2 = input("Podaj składnik 2: ")
    math_calculate(select_number, number_1, number_2)