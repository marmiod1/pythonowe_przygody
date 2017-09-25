import math

def primeNumber(number):
    divisors = []
    for i in range(1, int(number/2)):
        if number % i == 0:
            divisors.append(i)
            

    for z in divisors:
        if len(divisors) == 2:
            print("{} - Yes, it's a prime number".format(number))
            break
        else:
            print(divisors)
            print("Number {} has {} divisors ".format(number, len(divisors)))
            break
            
primeNumber(225)

    
