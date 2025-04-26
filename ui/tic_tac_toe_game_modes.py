from games.tic_tac_toe import TicTacToe
from evaluate.compare_ai import compare_ai
from algorithms.minmax_complete import best_move_complete
from algorithms.minmax_limited import best_move_limited
from algorithms.alphabeta_complete import best_move_ab_complete
from algorithms.alphabeta_limited import best_move_ab_limited

def manual_game(game): 
  while True:
    first_player = input("Choose your player (X or O): ").upper()
    if first_player in ['X', 'O']:
      break
    else:
      print("Invalid choice. Please choose 'X' or 'O'.")

  print("**"*25)
  print(f"You are playing as {first_player}.")
  game.current_player = first_player
  print("**"*25)
  state = game.get_initial_state()
  print("Initial State:")
  game.display(state)
  
  while not game.is_terminal(state):
    legal_moves = game.get_legal_moves(state)
    print("Legal Moves:", legal_moves)
    
    move = input("Enter your move (row,col) or 'q' to quit: ")
    if move.lower() == 'q':
      print("Exiting the game...")
      break
    try: 
        move = tuple(map(int, move.split(',')))
        if move not in legal_moves:
            print("Invalid move. Try again.")
            continue
    except ValueError:
        print("Invalid input. Please enter row,col format.")
        continue
      
    # Make the move
    if move:
        state = game.make_move(state, move, game.current_player)
        print(f"Player {game.current_player} makes move: {move}")
        game.display(state)
        game.change_player()
    else:
        break
      
  print("--"*25)
  winner = game.get_winner(state)
  if winner:
      print(f"Winner: {winner}")
  else:
      print("It's a draw!")

def ai_human_game(game):
  # Choose AI algorithm
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
      print("Invalid choice. Please choose '1' or '2'.")
  
  # Choose player symbol
  while True:
    human = input("Choose your player (X or O): ").upper()
    if human in ['X', 'O']:
      break
    else:
      print("Invalid choice. Please choose 'X' or 'O'.")
  ai = 'O' if human == 'X' else 'X'
  # Choose first move
  while True:
    first_move = input("Who should play first? (1. You, 2. AI): ")
    if first_move in ['1', '2']:
      break
    else: 
      print("Invalid choice. Please choose '1' or '2'.")
  
  if first_move == '1':
    game.player1 = human
    game.player2 = ai
    game.current_player = human
  else:
    game.player1 = ai
    game.player2 = human
    game.current_player = ai
  
  print("**"*25)
  print(f"You are playing as {human} and AI is playing as {ai}.")
  print("**"*25)
  print(f"{'You' if first_move == '1' else 'AI'} will play first.")
  
  state = game.get_initial_state()
  print("Initial State:")
  game.display(state)
  
  while not game.is_terminal(state):
    legal_moves = game.get_legal_moves(state)
    print("Legal Moves:", legal_moves)
    
    # AI move
    if game.current_player == ai:
      print("AI is thinking...")
      if algorithm == '1':
        move, metrics = best_move_complete(game, state, game.current_player)
      elif algorithm == '2':
        move, metrics = best_move_limited(game, state, depth, game.current_player)
      elif algorithm == '3':
        move, metrics = best_move_ab_complete(game, state, game.current_player)
      elif algorithm == '4':
        move, metrics = best_move_ab_limited(game, state, depth, game.current_player)
      print(f"AI ({game.current_player}) makes move: {move}")
       
    # Human move
    else:
      move = input("Enter your move (row,col) or 'q' to quit: ")
      if move.lower() == 'q':
        print("Exiting the game...")
        exit()
      try:
        move = tuple(map(int, move.split(',')))
        if move not in legal_moves:
            print("Invalid move. Try again.")
            continue
      except ValueError:
        print("Invalid input. Please enter row,col format.")
        continue
      print(f"Player {game.current_player} makes move: {move}")
    
    state = game.make_move(state, move, game.current_player)
    game.change_player()
    game.display(state)
        
  score = game.evaluate(state)
  print("--"*25)
  if score == 1:
    print(f"Winner: {game.player1}")
  elif score == -1:
    print(f"Winner: {game.player2}")
  else: 
    print("It's a draw!")

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