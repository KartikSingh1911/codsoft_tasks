"""
TASK 2: TIC-TAC-TOE AI USING MINIMAX

Human plays X. Computer plays O. The Minimax algorithm evaluates possible
moves and chooses an optimal move. No external packages needed.
"""

HUMAN = "X"
AI = "O"
EMPTY = " "


def print_board(board):
    """Display the board with cell numbers for empty positions."""
    display = [
        str(i + 1) if board[i] == EMPTY else board[i]
        for i in range(9)
    ]
    print()
    print(f" {display[0]} | {display[1]} | {display[2]} ")
    print("---+---+---")
    print(f" {display[3]} | {display[4]} | {display[5]} ")
    print("---+---+---")
    print(f" {display[6]} | {display[7]} | {display[8]} ")
    print()


def get_winner(board):
    """Return X or O if there is a winner; otherwise return None."""
    winning_lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in winning_lines:
        if board[a] == board[b] == board[c] and board[a] != EMPTY:
            return board[a]
    return None


def is_draw(board):
    return get_winner(board) is None and EMPTY not in board


def minimax(board, depth, is_maximizing):
    """
    Score the current position:
      +1: AI wins
      -1: human wins
       0: draw

    Depth is used to prefer quicker wins and slower losses.
    """
    winner = get_winner(board)

    if winner == AI:
        return 10 - depth
    if winner == HUMAN:
        return depth - 10
    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = float("-inf")
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = AI
                score = minimax(board, depth + 1, False)
                board[i] = EMPTY
                best_score = max(best_score, score)
        return best_score

    best_score = float("inf")
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = HUMAN
            score = minimax(board, depth + 1, True)
            board[i] = EMPTY
            best_score = min(best_score, score)
    return best_score


def find_best_move(board):
    """Find and return the best available cell index for the AI."""
    best_score = float("-inf")
    best_move = None

    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI
            score = minimax(board, 0, False)
            board[i] = EMPTY

            if score > best_score:
                best_score = score
                best_move = i

    return best_move


def get_human_move(board):
    """Read and validate the human player's move."""
    while True:
        choice = input("Choose an empty cell (1-9): ").strip()

        if not choice.isdigit() or not 1 <= int(choice) <= 9:
            print("Please enter a number from 1 to 9.")
            continue

        index = int(choice) - 1
        if board[index] != EMPTY:
            print("That cell is already occupied. Choose another one.")
            continue

        return index


def play_game():
    board = [EMPTY] * 9

    print("=" * 42)
    print("             TIC-TAC-TOE AI")
    print("=" * 42)
    print("You are X. The computer is O.")
    print("Enter a cell number to make your move.")

    while True:
        print_board(board)

        # Human turn
        human_move = get_human_move(board)
        board[human_move] = HUMAN

        if get_winner(board) == HUMAN:
            print_board(board)
            print("Congratulations! You won.")
            break
        if is_draw(board):
            print_board(board)
            print("The game is a draw.")
            break

        # AI turn
        print("Computer is thinking...")
        ai_move = find_best_move(board)
        if ai_move is not None:
            board[ai_move] = AI

        if get_winner(board) == AI:
            print_board(board)
            print("Computer wins! Better luck next time.")
            break
        if is_draw(board):
            print_board(board)
            print("The game is a draw.")
            break


if __name__ == "__main__":
    try:
        play_game()
    except (EOFError, KeyboardInterrupt):
        print("\nGame ended. Thanks for playing!")
