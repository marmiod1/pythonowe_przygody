#Napisz program, który sprawdzi czy liczba całkowita jest potęgą drugiej podanej liczby całkowitej

import math


def is_a_power(n, m):
    while n > m:
        n = n / m
    if n == m:
        print("true")
        return True
    else:
        print("false")
        return False


is_a_power(243, 3)


import math

def is_a_power(n, m):
    while n > m:
        n = n / m
        
    result = n == m # wyrażenie n == m zwraca booleana i to przypisuję do result
    print(result)
    return result

is_a_power(1024,2) 


def is_a_power(n, m):
    while n > m:
        n = n / m
    return n == m

print(is_a_power(1024,2))
