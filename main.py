from games.tic_tac_toe import TicTacToe
def main():
    game = TicTacToe()
    state = game.get_initial_state()
    print("Initial State:")
    game.display(state)
    
    while not game.is_terminal(state):
        legal_moves = game.get_legal_moves(state)
        print("Legal Moves:", legal_moves)
        
        # Example move (you can replace this with user input or AI logic)
        move = input("Enter your move (row,col) or 'q' to quit: ")
        if move.lower() == 'q':
          print("Exiting the game...")
          exit()
        try: 
            move = tuple(map(int, move.split(',')))
            if move not in legal_moves:
                print("Invalid move. Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter row,col format.")
            continue
        # Check if the move is valid
        if not game.is_valid_move(state, move):
            print("Invalid move. Try again.")
            continue
        # Make the move
        if move:
            state = game.make_move(state, move, game.current_player)
            print(f"Player {game.current_player} makes move: {move}")
            game.display(state)
            game.current_player = TicTacToe.player2 if game.current_player == TicTacToe.player1 else TicTacToe.player1
        else:
            break
    
    winner = game.get_winner(state)
    if winner:
        print(f"Winner: {winner}")
    else:
        print("It's a draw!")
        
if __name__ == "__main__":
  main()
    


      
