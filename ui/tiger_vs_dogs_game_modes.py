from evaluation.compare_ai import compare_ai
from algorithms.minmax_complete import best_move_complete
from algorithms.minmax_limited import best_move_limited
from algorithms.alphabeta_complete import best_move_ab_complete
from algorithms.alphabeta_limited import best_move_ab_limited

def manual_game(game):
  state = game.get_initial_state()
  while not game.is_terminal(state):
    print(f"Player {game.current_player}'s turn.")
    game.display(state)
    legal_moves = game.get_legal_moves(state)
    print("Legal moves:", legal_moves)

    move = input("Enter your move from current (row,col) to new (row,col) (eg. 0,0 0,1): ")
    try:
      parts = move.strip().split()
      current = tuple(map(int,parts[0].split(",")))
      next = tuple(map(int,parts[1].split(",")))
      move = (current, next)
      if not game.is_valid_move(state, move):
          print("Invalid move. Try again.")
          continue
    except:
      print("Invalid input format. Try again.")
      continue
    state = game.make_move(state, move, game.current_player)
    
    game.change_player()
    game.display(state)

  print("--" * 25)
  winner = game.get_winner(state)
  print(f"Winner: {winner}")

    
def ai_human_game(game):
  while True:
    algorithm = input("Choose AI algorithm (1. Minimax Complete, 2. Minimax Limited, 3. Alphabeta Complete, 4. Alphabeta Limited): ")
    if algorithm in ['1', '3']:
      break
    elif algorithm in ['2', '4']:
      while True:
        depth = input("Enter depth (e.g., 2): ")
        if depth.isdigit() and int(depth) > 0:
          depth = int(depth)
          break
        else:
          print("Invalid depth. Please enter a positive integer.")
      break
    else:
      print("Invalid choice. Please choose 1, 2, 3, or 4.")
      
  while True:
    first_move = input("Who should play first? (1. You, 2. AI): ")
    if first_move in ['1', '2']:
      break
    else: 
      print("Invalid choice. Please choose '1' or '2'.")
  
  state = game.get_initial_state()
  game.display(state)
  
  game.killed_dogs = 0

  human_player = game.player1 if first_move == '1' else game.player2

  while not game.is_terminal(state):
    legal_moves = game.get_legal_moves(state)
    print("Legal Moves:", legal_moves)
    
    if not legal_moves:
      print(f"No legal moves for {game.current_player}. Game over!")
      break
    
    if game.current_player == human_player:
       
      print(f"Your turn ({game.current_player})")

      while True:
        move = input("Enter your move from current (row,col) to new (row,col) (eg. 0,0 0,1): ")
        try:
          parts = move.strip().split()
          current = tuple(map(int, parts[0].split(",")))
          next = tuple(map(int, parts[1].split(",")))
          move = (current, next)
          if game.is_valid_move(state, move):
            break
          else:
            print("Invalid move. Try again.")
        except:
          print("Invalid input format. Try again.")
          
      state = game.make_move(state, move, game.current_player)
    else:
      print(f"AI's turn ({game.current_player})")
      print("AI is thinking...")
      if algorithm == '1':
        move, metrics = best_move_complete(game, state, game.current_player)
      elif algorithm == '2':
        move, metrics = best_move_limited(game, state, depth, game.current_player)
      elif algorithm == '3':
        move, metrics = best_move_ab_complete(game, state, game.current_player)
      elif algorithm == '4':
        move, metrics = best_move_ab_limited(game, state, depth, game.current_player)
        
      print(f"AI ({game.current_player}) chooses move: {move}")
      state = game.make_move(state, move, game.current_player)
    
    game.display(state)
    
    # Check if game is over after the move
    winner = game.get_winner(state)
    if winner:
      print(f"Winner: {winner}")
      break
      
    # Change player for next turn
    game.change_player()

  print("--" * 25)
  winner = game.get_winner(state)
  if winner:
    print(f"Winner: {winner}")
  else:
    print("Game ended in a draw.")
  
  print("Thank you for playing!")
  print("Returning to main menu...")

def ai_ai_game(game):
  print("\n5 algorithms available to evaluate")
  print("1. Minimax Complete")
  print("2. Minimax Limited")
  print("3. Alpha-Beta Pruning Complete")
  print("4. Alpha-Beta Pruning Limited")
  print("5. Random Move algorithm (Baseline)")
  
  algorithms = {
      '1': 'complete',
      '2': 'limited',
      '3': 'ab_complete',
      '4': 'ab_limited',
      '5': 'random'
  }
  
  while True:
    input1 = input("Choose AI algorithm for player1 (1-5): ")
    input2 = input("Choose AI algorithm for player2 (1-5): ")
    
    if input1 in algorithms and input2 in algorithms:
      algorithm1 = algorithms.get(input1)
      algorithm2 = algorithms.get(input2)
      
      while True:
        depth1 = int(input(f"Enter depth for algorithm 1 ({algorithm1}) (e.g. 2): ")) if algorithm1 in ['limited', 'ab_limited'] else None
        depth2 = int(input(f"Enter depth for algorithm 2 ({algorithm2}) (e.g. 2): ")) if algorithm2 in ['limited', 'ab_limited'] else None
        
        if (depth1 is None or depth1 > 0) and (depth2 is None or depth2 > 0):
          break
        else:
          print("Invalid. Both depths must be positive integers. Try again.")
      break
    else:
      print("Invalid choice. Please choose valid options from the list.")
  
  result = compare_ai(game, algorithm1, algorithm2, depth1, depth2)  
  print(f"Player 1 ({algorithm1}) vs Player 2 ({algorithm2})")
  print(f"{result}")