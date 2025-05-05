from algorithms.minmax_complete import best_move_complete
from algorithms.minmax_limited import best_move_limited
from algorithms.alphabeta_complete import best_move_ab_complete
from algorithms.alphabeta_limited import best_move_ab_limited

def compare_ai(game, algorithm1, algorithm2, depth1=None, depth2=None, num_games=10):
  
  algo1_name = f"{algorithm1}" + (f"_depth{depth1}" if algorithm1 in ["limited", "ab_limited"]else "")
  algo2_name = f"{algorithm2}" + (f"_depth{depth2}" if algorithm2 in ["limited", "ab_limited"] else "")
  print("**"*25)
  print(f"Comparing {algo1_name} (X) vs {algo2_name} (O) for {num_games} games.......")
  print("**"*25)
  results = {
    f'{algo1_name}_wins': 0,
    f'{algo2_name}_wins': 0,
    'draw': 0
  }

  for i in range(num_games):
    state = game.get_initial_state()
    game.state_history = []
    print("Playing Game", i + 1)
    
    # Assign players
    game.current_player = game.player1
    player_1_total_excution_time = 0
    plyaer_2_total_excution_time = 0
  
    while not game.is_terminal(state):
      if game.__class__.__name__ == "TigerVsDogs":
        state_hash = tuple(tuple(row) for row in state)
        game.state_history.append(state_hash)
      if game.current_player == game.player1:
        if algorithm1 == "complete":
          move, metrics = best_move_complete(game, state, game.current_player)
        elif algorithm1 == "ab_complete":
          move, metrics = best_move_ab_complete(game, state, game.current_player)
        elif algorithm1 == "limited":
          move, metrics = best_move_limited(game, state, depth1, game.current_player)
        elif algorithm1 == "ab_limited":
          move, metrics = best_move_ab_limited(game, state, depth1, game.current_player)
        elif algorithm1 == "random":
          move, metrics = game.random_move(state)
        
        player_1_total_excution_time += metrics.execution_time
      
      else:
        if algorithm2 == "complete":
          move, metrics = best_move_complete(game, state, game.current_player)
        elif algorithm2 == "ab_complete":
          move, metrics = best_move_ab_complete(game, state, game.current_player)
        elif algorithm2 == "limited":
          move, metrics = best_move_limited(game, state, depth2, game.current_player)
        elif algorithm2 == "ab_limited":
          move, metrics = best_move_ab_limited(game, state, depth2, game.current_player)
        elif algorithm2 == "random":
          move, metrics = game.random_move(state)
        
        plyaer_2_total_excution_time += metrics.execution_time
      
      print(f"Player {game.current_player} current move: {move}")
      metrics.display()
      print("" + "-"*50)
      
      state = game.make_move(state, move, game.current_player)
      game.change_player()

    print(f"Player X total execution time: {player_1_total_excution_time:.4f}")
    print(f"Player O total execution time: {plyaer_2_total_excution_time:.4f}")
    print("Final Board State:")
    game.display(state)
    winner = game.get_winner(state, game.current_player)
    if winner == game.player1:
      results[f'{algo1_name}_wins'] += 1
    elif winner == game.player2:
      results[f'{algo2_name}_wins'] += 1
    else:
      results['draw'] += 1
    print("End of Game", i + 1)
    print("="*50)
  return results
