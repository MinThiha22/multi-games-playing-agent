from abc import ABC, abstractmethod

class Game(ABC):
  
  @abstractmethod
  def get_initial_state(self):
    """Returns the initial state of the game."""
    pass
  
  def get_current_player(self):
    """Returns the current player."""
    pass
  
  @abstractmethod
  def get_legal_moves(self, state):
    """Returns a list of possible legal moves from the given state."""
    pass
  
  @abstractmethod
  def is_valid_move(self, state, move):
    """Returns True if the move is valid in the given state, False otherwise."""
    pass
  
  @abstractmethod
  def make_move(self, state, move,player):
    """Returns the new state after making the given move from the current state."""
    pass
  
  @abstractmethod
  def is_terminal(self, state):
    """Returns True if the game is over, False otherwise."""
    pass
  
  @abstractmethod
  def evaluate(self, state):
    """Returns the value of the given state for the current player."""
    pass
  
  @abstractmethod
  def get_winner(self, state):
    """Returns the winner of the game if it is over, otherwise None."""
    pass
  
  @abstractmethod
  def display(self, state):
    """Displays the current state of the game."""
    pass