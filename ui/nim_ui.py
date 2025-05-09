from games.nim import Nim
from ui.nim_game_modes import manual_game, ai_human_game, ai_ai_game

def scalable_nim():
  print("Scalable Nim")
  while True:
    x = input("Enter number of Heap/Row (x): ")
    y = input("Enter max size of heap (y): ")
    
    if x.isdigit() and y.isdigit():
      x,y = int(x), int(y)
      break
    else:
      print("Invalid input. Please enter positive integers.")
      
  game = Nim(x,y)
  print(f"Game initialized with {x} heaps/rows and max number of sticks {y}")
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

def nim_ui():
  print("\nWelcome to Nim!")
  print("1. Manual Game")
  print("2. AI vs Human Game")
  print("3. AI vs AI Evaluation")
  print("4. Scalable Nim Game")
  print("5. Back to Main Menu")
  
  game = Nim()
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
        scalable_nim()
        break
      case '5':
        print("Exiting Nim...")
        print("Going back to main menu...")
        return
      case _:
        print("Invalid choice. Please try again.")
  
  print('Thank you for playing!')
  print('Returning to menu...')
  print('=='*50)
  nim_ui() 