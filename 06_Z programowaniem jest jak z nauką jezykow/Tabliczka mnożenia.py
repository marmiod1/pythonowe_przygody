'''Wygeneruj na ekranie tabliczkę mnożenia 10 x 10. Nie musi wyglądać ładnie pod względem graficznym, ale niech w każdym wierszu będzie dokładnie wyników mnożenia).'''

scope = range(1,11)
cols = [0] + list(scope)
for x in cols:
    print(str(cols[x]) + ' ', end='')
print()
for x in scope:
    print(str(x) + ' ', end='')
    for i in scope:
        print(str(x * scope[i-1]) + ' ', end='')
    print()
