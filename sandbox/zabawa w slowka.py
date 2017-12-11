print("We will start from the letter 'a' ")
list_of_words = []


def main():
    while True:
        player_move("1")
        player_choose("1")
        if uniqueness("1"):
            pass
        else:
            break
        player_move("2")
        player_choose("2")
        if uniqueness("2"):
            pass
        else:
            break

def player_move(player):
    if player == "1":
        player = "1"
    elif player == "2":
        player = "2"
    print("Now it's your turn player {}".format(player))


def player_choose(player):
    if len(list_of_words) < 1:
        last_letter = "a"
        return last_letter
    else:
        active_word = list_of_words[-1]
        last_letter = active_word[-1]
        return last_letter


def uniqueness(player):
    chosen_word = get_input()
    if chosen_word[0] == player_choose(player):
        if chosen_word not in list_of_words:
            list_of_words.append(chosen_word)
            return True
        else:
            print("This word has already appeared. Unfortunately you lost this time.")
            return False
    else:
        print("You didn't start from correct letter which was '{}'".format(player_choose(player)))
        print("You lost this time.")


def get_input():
    while True:
        choice = input("My chosen word is: ")
        if choice.isalpha():
            choice = str.lower(choice)
            return choice
        else:
            print("You need to enter correct word.")


main()




