'''Zadanie: sumator liczb dodatnich z licznikiem
Zmodyfikuj poprzedni algorytm tak, aby zliczał on ile liczb użytkownik wprowadził. Zatem chcemy
mieć algorytm, który sumuje liczby dodatnie podawane przez użytkownika i zapamiętuje ile liczb
zostało wprowadzonych.
Niech program prosi o podawanie kolejnych liczb dopóki użytkownik nie wprowadzi liczby
ujemnej.
Niech po każdej podanej liczbie program wypisuje aktualną wartość sumy i informację ile liczb
zostało zsumowanych.
Na koniec niech program wypisuje uzyskaną sumę i ilość wprowadzonych liczb'''

total = 0
counter = 0

while True:
    a = int(input("Enter a number "))
    if a > 0:
        total += a
        counter += 1
        print(total)
        print("You entered {} numbers".format(counter))
    else:
        print("This is the end")
        break

print("Final score is {}".format(total))
print("The user entered {} numbers".format(counter))
