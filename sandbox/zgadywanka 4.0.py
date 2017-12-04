import random
min_range = 0
max_range = 100
chances = 5


def main():
    while True:
        tie()
        continuing = input("Do you want to play again (y/n)?: ")
        if continuing == "n":
            print("Thanks for playing, see you soon!")
            break
        else:
            continue


def tie():
    counter = 0
    mystery_number = random.randint(min_range, max_range)
    while counter < chances:
        choice = get_input()
        if choice == mystery_number:
            print("Well done! You did it! That is the hunted number")
            break
        if choice > mystery_number:
            print("Too high. The hunted number is smaller.")

        elif choice < mystery_number:
            print("Too low. The hunted number is a little bit bigger")

        counter += 1
        if chances == counter:
            print("you lose")
            print("mistery number was {}".format(mystery_number))



def get_input():
    choice = min_range - 1
    while min_range > choice or choice > max_range:
        raw_choice = input("Guess a number from {} to {}: ".format(min_range, max_range))
        try:
            choice = int(raw_choice.strip())
        except ValueError:
            print("Enter correct value, please")
    return choice

main()