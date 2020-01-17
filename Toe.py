# global variables

#Game board
board =["-","-","-"
        ,"-","-","-",
        "-","-","-",]

#If game is still going 
game_still_going = True

#who won? Or tie?
winner = None

#whos turn is it
current_player = "X"



#play game of tie tac toe 
def play_game():

  display_board()

  #while the game is still going 
  while game_still_going:

    #handle a single turn of an arbitrary player
    handle_turn(current_player)

    #check if the game has ended
    check_if_game_over()

    # flip to the other player
    flip_player()

# The game has ended
  if winner == "X" or winner == "O":
    print(winner + " won.")
  elif winner == None:
    print("Tie.")

#display board
def display_board():
    print(board[0] + "|"+board[1] + "|"+ board[2])
    print(board[3] + "|"+board[4] + "|"+ board[5])
    print(board[6] + "|"+board[7] + "|"+ board[8])
   



def handle_turn(player):

  print(player + "'s turn.")
  position = input("Choose a position from 1-9: ")

  valid = False
  while not valid:

    while position not in ["1", "2", "3", "4" ,"5", "6", "7", "8", "9"]:
      position = input("invalid input. Choose a position from 1-9: ")

    position = int(position) - 1

    if board[position] == "-":
      valid = True
    else:
      print("You can't go there. Go again.")

  board[position] = player

  display_board()

def check_if_game_over():
  check_for_winner()
  check_if_tie()

def check_for_winner():
  #Set up global variables
  global winner

  row_winner = check_rows()
  column_winner = check_columns()
  diagonal_winner = check_diagonals()
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None


def check_rows():
  # Setup global variables
  global game_still_going
  # Check if any of the rows have all the same value(and not empty)
  row_1 =board[0]  == board[1] == board == [2] != "-"
  row_2 =board[3]  == board[4] == board == [5] != "-"
  row_3 =board[6]  == board[7] == board == [8] != "-"
  #if any row has a match flag that there is a win
  if row_1 or row_2 or row_3:
    game_still_going = False
  #Return the winner (x or o)
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  else:
    return None
  

def check_columns():
  global game_still_going
  # Check if any of the rows have all the same value(and not empty)
  columns_1 =board[0]  == board[3] == board == [6] != "-"
  columns_2 =board[1]  == board[4] == board == [7] != "-"
  columns_3 =board[2]  == board[5] == board == [8] != "-"
  #if any columns has a match flag that there is a win
  if columns_1 or columns_2 or columns_3:
    game_still_going = False
  #Return the winner (x or o)
  if columns_1:
    return board[0]
  elif columns_2:
    return board[1]
  elif columns_3:
    return board[2]
  else:
    return None
  


def check_diagonals():
  global game_still_going
  # Check if any of the rows have all the same value(and not empty)
  diagonals_1 = board[0]  == board[4] == board == [8] != "-"
  diagonals_2 = board[2]  == board[4] == board == [6] != "-"
  
  #if any columns has a match flag that there is a win
  if diagonals_1 or diagonals_2:
    game_still_going = False
  #Return the winner (x or o)
  if diagonals_1:
    return board[0]
  elif diagonals_2:
    return board[2]
  
  else:
   return None


def check_if_tie():
  global game_still_going
  if "-" not in board:
    game_still_going = False
    return 

  else:
    return False

def flip_player():
  global current_player
  if current_player == "X":
    current_player = "O"

  elif current_player == "O":
    current_player = "X"

play_game()



