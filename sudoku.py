import random

def generate_sudoku():
    board = [[0 for _ in range(9)] for _ in range(9)]
    fill_board(board)
    return board

def fill_board(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                numbers = list(range(1, 10))
                random.shuffle(numbers)
                for num in numbers:
                    if is_valid(board, i, j, num):
                        board[i][j] = num
                        if fill_board(board):
                            return True
                        board[i][j] = 0
                return False
    return True

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def hide_cells(board, difficulty):
    num_to_hide = 0
    if difficulty == 'easy':
        num_to_hide = 30
    elif difficulty == 'medium':
        num_to_hide = 45
    elif difficulty == 'hard':
        num_to_hide = 60
    else:
        print("Invalid difficulty level. Using default difficulty (medium).")
        num_to_hide = 45
    
    cells = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(cells)
    for _ in range(num_to_hide):
        row, col = cells.pop()
        board[row][col] = 0

def print_board(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                print("_", end=" ")
            else:
                print(board[i][j], end=" ")
            if j == 2 or j == 5:
                print("|", end=" ")
        print()
        if i == 2 or i == 5:
            print("-" * 21)

def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True
    row, col = empty_cell
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False

def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None
    
def print_board_with_options(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            if board[i][j] == 0:
                print("_", end=" ")
            else:
                print(board[i][j], end=" ")
        print()

def is_valid_move(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def add_solution(board, row, col, num):
    if is_valid_move(board, row, col, num):
        board[row][col] = num
        return True
    else:
        return False

def complete_board(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True
    row, col = empty_cell
    for num in range(1, 10):
        if is_valid_move(board, row, col, num):
            board[row][col] = num
            if complete_board(board):
                return True
            board[row][col] = 0
    return False

def print_board_with_options(board, reveal=False):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            if reveal or board[i][j] != 0:
                print(board[i][j], end=" ")
            else:
                print("_", end=" ")
        print()

# Play Sudoku
print("Welcome to Sudoku!")

# Generate a solvable Sudoku board
board = generate_sudoku()

# Hide cells
hide_cells(board, 'medium')

# Print the initial board with hidden cells
print("Generated Sudoku board:")
print_board_with_options(board)

while True:
    choice = input("Enter 's' to solve manually, 'a' to get answers, or 'q' to quit: ").lower()
    if choice == 's':
        row = int(input("Enter row (1-9): ")) - 1
        col = int(input("Enter column (1-9): ")) - 1
        num = int(input("Enter number (1-9): "))
        if 0 <= row < 9 and 0 <= col < 9 and 1 <= num <= 9:
            if add_solution(board, row, col, num):
                print("Number added successfully!")
                print_board_with_options(board)
            else:
                print("Invalid move! Try again.")
        else:
            print("Invalid input! Please enter numbers within the range 1-9.")
    elif choice == 'a':
        print("Sudoku solution:")
        solve_sudoku(board)
        print_board_with_options(board, reveal=True)
        break
    elif choice == 'q':
        print("Thanks for playing Sudoku!")
        break
    else:
        print("Invalid choice! Please enter 's', 'a', or 'q'.")
