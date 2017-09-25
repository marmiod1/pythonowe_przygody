"""
Wypisz największą liczbę niepodzielną przez 2,3,5,7 ale mniejszą od 1000
"""

def indivisible():
    numbers = []
    for x in range (0,1000):
        if x % 2 != 0 and x%3 != 0 and x % 5 != 0 and x % 7 != 0:
            numbers.append(x)

    print(max(numbers))

indivisible()



"""
W niepodzielności przez 2 3 5 i 7 proponuję zacząć pentlę od 1000 a nie od zera i 
sprawdzać czy jest liczba podzielna przez wymienione cyfry. Jeśli ją znajdziesz to już na pewno będzie największa – 
nie będzie trzeba robić maxa z tablicy, nie będzie trzeba przechowywać tablicy, ani robić 1000 iteracji
"""

def indivisible():
    a = range(1000)
    for x in a[::-1]:
        if x % 2 != 0 and x % 3 != 0 and x % 5 != 0 and x % 7 != 0:
            print(x)
            break


indivisible()
