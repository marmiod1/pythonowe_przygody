import random

def kolejka():
    counter = 1

    while counter <6:
        rawChoice = input("Wpisz cyfrę: ")
        choice = getInput(rawChoice)
        if choice == szukanaLiczba:
            print("Zgadłeś, brawo!")
            return False
            break
        if choice > szukanaLiczba:
            print("zbyt wysoka, szukaj mniejszej")
            counter += 1

        elif choice < szukanaLiczba:
            print("troszkę większa")
            counter += 1


def getInput(rawChoice):
    try:
        choice = int(rawChoice.strip())
    except ValueError:
        print("Spróbuj wpisać prawidłową wartość")
        return -1
    return choice


while True:
    szukanaLiczba = random.randint(1, 101)
    kolejka()
    kontynuacjaGry = input("Chcesz zagrać ponownie (y/n)?: ")
    if kontynuacjaGry == "n":
        print("dzięki za wspólnie spędzony czas")
        break
    else:
        continue







