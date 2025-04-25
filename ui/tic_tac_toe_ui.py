from games.tic_tac_toe import TicTacToe
from evaluate.compare_ai import compare_ai
from algorithms.minmax_complete import best_move_complete
from algorithms.minmax_limited import best_move_limited

def manual_game(game): 
  while True:
    first_player = input("Choose your player (X or O): ").upper()
    if first_player in ['X', 'O']:
      break
    else:
      print("Invalid choice. Please choose 'X' or 'O'.")

  print(f"You are playing as {first_player}.")
  game.current_player = first_player

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
  
  winner = game.get_winner(state)
  if winner:
      print(f"Winner: {winner}")
  else:
      print("It's a draw!")

def ai_human_game(game):
  # Choose AI algorithm
  while True:
    algorithm = input("Choose AI algorithm (1. Minimax Complete, 2. Minimax Limited): ")
    if algorithm == '1':
      break
    elif algorithm == '2':
      while True:
        depth = input("Enter depth for Minimax Limited (e.g., 2): ")
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
  
  print(f"You are playing as {human} and AI is playing as {ai}.")
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
      move, metrics = best_move_complete(game, state, game.current_player) if algorithm == '1' else best_move_limited(game, state, depth, game.current_player)
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
  if score == 1:
    print(f"Winner: {game.player1}")
  elif score == -1:
    print(f"Winner: {game.player2}")
  else: 
    print("It's a draw!")

def ai_ai_game(game):
  algorithms = {
      '1': 'Minimax Complete',
      '2': 'Minimax Limited',
      '3': 'Alpha Beta Complete',
      '4': 'Alpha Beta Limited',
      '5': 'Random'
  }
  for key, value in algorithms.items():
      print(f"{key}. {value}")
  
  while True:
      input1 = input("Choose AI algorithm for player1: ")
      input2 = input("Choose AI algorithm for player2: ")
      if input1 in algorithms and input2 in algorithms:
          break
      else:
          print("Invalid choice. Please choose valid options from the list.")
  
  result = compare_ai(game, "complete", "ab_complete", num_games=10)
  print(f"Complete vs Limited: {result}")
    
       
def tic_tac_toe_ui():
  print("Welcome to Tic Tac Toe!")
  print("1. Manual Game")
  print("2. AI vs Human Game")
  print("3. AI vs AI Evaluation")
  print("4. Exit")
  game = TicTacToe()
  while True:
    choice = input("Choose an option (1-4): ")
    match choice:
      case '1':
        manual_game(game)
        break
      case '2':
        ai_human_game(game)
        break
      case '3':
        ai_ai_game(game)
      case '4':
        print("Exiting the game...")
        exit()
      case _:
        print("Invalid choice. Please try again.")
  
  print('Thank you for playing!')
 
  