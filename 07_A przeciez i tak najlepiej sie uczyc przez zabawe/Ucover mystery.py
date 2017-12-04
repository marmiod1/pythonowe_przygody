import random
min_range = 1
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
            print("Well done! You did it! That is the mystery number")
            break
        if choice > mystery_number:
            print("Too high. The mystery number is smaller.")

        elif choice < mystery_number:
            print("Too low. The mystery number is bigger")

        counter += 1
        if chances == counter:
            print("Unfortunately, you lost")
            print("Mystery number was {}".format(mystery_number))



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