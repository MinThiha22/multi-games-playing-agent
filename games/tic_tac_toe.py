from games.game import Game
class TicTacToe(Game):
  player1 = 'X'
  player2 = 'O'
  EMPTY = ' '
  
  def __init__(self, current_player=player1):
    self.state = [[' ' for _ in range(3)] for _ in range(3)]
    self.current_player = current_player
    
  def get_initial_state(self):
    return self.state
  
  def get_legal_moves(self, state):
    legal_moves = []
    for i in range(3):
      for j in range(3):
        if state[i][j] == self.EMPTY:
          legal_moves.append((i, j))
    return legal_moves
  
  def is_valid_move(self, state, move):
    i, j = move
    return 0 <= i < 3 and 0 <= j < 3 and state[i][j] == self.EMPTY
  
  def make_move(self, state, move, player):
    copy_state = [row[:] for row in state]
    i, j = move
    if copy_state[i][j] == self.EMPTY:
      copy_state[i][j] = player
    return copy_state
  
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
  
  def evaluate(self, state):
    winner = self.get_winner(state)
    if winner == self.player1:
      return 1
    elif winner == self.player2:
      return -1
    else:
      return 0
    
  def is_terminal(self, state):
    return self.get_winner(state) is not None or all(cell != self.EMPTY for row in state for cell in row)
    
  def display(self, state):
    for i in range(3):
      print(' | '.join(state[i]))
      if i < 2:
        print('--+---+--')
  
  
      
  