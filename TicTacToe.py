
def main():
    c = 0

    board = ["_", "_", "_", 
             "_", "_", "_", 
             "_", "_", "_"]

    board[int(input(f"Pick a Square 1-9: {display(board)}")) - 1] = "x"

    while not(cfw(board, "x") == "W"):

        board[int(input(f"Pick a Square 1-9: {display(board)}")) - 1] = "x"

        display(board)

def cfw(data, player):

    wc = 0

    for i in range(3):
        wc = 0
        for o in range(3):
            if data[o + (i * 3)] == player:
                wc += 1
                if wc == 3:
                    return "W"

    for i in range(3):

        try: 
            data[i + 8]
        except 



        if data[i] == player and data[i + 3] == player and data[i + 6] == player:

            return "W"

        if data[i] == player and data[i + 4] == player and data[i + 8] == player:

            return "W"
        
        if data[i] == player and data[i + 2] == player and data[i + 4] == player:

            return "W"



    return "C"
    




def display(data):

        for i in range(3):
            print("""
            """)
            for o in range(3):
                print(f"{data[o + (i * 3)]:<4}",end="")



    
    
    

        
                

main()