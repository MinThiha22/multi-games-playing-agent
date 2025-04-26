from evaluate.metrics import EvaluationMetrics
import time

# Alpha beta pruning algorithm with limited depth
def alphabeta_limited(game, state, depth, player, alpha, beta, is_maximising):
  if depth == 0 or game.is_terminal(state):
    return game.evaluate(state)
  if alpha >= beta:
    return 0 
  legal_moves = game.get_legal_moves(state) 
  
  if is_maximising:
    max_eval = float('-inf')
    for move in legal_moves:
      child_state = game.make_move(state, move, player)
      next_player = game.player2 if player == game.player1 else game.player1
      eval = alphabeta_limited(game, child_state, depth-1, next_player, alpha, beta, False)
      max_eval = max(max_eval, eval)
      alpha = max(alpha, eval)
      if alpha >= beta:
        break
    return max_eval
  
  else:
    min_eval = float('inf')
    for move in legal_moves:
      child_state = game.make_move(state, move, player)
      next_player = game.player2 if player == game.player1 else game.player1
      eval = alphabeta_limited(game, child_state, depth-1, next_player, alpha, beta, True)
      min_eval = min(min_eval, eval)
      beta = min(beta, eval)
      if alpha >= beta:
        break
    return min_eval

# Alpha Beta Limited function to find the best move
def best_move_ab_limited(game, state, depth, player, alpha=float('-inf'), beta=float('inf')):
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
    eval = alphabeta_limited(game, child_state, depth-1, next_player, alpha, beta, not is_maximising)
    
    if is_maximising:
      if eval > best_eval:
        best_eval = eval
        best_move = move
      alpha = max(alpha, eval)
    else:
      if eval < best_eval:
        best_eval = eval
        best_move = move
      beta = min(beta, eval)
    if beta <= alpha:
      break
    
  metr.nodes_explored = node_explored
  metr.execution_time = time.time() - start_time
  
  return best_move, metr