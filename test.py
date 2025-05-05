class TigerVsDogsTest:
  def __init__(self):
    self.board_size = 5
    self.dog = 'D'
    self.tiger = 'T'
    self.EMPTY = '.'

    # Paste your updated check_and_kill_dogs here
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
            board[x1][y1] == self.dog and board[x2][y2] == self.dog
        ):
          blocked = False
          nx, ny = x1 + dir1[0], y1 + dir1[1]
          while 0 <= nx < self.board_size and 0 <= ny < self.board_size:
            if board[nx][ny] == self.dog:
                blocked = True
                break
            elif board[nx][ny] != self.EMPTY:
                break
            nx += dir1[0]
            ny += dir1[1]

          nx, ny = x2 + dir2[0], y2 + dir2[1]
          while 0 <= nx < self.board_size and 0 <= ny < self.board_size:
            if board[nx][ny] == self.dog:
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

  
def print_board(board):
  for row in board:
      print(' '.join(row))
  print()
# Example test
if __name__ == "__main__":

  game = TigerVsDogsTest()
  print("Test 1: Vertical kill")
  board1 = [
      ['.', '.', '.', '.', '.'],
      ['.', '.', 'D', '.', '.'],
      ['.', '.', 'T', '.', '.'],
      ['.', '.', 'D', '.', '.'],
      ['.', '.', '.', '.', '.']
  ]

  game = TigerVsDogsTest()
  print_board(board1)
  killed = game.check_and_kill_dogs(board1, 2, 2)
  print(f"Killed: {killed}")
  print_board(board1)
  
  print("Test 2: Blocked by 3rd dog in vertical line")
  board2 = [
      ['.', '.', '.', '.', '.'],
      ['.', '.', 'D', '.', '.'],
      ['.', '.', 'T', '.', '.'],
      ['.', '.', 'D', '.', '.'],
      ['.', '.', 'D', '.', '.']  # Extra dog below
  ]

  print_board(board2)
  killed = game.check_and_kill_dogs(board2, 2, 2)
  print(f"Killed: {killed}")
  print_board(board2)
  
  print("Test 3:")
  board3 = [
      ['D', 'D', 'D', '.', '.'],
      ['D', 'T', '.', '.', '.'],
      ['D', '.', '.', '.', '.'],
      ['.', '.', '.', '.', '.'],
      ['.', '.', '.', '.', '.']
  ]

  print_board(board3)
  killed = game.check_and_kill_dogs(board3, 1, 1)
  print(f"Killed: {killed}")
  print_board(board3)
  
  print("Test 4: Diagonal kill")
  board4 = [
      ['.', '.', '.', '.', '.'],
      ['.', 'D', '.', '.', '.'],
      ['.', '.', 'T', '.', '.'],
      ['.', '.', '.', 'D', '.'],
      ['.', '.', '.', '.', '.']
  ]

  print_board(board4)
  killed = game.check_and_kill_dogs(board4, 2, 2)
  print(f"Killed: {killed}")
  print_board(board4)