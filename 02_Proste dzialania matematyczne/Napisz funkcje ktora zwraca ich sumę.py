'''Napisz funkcję zawierającą dwa parametry, która zwraca ich sumę. Parametry mają być podane przez użytkownika'''


def total(x, y):
    return x + y

x = int(input("Enter first number: ")) # za pomocą int() zamieniam 'stringa' na 'integer'
y = int(input("Enter second number: "))
    

print (total(x, y))
