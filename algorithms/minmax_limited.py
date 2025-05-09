from evaluation.metrics import EvaluationMetrics
import time

# Minimax algorithm with limited depth search
def minmax_limited(game, state, depth, player, is_maximising):
  if depth == 0 or game.is_terminal(state):
    return game.evaluate(state,player)
  
  legal_moves = game.get_legal_moves(state)

  if is_maximising:
    max_eval = float('-inf')
    for move in legal_moves:
      child_state = game.make_move(state, move, player, evaluate = True)
      next_player = game.player2 if player == game.player1 else game.player1
      eval = minmax_limited(game, child_state, depth-1, next_player, False)
      max_eval = max(max_eval, eval)
    return max_eval
  
  else:
    min_eval = float('inf')
    for move in legal_moves:
      child_state = game.make_move(state, move, player, evaluate = True)
      next_player = game.player2 if player == game.player1 else game.player1
      eval = minmax_limited(game, child_state, depth-1, next_player, True)
      min_eval = min(min_eval, eval)
    return min_eval
      

# Minimax_Limited function to find the best move
def best_move_limited (game, state, depth, player):
  is_maximising = (player == game.player1)
  best_eval = float('-inf') if is_maximising else float('inf')
  best_move = None 
  
  metr = EvaluationMetrics()
  node_explored = 0
  start_time = time.time()

  for move in game.get_legal_moves(state):
    node_explored += 1
    child_state = game.make_move(state, move, player, evaluate = True)
    next_player = game.player2 if player == game.player1 else game.player1
    eval = minmax_limited (game, child_state, depth-1, next_player, not is_maximising)

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