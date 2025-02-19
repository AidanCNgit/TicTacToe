

def main():

    p1score = 0
    p2score = 0

    #super weird turn idea, makes it so I dont have to use an if statement to change turns though
    turn = 3
    #board list
    board = ["_", "_", "_", 
             "_", "_", "_", 
             "_", "_", "_"]



    #game continues until win or tie

    while not(cfw(board, "x") == "W" or cfw(board, "o") == "W"):
        
        if turn % 2 == 1:
            display(board)
            currentP = int(input(f"X, Pick a Square 1-9: ")) - 1
            while not(board[currentP] == "_"):
                currentP = int(input(f"X, Please pick an empty square: ")) - 1
            board[currentP] = "x"

        else:
            display(board)
            currentP = int(input(f"O, Pick a Square 1-9: ")) - 1
            while not(board[currentP] == "_"):
                currentP = int(input(f"O, Please pick an empty square: ")) - 1
            board[currentP] = "o"

        if not("_" in board):
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
        main()
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
    


#displays the board

def display(data):

        for i in range(3):
            print("""
            """)
            for o in range(3):
                print(f"{data[o + (i * 3)]:<4}",end="")



    
    
main()

