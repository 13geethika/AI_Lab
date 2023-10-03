import time
import random
board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]
def choice(player,cho):
    if board[cho] == " ":
        board[cho] = player
    else:
        print ("Sorry, that space is not empty!")
        time.sleep(1)
    if is_winner(board, player):
        print_board()
        print(player+" wins! Congratulations")
        return True
    if is_board_full(board):
        print("Tie!")
        return True
    
def print_board():
    print("   |   |   ")
    print(" " + board[1] + " | " + board[2] + " | " + board[3] + "  ")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(" " + board[4] + " | " + board[5] + " | " + board[6] + "  ")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(" " + board[7] + " | " + board[8] + " | " + board[9] + "  ")
    print("   |   |   ")
def is_winner(board, player):
    if ((board[1] == player and board[2] == player and board[3] == player) or 
            (board[4] == player and board[5] == player and board[6] == player) or 
            (board[7] == player and board[8] == player and board[9] == player) or 
            (board[1] == player and board[4] == player and board[7] == player) or 
            (board[2] == player and board[5] == player and board[8] == player) or 
            (board[3] == player and board[6] == player and board[9] == player) or 
            (board[1] == player and board[5] == player and board[9] == player) or 
            (board[3] == player and board[5] == player and board[7] == player)):
        return True
    else:
        return False 
def is_board_full(board):
    if " " in board:
        return False
    else:
        return True
def get_computer_move(board, player):
    if board[5] == " ":
        return 5
    while True:
        move = random.randint(1, 9)
        if board[move] == " ":
            return move
            break
    return 5
while True:
    print_board()
    cho = int(input("Please choose an empty space for X. "))
    choice("X",cho)
    if (choice("X",cho)):
        break
    cho= get_computer_move(board, "O")
    choice("O",cho)
    if (choice("O",cho)):
        break