def print_board(entries):
    line = "+---+---+---+"
    output = line
    n = 0
    for entry in entries:
        if n % 3 == 0:
            output = output + "\n| "
        else:
            output = output + " | "
        output = output + str(entry)
        if n % 3 == 2:
            output = output + " |\n"
            output = output + line
        n = n + 1
    print(output)
    print()


board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
current_player = "X"


def game_over(board, num):
    print_board(board)
    print("Game Over")
    print(board[num], "has won")
    exit()


def is_row_winner(board, row):
    if row == 1:
        index = 0
    if row == 2:
        index = 3
    if row == 3:
        index = 6
    return board[index] == board[index + 1] and board[index + 1] == board[index + 2]

def is_column_winner(board, column):
    index = column - 1
    return board[index] == board[index + 3] and board[index + 3] == board[index + 6]

def is_diagonal_winner(board, diagonal):
    if diagonal == 1:
        index = 0
        return board[index] == board[index + 4] and board[index + 4] == board[index + 8]
    if diagonal == 2:
        index = diagonal
        return board[index] == board[index + 2] and board[index + 2] == board[index + 4]

for move_number in range(1, 10):
    print_board(board)
    response = input("Where would " + current_player + " like to move? ")
    space_number = int(response) - 1
    board[space_number] = current_player

    if is_row_winner(board, 1):
        game_over(board, 0)

    elif is_row_winner(board, 2):
        game_over(board, 3)

    elif is_row_winner(board, 3):
        game_over(board, 6)

    elif is_column_winner(board, 1):
        game_over(board, 0)

    elif is_column_winner(board, 2):
        game_over(board, 1)

    elif is_column_winner(board, 3):
        game_over(board, 2)

    elif is_diagonal_winner(board, 1):
        game_over(board, 0)

    elif is_diagonal_winner(board, 2):
        game_over(board, 2)

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

print("It's a tie!")
