'''Sprawdź czy podana jako parametr liczba jest liczbą pierwszą'''

import math

i = 2

number = 81

while i <= math.sqrt(number):
    if number % i == 0:
        print("{} - No, it's not a prime number".format(number))
    break
    i += 1

print("{} it's a prime number".format(number))

  


            
