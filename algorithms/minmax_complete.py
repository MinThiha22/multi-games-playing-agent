from evaluation.metrics import EvaluationMetrics
import time

# Minimax algorithm with complete depth first search
def minmax_complete(game, state, player, is_maximising):
  if game.is_terminal(state):
    return game.evaluate(state)
  
  legal_moves = game.get_legal_moves(state)
  
  if is_maximising:
    max_eval = float('-inf')
    for move in legal_moves:
      child_state = game.make_move(state, move, player)
      next_player = game.player2 if player == game.player1 else game.player1
      eval = minmax_complete(game, child_state, next_player, False)
      max_eval = max(max_eval, eval)
    return max_eval
  
  else:
    min_eval = float('inf')
    for move in legal_moves:
      child_state = game.make_move(state, move, player)
      next_player = game.player2 if player == game.player1 else game.player1
      eval = minmax_complete(game, child_state, next_player, True)
      min_eval = min(min_eval, eval)
    return min_eval
  
# Minimax_Complete function to find the best move
def best_move_complete(game, state, player):
  is_maximising = (player == game.player1)
  best_eval = float('-inf') if is_maximising else float('inf')
  best_move = None
  
  metr = EvaluationMetrics()
  node_explored = 0
  start_time = time.time()
  
  for move in game.get_legal_moves(state):
    node_explored += 1
    child_state = game.make_move(state, move, player)
    next_player = game.player2 if player == game.player1 else game.player1
    eval = minmax_complete(game, child_state, next_player, not is_maximising)
    
    if is_maximising:
      if eval > best_eval:
        best_eval = eval
        best_move = move
    else:
      if eval < best_eval:
        best_eval = eval
        best_move = move

  metr.nodes_explored = node_explored
  metr.execution_time = time.time() - start_time
  
  return best_move, metr