'''Zadanie: średnia liczb
Zmodyfikuj poprzedni algorytm tak, że pobiera on od użytkownika ciąg liczb, i wypisuje długość i
średnią tego ciągu. Przyjmij, że użytkownik wpisał wszystkie liczby wtedy, kiedy na pytanie o
następną liczbę po prostu naciśnie Enter, czyli wpisze pustą linijkę.
Wskazówka: Fragment algorytmu potrzebny do obsługi wczytywania:
1. wczytaj to co wprowadza użytkownik funkcją raw_input,
2. następnie sprawdź czy to nie jest pusty napis.
Jeśli napis jest pusty to koniec,
a jeśli nie pusty to dokonaj konwersji na liczbę i kontynuuj program'''

total = 0
counter = 0
ciąg_liczb = []
average = 0

while True:
    a = input("Enter a number: ")
    try:
       a = int(a)
    except ValueError:
        print("You did not enter a number, game is over")
        break


    ciąg_liczb.append(a)
    total += a
    counter += 1
    print("Current total is {}".format(total))
    print("You entered {} numbers".format(counter))
    average = total / len(ciąg_liczb)


print("Final score is {}".format(total))
print("The user entered {} numbers".format(counter))
print("The average score is {}".format(average))


