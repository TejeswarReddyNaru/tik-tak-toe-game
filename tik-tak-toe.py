import random

def print_board(board):
    for row in board:
        print('|', end='')
        for cell in row:
            print(' ' + cell + ' |', end='')
        print('\n')

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    return None

def make_move(board, player, row, col):
    if board[row][col] == ' ':
        board[row][col] = player
        return True
    else:
        return False

def get_opponent_move(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return (i, j)
    return None

board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
players = ['X', 'O']
current_player = random.choice(players)

print('Welcome to tic-tac-toe! You are playing as', current_player)
while True:
    print_board(board)
    if current_player == 'X':
        row = int(input('Enter row: '))
        col = int(input('Enter column: '))
        if not make_move(board, current_player, row, col):
            print('That cell is already occupied. Try again.')
            continue
    else:
        print("Tejeswar is thinking.....")
        row, col = get_opponent_move(board)
        make_move(board, current_player, row, col)
        print("Tejeswar played row {} column {}".format(row, col))
    winner = check_winner(board)
    if winner is not None:
        print_board(board)
        print(winner, 'wins!')
        break
    if all(all(cell != ' ' for cell in row) for row in board):
        print_board(board)
        print('Tie game!')
        break
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'
