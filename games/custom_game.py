# Take Away Game
from games.game import Game
from evaluation.metrics import EvaluationMetrics
from copy import deepcopy
import random, time

class TakeAway(Game):
  def __init__(self, starting_chips=15):
    self.player1 = '1'
    self.player2 = '2'
    self.starting_tokens = starting_chips
    self.current_player = self.player1  # Default to player1

  def get_initial_state(self):
    return self.starting_tokens

  def change_player(self):
    self.current_player = self.player1 if self.current_player == self.player2 else self.player2

  def get_legal_moves(self, state):
    # Players can take 1, 2, or 3 tokens, but not more than the remaining chips
    return [x for x in [1,2,3] if x <= state]

  def is_valid_move(self, state, move):
    return move in self.get_legal_moves(state)

  def make_move(self, state, move, player=None, evaluate=False):
    new_state = deepcopy(state)
    new_state = state - move
    return new_state

  def get_winner(self, state, player=None):
    if state == 0:
      return self.player1 if self.current_player == self.player2 else self.player2
    return None

  def is_terminal(self, state):
    return state == 0

  def evaluate(self, state, player):
    if self.is_terminal(state):
      return -1 if player == self.player1 else 1
    return 0
  
  def display(self, state):
    print(f"Chips remaining: {state}")
           
  # Random move
  def random_move(self, state):
    metr = EvaluationMetrics()
    start_time = time.time()
    legal_moves = self.get_legal_moves(state)
    if legal_moves:
      metr.execution_time = time.time() - start_time
      return random.choice(legal_moves), metr
    return None
