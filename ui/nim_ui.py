from games.nim import Nim
from ui.nim_game_modes import manual_game, ai_human_game, ai_ai_game

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
        #scalable_nim()
        break
      case '5':
        print("Exiting Nim...")
        print("Going back to main menu...")
        return
      case _:
        print("Invalid choice. Please try again.")
  
  print('Thank you for playing!')
  print('Returning to main menu...')
  print('=='*50)
  nim_ui() 