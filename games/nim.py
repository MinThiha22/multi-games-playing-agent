from games.game import Game
from evaluation.metrics import EvaluationMetrics
from copy import deepcopy
import random, time

class Nim(Game):
  def __init__(self, num_heaps=4, max_heap_size=7):
    self.state = [random.randint(1, max_heap_size) for _ in range(num_heaps)]
    self.player1 = 1
    self.player2 = 2
    self.current_player = self.player1
  
  def get_initial_state(self):
    return self.state
  
  def change_player(self):
    if self.current_player == self.player1:
      self.current_player = self.player2
    else:
      self.current_player = self.player1
  
  def get_legal_moves(self, state):
    legal_moves = []
    for i in range(len(state)):
      for j in range(1, state[i] + 1):
        legal_moves.append((i, j))
    return legal_moves
  
  def is_valid_move(self, state, move):
    i,j = move
    return 0 <= i < len(state) and 1 <= j <= state[i]
  
  def make_move(self, state, move, player=None, evaluate = False):
    copy_state = deepcopy(state)
    i,j = move
    if self.is_valid_move(copy_state, move):
      copy_state[i] -= j
    return copy_state
  
  def is_terminal(self, state):
    return all(pile == 0 for pile in state)
  
  def get_winner(self, state, player):
    if self.is_terminal(state):
      return player
    return None 

  def evaluate(self, state, player):
    # Evaluate the state based on the current player’s perspective
    if self.is_terminal(state):
      winner = self.get_winner(state, player)
      if winner == self.player1:
        return 1  # Player 1 wins
      elif winner == self.player2:
        return -1  # Player 2 wins
      else:
        return 0  # Draw or no winner yet
    return 0 
  
  def display(self, state):
    for i, j in enumerate(state):
      print(f"Row {i}: {'|' * j}")
  
  def random_move(self, state):
    metr = EvaluationMetrics()
    start_time = time.time()
    legal_moves = self.get_legal_moves(state)
    if legal_moves:
      metr.execution_time = time.time() - start_time
      return random.choice(legal_moves), metr
    return None
