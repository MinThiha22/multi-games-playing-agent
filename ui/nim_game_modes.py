from games.nim import Nim
from evaluation.compare_ai import compare_ai
from algorithms.minmax_complete import best_move_complete
from algorithms.minmax_limited import best_move_limited
from algorithms.alphabeta_complete import best_move_ab_complete
from algorithms.alphabeta_limited import best_move_ab_limited

def manual_game(game):
  state = game.get_initial_state()
  while not game.is_terminal(state):
    game.display(state)    
    print(f"Player {game.current_player}'s turn.")
    
    row = input(f"Enter row number: ")
    if not row.isdigit() or not (0 <= int(row) < len(state)) or state[int(row)] == 0:
      print("Invalid row. Try again.")
      continue
    row = int(row)
    made_move = False
    while True:
      sticks = input(f"Enter number of sticks to remove from row {row} (1-{state[row]}) or 'n' to pass turn: ")
      if sticks.lower() == 'n' and made_move:
        print("Passing turn.")
        game.change_player()
        break
        
      if not sticks.isdigit() or not (1 <= int(sticks) <= state[row]):
        print("Invalid number of sticks. Try again.")
        continue
      
      sticks = int(sticks)
      move = (row,sticks)
      
      state = game.make_move(state, move)
      made_move = True
      print(f"Player {game.current_player} removes {sticks} from row {row}.")
      game.display(state)
      
      if game.is_terminal(state):
        print("--"*25)
        winner = game.get_winner(state)
        print(f"Winner: player {winner}")
        break
      
      if(state[row] == 0):
        print(f"Row {row} is empty. Passing turn.")
        game.change_player()
        break
      
  
  

def ai_human_game():
  pass

def ai_ai_game():
  pass