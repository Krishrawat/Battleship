from random import randint
start=input("Do u want instructions:y/n").lower()
if start=="y":	
    print("Hey! I am Krish Rawat.Welcome to this game and your task here is to sink my battleship which is hidden in one of the pool in this ocean")
	print("Enjoy the game. :\)")
board = []
for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print (" ".join(row))
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)
def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print (ship_row)
print (ship_col)

for turn in range(4): 
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    if guess_row == ship_row and guess_col == ship_col:
        print ("Congratulations! You sunk my battleship!")
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
        print ("Oops, that's not even in any pool in the ocean.")
        elif(board[guess_row][guess_col] == "X"):
        print "You guessed that one already."
    else:
        if turn==3:
            print ("Game Over")
        else:
            print ("You missed my battleship!")
            board[guess_row][guess_col] = "X"
    print ("This is yours : ", turn+1,"turn")
    print_board(board)