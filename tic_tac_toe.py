import random
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None
def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True
def get_empty_cells(board):
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                empty_cells.append((i, j))
    return empty_cells
def minimax(board, depth, maximizing_player):
    winner = check_winner(board)
    if winner == 'X':
        return -10 + depth
    elif winner == 'O':
        return 10 - depth
    elif is_board_full(board):
        return 0
    if maximizing_player:
        max_eval = float('-inf')
        for move in get_empty_cells(board):
            board[move[0]][move[1]] = 'O'
            eval = minimax(board, depth + 1, False)
            board[move[0]][move[1]] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in get_empty_cells(board):
            board[move[0]][move[1]] = 'X'
            eval = minimax(board, depth + 1, True)
            board[move[0]][move[1]] = ' '
            min_eval = min(min_eval, eval)
        return min_eval
def get_best_move(board):
    best_move = None
    best_eval = float('-inf')
    for move in get_empty_cells(board):
        board[move[0]][move[1]] = 'O'
        eval = minimax(board, 0, False)
        board[move[0]][move[1]] = ' '
        if eval > best_eval:
            best_eval = eval
            best_move = move
    return best_move
def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    while True:
        if player == 'X':
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            if board[row][col] != ' ':
                print("That cell is already taken. Try again.")
                continue
            board[row][col] = player
        else:
            row, col = get_best_move(board)
            board[row][col] = player
            print(f"AI plays at row {row}, column {col}")
        print_board(board)
        winner = check_winner(board)
        if winner:
            print(f"{winner} wins!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

        player = 'O' if player == 'X' else 'X'
if __name__ == "__main__":
    main()
