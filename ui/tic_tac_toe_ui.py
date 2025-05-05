from games.tic_tac_toe import TicTacToe
from ui.tic_tac_toe_game_modes import manual_game, ai_human_game, ai_ai_game

def scalable_m_n_k():
  print("Scalable Tic Tac Toe")
  while True:
    m = input("Enter number of rows (m): ")
    n = input("Enter number of columns (n): ")
    k = input("Enter number of consecutive marks to win (k): ")
    
    if m.isdigit() and n.isdigit() and k.isdigit():
      m, n, k = int(m), int(n), int(k)
      break
    else:
      print("Invalid input. Please enter positive integers.")
  
  game = TicTacToe(m, n, k)
  print(f"Game initialized with {m} rows, {n} columns, and {k} consecutive marks to win.")
  print("1. Manual Game")
  print("2. AI vs Human Game")
  print("3. AI vs AI Evaluation")
  while True:
    choice = input("Choose an option (1-3): ")
    match choice:
      case '1':
        manual_game(game)
        break
      case '2':
        ai_human_game(game)
        break
      case '3':
        ai_ai_game(game)
        break
      case _:
        print("Invalid choice. Please try again.")

def tic_tac_toe_ui():
  print("\nWelcome to Tic Tac Toe!")
  print("1. Manual Game")
  print("2. AI vs Human Game")
  print("3. AI vs AI Evaluation")
  print("4. Scalable (m,n,k) game")
  print("5. Exit")
  game = TicTacToe()
  while True:
    choice = input("Choose an option (1-5): ")
    match choice:
      case '1':
        manual_game(game)
        break
      case '2':
        ai_human_game(game)
        break
      case '3':
        ai_ai_game(game)
        break
      case '4':
        scalable_m_n_k()
        break
      case '5':
        print("Exiting Tic Tac Toe...")
        print("Going back to main menu...")
        return
      case _:
        print("Invalid choice. Please try again.")
  
  print('Thank you for playing!')
  print('Returning to menu...')
  print('=='*50)
  tic_tac_toe_ui()