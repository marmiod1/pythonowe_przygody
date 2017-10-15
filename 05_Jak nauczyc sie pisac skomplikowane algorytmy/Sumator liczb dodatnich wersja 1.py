'''Zadanie: sumator liczb dodatnich wersja 1
Wymyśl algorytm, a następnie napisz program, który sumuje liczby dodatnie podawane przez
użytkownika.
Niech program prosi o podawanie kolejnych liczb dopóki użytkownik nie wprowadzi liczby
ujemnej.
Niech po każdej podanej liczbie program wypisuje aktualną wartość sumy.
Na koniec niech program wypisuje całkowitą uzyskaną sumę.'''

total = 0

while True:
    a = int(input("Enter a number "))
    if a > 0:
        total += a
        print(total)
    else:
        print("This is the end")
        break

print("Final score is {}".format(total))


