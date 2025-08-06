import math

# Game board
board = [" " for _ in range(9)]

# Print the board
def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")

# Check for winner
def check_winner(brd, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8], # rows
        [0,3,6], [1,4,7], [2,5,8], # columns
        [0,4,8], [2,4,6]           # diagonals
    ]
    for condition in win_conditions:
        if all(brd[i] == player for i in condition):
            return True
    return False

# Check for draw
def is_draw(brd):
    return " " not in brd

# Player move
def player_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move >= 0 and move < 9 and board[move] == " ":
                board[move] = "X"
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Please enter a number between 1 and 9.")

# AI move using Minimax
def ai_move():
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"

# Minimax Algorithm
def minimax(brd, depth, is_maximizing):
    if check_winner(brd, "O"):
        return 1
    elif check_winner(brd, "X"):
        return -1
    elif is_draw(brd):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if brd[i] == " ":
                brd[i] = "O"
                score = minimax(brd, depth + 1, False)
                brd[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if brd[i] == " ":
                brd[i] = "X"
                score = minimax(brd, depth + 1, True)
                brd[i] = " "
                best_score = min(score, best_score)
        return best_score

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe! You are X. AI is O.")
    print_board()
    
    while True:
        player_move()
        print_board()
        if check_winner(board, "X"):
            print("You win!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

        print("AI's turn...")
        ai_move()
        print_board()
        if check_winner(board, "O"):
            print("AI wins!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
