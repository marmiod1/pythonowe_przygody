'''Wypisz liczby podzielne przez 3 albo 5 ( w zakresie 1..100) (nie wypisuj tych podzielnych jednocześnie przez 3 i 5)'''

def solution():
    numbers = []
    for x in range (1,101):
        if x % 3 == 0 or x % 5 == 0:
            if x % 3 != 0 or x % 5 !=0:
                numbers.append(x)

    print(numbers)

solution()


# można wykorzystać listę i wydrukować jako [] albo po prostu wydrukować wszystkie rozwiązania przez print(x)

"""
def solution():
    for x in range (1,101):
        if x % 3 == 0 or x % 5 == 0:
            if x % 15 != 0:
        print(x)
        
        
solution()
"""
