import random

p1score = 0
p2score = 0 # this will be used for ai, else player

def main():
    ai_mode = input("Would you like to play against the computer? y/n: ").lower()

    global p1score
    global p2score

    # super weird turn idea, makes it so I dont have to use an if statement to change turns though
    turn = 3
    # board list
    board = ["_", "_", "_", 
             "_", "_", "_", 
             "_", "_", "_"]
    
    if ai_mode == "y":
        # same logic as the normal game, but against the ai
        ai_game(turn, board)
    elif ai_mode == "n":
        # game continues until win or tie
        normal_game(turn, board)
    else:
        print("Please enter a valid input.")
        main()

def normal_game(turn, board):
    global p1score
    global p2score

    while not(cfw(board, "x") == "W" or cfw(board, "o") == "W"):
        if turn % 2 == 1:
            display(board)
            currentP = int(input("X, Please pick 1-9: ")) - 1
            try:
                while not(board[currentP] == "_"):
                    currentP = int(input("X, Please pick an empty square: ")) - 1
            except:
                while currentP > 8 or currentP < 0:
                    currentP = int(input("X, Please pick 1-9: ")) - 1
            while currentP < 0:
                currentP = int(input("X, Please pick 1-9: ")) - 1
            board[currentP] = "x"
        else:
            display(board)
            currentP = int(input("O, Pick a Square 1-9: ")) - 1
            try:
                while not(board[currentP] == "_"):
                    currentP = int(input("O, Please pick an empty square: ")) - 1
            except:
                while currentP > 8 or currentP < 0:
                    currentP = int(input("O, Please pick 1-9: ")) - 1
            while currentP < 0:
                currentP = int(input("X, Please pick 1-9: ")) - 1
            board[currentP] = "o"
        if "_" not in board:
            print("Tie! Go again!")
            board = ["_", "_", "_", 
             "_", "_", "_", 
             "_", "_", "_"]
        turn += 1
    if cfw(board, "x") == "W":
        display(board)
        print("X wins!")
        p1score += 1
    if cfw(board, "o") == "W":
        display(board)
        print("O wins!")
        p2score += 1
    if input("Play again? y/n") == "y":
        board = ["_", "_", "_", 
             "_", "_", "_", 
             "_", "_", "_"]
        
        turn = 3

        normal_game(turn, board)
    else:
        print(f"Thanks for playing! X won {p1score} time(s), while O won {p2score} time(s)!")

def ai_game(turn, board):
    global p1score
    global p2score

    while not(cfw(board, "x") == "W" or cfw(board, "o") == "W"):
        if turn % 2 == 1:
            display(board)
            currentP = int(input("X, Please pick 1-9: ")) - 1
            try:
                while not(board[currentP] == "_"):
                    currentP = int(input("X, Please pick an empty square: ")) - 1
            except:
                while currentP > 8 or currentP < 0:
                    currentP = int(input("X, Please pick 1-9: ")) - 1
            while currentP < 0:
                currentP = int(input("X, Please pick 1-9: ")) - 1
            board[currentP] = "x"
        else:
            display(board)
            currentP = ai_move(board) # move for the ai
            board[currentP] = "o"
        if "_" not in board:
            print("Tie! Go again!")
            board = ["_", "_", "_", 
             "_", "_", "_", 
             "_", "_", "_"]
        turn += 1
    if cfw(board, "x") == "W":
        display(board)
        print("X wins!")
        p1score += 1
    if cfw(board, "o") == "W":
        display(board)
        print("O wins!")
        p2score += 1
    if input("Play again? y/n ") == "y":
        board = ["_", "_", "_", 
             "_", "_", "_", 
             "_", "_", "_"]
        
        turn = 3

        ai_game(turn, board)
    else:
        print(f"Thanks for playing! X won {p1score} time(s), while O won {p2score} time(s)!")

#Function checks for win for one player. 

def cfw(data, player):
    wc = 0
    #row checking
    for i in range(3):
        wc = 0
        for o in range(3):
            if data[o + (i * 3)] == player:
                wc += 1
                if wc == 3:
                    return "W"
    #column + diagnol check
    for i in range(3):
        if data[i] == player and data[i + 3] == player and data[i + 6] == player:

            return "W"

        if i == 0:
            if data[i] == player and data[i + 4] == player and data[i + 8] == player:

                return "W"
        if i == 2:
            if data[i] == player and data[i + 2] == player and data[i + 4] == player:

                return "W"

    return "C"

# "ai" functionality, picks a random empty square

def ai_move(data):
    empty_squares = []

    for i in range(9):
        if data[i] == "_":
            empty_squares.append(i)
    
    if empty_squares:
        return random.choice(empty_squares)
    return None

#displays the board

def display(data):
    for i in range(3):
        print("\n")
        for o in range(3):
            print(f"{data[o + (i * 3)]:<4}",end="")
    print("\n")            
    
main()