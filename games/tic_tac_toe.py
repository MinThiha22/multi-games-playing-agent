import random
from games.game import Game
from copy import deepcopy

class TicTacToe(Game):
  def __init__(self, m=3, n=3, k=3):
    self.player1 = 'X'
    self.player2 = 'O'
    self.EMPTY = ' '
    self.m = m
    self.n = n
    self.k = k
    self.state = [[self.EMPTY for _ in range(n)] for _ in range(m)]
    self.current_player = self.player1 # Default to player1
    
  def get_initial_state(self):
    return self.state
  
  def change_player(self):
    if self.current_player == self.player1:
      self.current_player = self.player2
    else:
      self.current_player = self.player1
  
  def get_legal_moves(self, state):
    legal_moves = []
    for i in range(self.m):
      for j in range(self.n):
        if state[i][j] == self.EMPTY:
          legal_moves.append((i, j))
    return legal_moves
  
  def is_valid_move(self, state, move):
    i, j = move
    return 0 <= i < self.m and 0 <= j < self.n and state[i][j] == self.EMPTY
  
  def make_move(self, state, move, player):
    copy_state = deepcopy(state)
    i, j = move
    if copy_state[i][j] == self.EMPTY:
      copy_state[i][j] = player
    return copy_state
  
  # get_winner method before scaling to m,n,k
  """ 
  def get_winner(self, state):
    # Check rows
    for row in state:
      if row[0] == row[1] == row[2] != self.EMPTY:
        return row[0]
    
    # Check columns
    for j in range(3):
      if state[0][j] == state[1][j] == state[2][j] != self.EMPTY:
        return state[0][j]
    
    # Check diagonals
    if state[0][0] == state[1][1] == state[2][2] != self.EMPTY:
      return state[0][0]
    if state[0][2] == state[1][1] == state[2][0] != self.EMPTY:
      return state[0][2]
    return None 
  """
 
  def get_winner(self, state):
    directions = [(0,1), (1,0), (1,1), (1,-1)]  # right, down, down-right, down-left
    for i in range(self.m):
      for j in range(self.n):
        if state[i][j] == self.EMPTY:
          continue
        player = state[i][j]
        for dx, dy in directions:
          count = 1
          x, y = i + dx, j + dy
          while 0 <= x < self.m and 0 <= y < self.n and state[x][y] == player:
            count += 1
            if count == self.k:
              return player
            x += dx
            y += dy
    return None
   
  def is_terminal(self, state):
    return self.get_winner(state) is not None or all(cell != self.EMPTY for row in state for cell in row)
  
  def evaluate(self, state):
    winner = self.get_winner(state)
    if winner == self.player1:
      return 1
    elif winner == self.player2:
      return -1
    else:
      return 0
  
  def display(self, state):
    for i in range(self.m):
      print(' | '.join(state[i]))
      if i < self.m - 1:
        print('--+' + '---+' * (self.n - 2) + '--')
                     
  #Random move
  def random_move(self, state, player):
    legal_moves = self.get_legal_moves(state)
    if legal_moves:
      return random.choice(legal_moves)
    return None
