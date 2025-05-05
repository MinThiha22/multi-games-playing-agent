from games.tiger_vs_dogs import TigerVsDogs
from ui.tiger_vs_dogs_game_modes import manual_game, ai_human_game, ai_ai_game
def tiger_vs_dogs_ui():
  print("\nWelcome to Tiger vs Dogs!")
  print("1. Manual Game")
  print("2. AI vs Human Game")
  print("3. AI vs AI Evaluation")
  print("4. Back to Main Menu")
  
  game = TigerVsDogs()
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
        print("Exiting Tiger vs Dogs...")
        print("Going back to main menu...")
        return
      case _:
        print("Invalid choice. Please try again.")
  
  print('Thank you for playing!')
  print('Returning to menu...')
  print('=='*50)
  tiger_vs_dogs_ui() 