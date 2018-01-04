#Napisz program, który będzie sprawdał czy podana liczba jest liczbą kwadratową

import math


def perfect_square(n):
    for number in range(1, n):
        if n/number == number:
            return True, number
        else:
            pass


print(perfect_square(n=25))


def perfect_square(n):
    for number in range(n):
        if n == number**2:
            return True, number
        else:
            pass


print(perfect_square(n=16))

