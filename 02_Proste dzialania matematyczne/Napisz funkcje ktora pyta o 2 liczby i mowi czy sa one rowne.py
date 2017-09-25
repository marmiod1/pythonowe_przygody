'''Napisz funkcję, która pyta o dwie liczby i mówi czy są one równe, a jeśli nie to mówi jaka jest różnica między nimi.'''


def comparison(x,y):
    if x == y:
        print("Numbers are equal")
    elif x > y:
        difference = x - y
        print("{} is bigger than {}, difference is {}".format(x, y, difference))
    else:
        difference = y - x
        print("{} is bigger than {}, difference is {}".format(y, x, difference))

comparison(1,9)
comparison(15, 10)
