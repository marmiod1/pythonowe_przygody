'''Napisz program, który obliczy stan konta za n lat, gdzie stan początkowy konta wynosi SPK, a stopa oprocentowania P % rocznie (obowiązuje miesięczna kapitalizacja odsetek).
 N, SPK i P podaje użytkownik programu.'''

def profit(spk, p, n):
    for i in range(n):
        final = spk + spk * p #wynik mnożenia przez "float" również jest liczbą zmiennoprzecinkową
    return int(final) #wynik działania zostaje zmieniony na "integer" aby 'pozbyć' się przecinka w wyniku

spk = int(input("Enter invested funds: ")) #za pomocą int() zamieniam wpisywaną wartość "string" na "integer"
p = int(input("How high is the interest rate: "))*0.01 #wpisywana wartość zmieniana jest na integer a następnie na procenty
n = int(input("How long do you want to save (in years): "))



print("Final account balance after {} years is ".format(n) + str(profit(spk, p, n))) #wynik fukncji profit() zostaje zmieniony na "string" aby dodawanie 'stringów' podczas drukowania wyniku było możliwe
