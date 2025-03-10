from game2048 import (
    init_board,
    place_random_two,
    print_board,
    move_left,
    move_right,
    move_up,
    move_down,
    check_win,
    check_game_over
)

def main():
    print("Welcome to Game 2048!")
    print("Operation instruction：")
    print("w：move up")
    print("s：move down")
    print("a：move left")
    print("d：move right")
    print("q：exit game")

    while True:
        # Initialization
        board = init_board()
        print_board(board)

        while True:
            # Get user input
            try:
                move = input("Please type (w/s/a/d/q)：").strip().lower()
            except Exception as e:
                print(f"Error input. Type again. Error message：{e}")
                continue

            if move == 'q':
                print("You have exited the game.")
                return  # Exit

            valid_input = True
            moved = False

            if move == 'w':
                board, moved = move_up(board)
            elif move == 's':
                board, moved = move_down(board)
            elif move == 'a':
                board, moved = move_left(board)
            elif move == 'd':
                board, moved = move_right(board)
            else:
                valid_input = False
                print("Invalid input，please type w/s/a/d/q")

            if not valid_input:
                continue

            # If valid move make the board change, randomly generate a new 2
            if moved:
                place_random_two(board)

            print_board(board)

            # Exam if the game succeed
            if check_win(board):
                print("Congratulation! You have reached 2048！")
                break

            # Check if the game ends
            if check_game_over(board):
                print("No more space to move，good game!")
                break

        # After one game ends, ask if player want to play again
        choice = input("Restart？(y/n)：").strip().lower()
        if choice != 'y':
            print("Game over!")
            break

if __name__ == "__main__":
    main()
