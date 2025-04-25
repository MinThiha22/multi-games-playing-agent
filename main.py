from ui.tic_tac_toe_ui import tic_tac_toe_ui

if __name__ == "__main__":
  print("Welcome to Muli-Games-Playing Agent")
  print("1. Tic Tac Toe")
  print("2. Nim")
  print("3. Tiger vs Dogs")
  print("4. Custom Own Game")
  print("5. Exit")
  
  while True:
    choice = input("Choose an option (1-5): ")
    match choice:
      case '1':
        tic_tac_toe_ui()
        break
      case '2':
        print("Nim game is not implemented yet.")
      case '3':
        print("Tiger vs Dogs game is not implemented yet.")
      case '4':
        print("New game is not implemented yet.")
      case '5':
        print("Exiting the game...")
        exit()
      case _:
        print("Invalid choice. Please try again.")