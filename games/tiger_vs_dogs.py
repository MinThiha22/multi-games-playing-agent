from games.game import Game
from evaluation.metrics import EvaluationMetrics
from copy import deepcopy
import random, time

class TigerVsDogs(Game):
  def __init__(self):
    self.player1 = 'T'
    self.player2 = 'D'
    self.EMPTY = '.'
    self.state_history = []
    self.board_size = 5
    self.killed_dogs = 0
    self.current_player = self.player1 
    self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

  def get_initial_state(self):
    board = [[self.EMPTY for _ in range(self.board_size)] for _ in range(self.board_size)]
    for i in [0, 4]:
      for j in range(self.board_size):
        board[i][j] = self.player2
    for i in range(1, 4):
        board[i][0] = board[i][4] = self.player2
    board[2][2] = self.player1
    return board
  
  def change_player(self):
    if self.current_player == self.player1:
      self.current_player = self.player2
    else:
      self.current_player = self.player1
  
  def get_legal_moves(self, state):
    legal_moves = []
    for i in range(self.board_size):
      for j in range(self.board_size):
        if state[i][j] == self.current_player:
          for dx, dy in self.directions:
            ni, nj = i + dx, j + dy
            if 0 <= ni < self.board_size and 0 <= nj < self.board_size and state[ni][nj] == '.':
                legal_moves.append(((i,j),(ni, nj)))
    return legal_moves

  def is_valid_move(self, state, move):
    (x1, y1), (x2, y2) = move
    if not (0 <= x1 < 5 and 0 <= y1 < 5 and 0 <= x2 < 5 and 0 <= y2 < 5):
      return False
    if state[x1][y1] != self.current_player or state[x2][y2] != '.':
      return False
    dx, dy = x2 - x1, y2 - y1
    return (dx, dy) in self.directions
  
  def make_move(self, state, move, player, evaluate = False):
    (x1, y1), (x2, y2) = move
    new_state = deepcopy(state)
    new_state[x2][y2] = player
    new_state[x1][y1] = '.'
    if player == self.player1 and not evaluate:
      killed = self.check_and_kill_dogs(new_state, x2, y2)
      self.killed_dogs += killed
      if killed > 0:
        print(f"Tiger killed {killed} dogs! Total killed: {self.killed_dogs}")
    return new_state
  
  def check_and_kill_dogs(self, board, x, y):
    killed = 0
    directions = [
      [(-1, 0), (1, 0)],  # Vertical
      [(0, -1), (0, 1)],  # Horizontal
      [(-1, -1), (1, 1)], # Diagonal TL–BR
      [(-1, 1), (1, -1)]  # Diagonal TR–BL
    ]

    for dir1, dir2 in directions:
      x1, y1 = x + dir1[0], y + dir1[1]
      x2, y2 = x + dir2[0], y + dir2[1]

      if (
          0 <= x1 < self.board_size and 0 <= y1 < self.board_size and
          0 <= x2 < self.board_size and 0 <= y2 < self.board_size and
          board[x1][y1] == self.player2 and board[x2][y2] == self.player2
      ):
        blocked = False
        nx, ny = x1 + dir1[0], y1 + dir1[1]
        while 0 <= nx < self.board_size and 0 <= ny < self.board_size:
          if board[nx][ny] == self.player2:
            blocked = True
            break
          elif board[nx][ny] != self.EMPTY:
            break
          nx += dir1[0]
          ny += dir1[1]

        nx, ny = x2 + dir2[0], y2 + dir2[1]
        while 0 <= nx < self.board_size and 0 <= ny < self.board_size:
          if board[nx][ny] == self.player2:
            blocked = True
            break
          elif board[nx][ny] != self.EMPTY:
            break
          nx += dir2[0]
          ny += dir2[1]

        if not blocked:
          board[x1][y1] = self.EMPTY
          board[x2][y2] = self.EMPTY
          killed += 2
    return killed
  
  def get_winner(self, state,player=None):
    # Tiger wins if enough dogs are killed
    if self.killed_dogs >= 6:
      return self.player1
    
    legal_moves = self.get_legal_moves(state)
    if not legal_moves:
      # If it's Tiger's turn and no moves, dogs win and vice versa
      return self.player2 if self.current_player == self.player1 else self.player1
    
    if self.state_history.count(tuple(tuple(row) for row in state)) >= 3:
      print("Detected looped states. Ending game as a draw.")
      return "draw"

  def evaluate(self, state, player=None):
    winner = self.get_winner(state)
    if winner == self.player1:
      return 1
    elif winner == self.player2:
      return -1
    return 0
  
  
  def is_terminal(self, state):
    return self.get_winner(state) 

  def display(self, state):
    print('\n'.join(' '.join(row) for row in state))

  def random_move(self, state):
    metr = EvaluationMetrics()
    start_time = time.time()
    legal_moves = self.get_legal_moves(state)
    if legal_moves:
      metr.execution_time = time.time() - start_time
      return random.choice(legal_moves), metr
    return None
   
  