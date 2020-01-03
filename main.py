# ------- Global Variabels -------

# game board
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

# if game is still going
game_still_going = True

# who won? or cats game?
winner = None

# Whos turn is it
current_player = "X"

# displays the board
def display_board():
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])

# play a game of tic tac toe
def play_game():

  # display initial board
  display_board()
  
  # while the game is still going
  while game_still_going:

    # handle a single turn of a arbitrary player
    handle_turn(current_player)

    # check if game has ended
    check_if_game_over()

    # flip to other player
    flip_player()

  # the game has ended
  if winner == "X" or winner == "O":
    print(winner + " won.")
  elif winner == None:
    print("cats game.")

# handle a single turn of a arbitrary player
def handle_turn(player):

  print(player + "'s turn")
  position = input("Chose a position from 1-9: ")
 
  if position not in ["1", "2", "3", "4", "5", "6", "7","8", "9"]:
    position = input("Invalad input. Chose a position from 1-9: ")

  position = int(position) - 1

  board[position] = player
  
  display_board()


def check_if_game_over():
  check_for_winner()
  check_if_cats_game()


def check_for_winner():

  global winner
  
  #check rows
  row_winner = check_rows()
  #check columns
  column_winner = check_columns()
  #check diagonals
  diagonal_winner = check_diagonals()
  
  
  #get the winner
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None
  return



def check_rows():
  # set up global varibaels
  global game_still_going
  # check if any of the rows have all the same vaule 
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  # if any row has a match, flag that there is a win
  if row_1 or row_2 or row_3:
    game_still_going = False
  if row_1:
  # return the winner (X or O)
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  return


def check_columns():
  # set up global varibaels
  global game_still_going
  # check if any of the rows have all the same vaule 
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-" 
  # if any row has a match, flag that there is a win
  if column_1 or column_2 or column_3:
    game_still_going = False
  if column_1:
  # return the winner (X or O)
    return board[0]
  elif column_2:
    return board[3]
  elif column_3:
    return board[6]
  return

def check_diagonals():
  # set up global varibaels
  global game_still_going

  # check if any of the rows have all the same vaule 
  diagonals_1 = board[0] == board[4] == board[8] != "-"
  diagonals_2 = board[6] == board[4] == board[2] != "-"

  # if any row has a match, flag that there is a win
  if diagonals_1 or diagonals_2:
    game_still_going = False
  
    
  if diagonals_1:
    return board[0]
  elif diagonals_2:
    return board[3]
  return

def check_if_cats_game():
  global game_still_going
  if "-" not in board:
    game_still_going = False

  return



def flip_player():
  #global varibals we need
  global current_player
  if current_player == "X":
    current_player = "O"
  elif current_player == "O":
    current_player = "X"
  return


play_game()
