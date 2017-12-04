# zacząć od tego by gracz wpisywał słowa, które w każdej kolejne będa dodawana do listy

wszystie_uzyte_slowa = []
print("Zaczynamy od słowa na literkę 'a' ")

def player_move(player):
    if player == "1":
        gracz = "1"
    elif player == "2":
        gracz = "2"
    print("Kolej gracza nr {}".format(gracz))


def player_choose(player):
    wybor = get_input()
    if len(wszystie_uzyte_slowa) < 1:
        ostatnia_literka = "a"
    else:
        slowo_do_walidacji = wszystie_uzyte_slowa[-1]
        ostatnia_literka = slowo_do_walidacji[-1]

    if wybor[0] == ostatnia_literka:
        pass
    else:
        print("nie udało ci się zacząć słowa na odpowiednią literę, którą była litera: {}".format(ostatnia_literka))
        #wtedy powinien przerwać grę, a teraz idzie dalej i dodaje do listy "wszystkie użyte słowa, słowo, które było złe
        #i przez to zmienia wartość "ostatnia_literka"

    if wybor in wszystie_uzyte_slowa:
        print("to słowo się już raz pojawiło, Graczu przegrałeś") #chciałabym żeby skończyło grę w tym momencie
    else:
        wszystie_uzyte_slowa.append(wybor)


def get_input():
    while True:
        choice = input("Moje słowo: ")
        if choice.isalpha():
            return choice
        else:
            print("podane słowo nie może być cyfrą")


while True:
    player_move("1")
    player_choose("1")
    player_move("2")
    player_choose("2")

