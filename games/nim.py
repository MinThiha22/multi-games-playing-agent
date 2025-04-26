from games.game import Game
from copy import deepcopy
import random

class Nim(Game):
  def __init__(self, piles=[1, 3, 5, 7]):
    self.state = piles
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
  
  def make_move(self, state, move):
    copy_state = deepcopy(state)
    i,j = move
    if self.is_valid_move(copy_state, move):
      copy_state[i] -= j
    return copy_state
  
  def is_terminal(self, state):
    return all(pile == 0 for pile in state)
  
  def get_winner(self, state):
    if self.is_terminal(state):
      return self.player2 if self.current_player == self.player1 else self.player1
    return None
  
  def evaluate(self, state):
    winner = self.get_winner(state)
    if winner == self.player1:
      return 1
    elif winner == self.player2:
      return -1
    else:
      return 0
    
  def display(self, state):
    num_rows = len(state)
    for i,j in enumerate(state):
      print(" " * (len(state) - i - 1) + "|" * j + " " * (len(state) - i - 1) + "\n")
  
  def random_move(self, state):
    legal_moves = self.get_legal_moves(state)
    if legal_moves:
      return random.choice(legal_moves)
    return
