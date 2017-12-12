"""Napisz program, który dla podanego łańcucha znaków zamieni podaną pozycję na jakiś znak (też podany przez użytkownika).
Funkcja, która dokona zamiany znaku z podanej pozycji musi sprawdzid, czy w ogóle pozycja wskazana jest prawidłowo
(nie każemy np. Zamienic 6 znaku, podczas gdy łaocuch ma tylko 5 znaków).
Funkcja powinna przyjmowad 3 parametry (łaocuch do analizy, pozycję, którą należy podmienid, i znak który ma służyd do podmiany).
Niech program wyświetla łaocuch przed i po zamianie.
"""


def zmiany(pierwotny, pozycja, znaki):
    indeks = pozycja - 1
    poczatek_slowa = indeks
    dlugosc_slowa = len(znaki)
    pozycja_konca_zmiany = indeks + dlugosc_slowa
    początek = pierwotny[:indeks]
    koniec = pierwotny[pozycja_konca_zmiany:]
    liczba_koncowych_liter = len(koniec)

    if pozycja > len(pierwotny):
        print("To słowo nie ma tyle znaków")
    elif dlugosc_slowa <= len(pierwotny) and pozycja > 0 and dlugosc_slowa <= len(pierwotny[indeks:]):
        noweSłowo = [początek, znaki, koniec]
        noweSłowo = ''.join(noweSłowo)
        print(noweSłowo)
        print(pierwotny)
    else:
        print("zbyt duża ilość znaków do podmiany")

pierwotny = input("wpisz słowo, które będziemy modyfikować: ")
pozycja = int(input("od której litery zaczynamy zmiany?: "))
znaki = input("co wstawiamy: ")

zmiany(pierwotny, pozycja, znaki)

    


