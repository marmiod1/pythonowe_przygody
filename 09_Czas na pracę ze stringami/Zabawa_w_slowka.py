# Napisz program, w którym dwie osoby będą naprzemiennie podawać słowa.
# Pierwsza litera podanego wyrazu musi zaczynać się na ostatnią literę słowa poprzedniego gracza.
# Słówka nie mogą się powtarzać. Pierwsze słowo musi zaczynać się na literę 'a'

print("Let's start from the letter 'a' ")
set_of_all_words = []


def main():
    while True:
        player_move("1")
        player_choose("1")
        if validation_player_choose("1"):
            pass
        else:
            break
        player_move("2")
        player_choose("2")
        if validation_player_choose("2"):
            pass
        else:
            break


def player_move(player):
    if player == "1":
        player = "1"
    elif player == "2":
        player = "2"
    print("Now it's your turn Player {}".format(player))


def player_choose(player):
    if len(set_of_all_words) < 1:
        first_letter_current_word = "a"
        return first_letter_current_word
    else:
        current_word = set_of_all_words[-1]
        first_letter_current_word = current_word[-1]
        return first_letter_current_word


def validation_player_choose(player):
    chosen_word = get_input()
    if chosen_word[0] == player_choose(player):
        if chosen_word not in set_of_all_words:
            set_of_all_words.append(chosen_word)
            return True
        else:
            print("This word has already appeared. Unfortunately you lost this time.")
            return False
    else:
        print("You didn't start from correct letter which was '{}'".format(player_choose(player)))
        print("You lost this time.")


def get_input():
    while True:
        choice = str.lower(input("My chosen word is: "))
        if choice.isalpha():
            return choice
        else:
            print("You need to enter correct word.")


main()


