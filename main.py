from ui.tic_tac_toe_ui import tic_tac_toe_ui
from ui.nim_ui import nim_ui

if __name__ == "__main__":
  while True:
    print("Welcome to Muli-Games-Playing Agent")
    print("1. Tic Tac Toe")
    print("2. Nim")
    print("3. Tiger vs Dogs")
    print("4. Custom Own Game")
    print("5. Exit")
    choice = input("Choose an option (1-5): ")
    match choice:
      case '1':
        tic_tac_toe_ui()
      case '2':
        nim_ui()
      case '3':
        print("Tiger vs Dogs game is not implemented yet.")
      case '4':
        print("New game is not implemented yet.")
      case '5':
        print("Exiting the game...")
        exit()
      case _:
        print("Invalid choice. Please try again.")