from games.custom_game import TakeAway
from ui.custom_game_modes import manual_game, ai_human_game, ai_ai_game

def scalable_takeaway():
  print("Scalable Take Away Game")
  while True:
    x = input("Enter number of chips:(x): ")
    if x.isdigit():
      x = int (x)
      break
    else:
      print("Invalid input. Please enter positive integers.")
  
  game = TakeAway(x)
  print(f"Game initialized with {x} chips")
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

def custom_game_ui():
  print("\nWelcome to Custom Game (Take Away Game)!")
  print("1. Manual Game")
  print("2. AI vs Human Game")
  print("3. AI vs AI Evaluation")
  print("4. Scalable Take Away game")
  print("5. Exit")
  game = TakeAway()
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
        scalable_takeaway()
        break
      case '5':
        print("Exiting Take Away...")
        print("Going back to main menu...")
        return
      case _:
        print("Invalid choice. Please try again.")
  
  print('Thank you for playing!')
  print('Returning to menu...')
  print('=='*50)
  custom_game_ui()