'''Zadanie: średnia liczb dodatnich
Zmodyfikuj poprzedni algorytm tak, że pobiera on od użytkownika ciąg liczb, i wypisuje długość i
średnią tego ciągu. Przyjmij, że użytkownik wpisał wszystkie liczby wtedy, kiedy na pytanie o
następną liczbę, poda liczbę ujemną.'''

total = 0
counter = 0

while True:
    a = int(input("Enter a number "))
    if a > 0:
        total += a
        counter += 1
        print(total)
        print("You entered {} numbers".format(counter))
        average = total / counter
    else:
        print("This is the end")
        break

print("Final score is {}".format(total))
print("The user entered {} numbers".format(counter))
print("The average score is {}".format(average))
