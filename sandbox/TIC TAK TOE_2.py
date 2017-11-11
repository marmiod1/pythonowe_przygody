# making a board

board = [" " for i in range(9)]

def print_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

    print()
    print()
    print(row1)
    print(row2)
    print(row3)
    print()
    print()


def player_move(icon):
    print("Your turn player {}".format(icon))

    choice=-1
    while(choice==-1):
        rawChoice=input("Enter you move (1-9): ")
        choice = getInput(rawChoice)
    board[choice - 1] = icon

def getInput(rawChoice):
    try:
        choice = int(rawChoice.strip())
    except ValueError:
        print("It is not a number")
        return -1

    if choice < 0 or choice > 9:
        print("Please, enter your move only from 1-9:  ")
        return -1

    if board[choice - 1] != " ":
        print("That space is taken!")
        return -1
    return choice

def is_victory(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
            (board[3] == icon and board[4] == icon and board[5] == icon) or \
            (board[6] == icon and board[7] == icon and board[8] == icon) or \
            (board[0] == icon and board[3] == icon and board[6] == icon) or \
            (board[1] == icon and board[4] == icon and board[7] == icon) or \
            (board[2] == icon and board[5] == icon and board[8] == icon) or \
            (board[0] == icon and board[4] == icon and board[8] == icon) or \
            (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False


def is_draw():
    if " " not in board:
        return True
    else:
        return False


while True:
    print_board()
    player_move("X")
    print_board()
    if is_draw():
        print("It's a draw")
        break
    elif is_victory("X"):
        print("X Wins! Congratulations")
        break
    player_move("O")
    if is_victory("O"):
        print_board()
        print("O Wins! Congratulations")
        break
    elif is_draw():
        print_board()
        print("It's a draw")
        break