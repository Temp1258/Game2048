import random

def init_board():
    """
    Initialize the game board, and return a 4x4 2D list, and generate two number '2' in two random place on board.
    """
    board = [[0 for _ in range(4)] for _ in range(4)]
    # generate two '2' on two random places
    place_random_two(board)
    place_random_two(board)
    return board

def place_random_two(board):
    """
    choose an empty entry on board and place 2 on it
    """
    empty_cells = [(r, c) for r in range(4) for c in range(4) if board[r][c] == 0]
    if not empty_cells:
        return  # do nothing id no empty place
    r, c = random.choice(empty_cells)
    board[r][c] = 2

def print_board(board):
    """
    print current board situation.
    """
    print("-" * 21)
    for row in board:
        row_str = ""
        for num in row:
            if num == 0:
                row_str += "|   "
            else:
                row_str += f"|{num:3}"
        row_str += "|"
        print(row_str)
        print("-" * 21)

def move_left(board):
    """
    move left and combine all the rows
    return new board after a move or combined, and borad values.
    """
    new_board = []
    moved = False

    for row in board:
        # 1. rip 0 (space)
        filtered_row = [num for num in row if num != 0]

        # 2. combine neighbour numbers from left to right
        merged_row = []
        skip = False
        for i in range(len(filtered_row)):
            if skip:
                skip = False
                continue
            if i < len(filtered_row) - 1 and filtered_row[i] == filtered_row[i+1]:
                merged_value = filtered_row[i] * 2
                merged_row.append(merged_value)
                skip = True
            else:
                merged_row.append(filtered_row[i])

        # 3. fill 0 according to length after combining.
        merged_row.extend([0] * (4 - len(merged_row)))

        # 4. exam if there are difference between now and original one
        if merged_row != row:
            moved = True

        new_board.append(merged_row)

    return new_board, moved

def move_right(board):
    """
    move right and combine all the rows.
    """
    # reverse each row, reuse move left and reverse again.
    reversed_board = [row[::-1] for row in board]
    moved_board, moved = move_left(reversed_board)
    restored_board = [row[::-1] for row in moved_board]
    return restored_board, moved

def move_up(board):
    """
    move up and combine all the columns
    """
    # turn columns to rows and use move left to turn back.
    transposed = transpose(board)
    moved_board, moved = move_left(transposed)
    restored_board = transpose(moved_board)
    return restored_board, moved

def move_down(board):
    """
    move down and combine all the columns.
    """
    # turn columns to rows and use move right to turn back.
    transposed = transpose(board)
    moved_board, moved = move_right(transposed)
    restored_board = transpose(moved_board)
    return restored_board, moved

def transpose(board):
    """
    transpose
    """
    return [list(row) for row in zip(*board)]

def check_win(board):
    """
    check if 2048 exist.
    """
    for row in board:
        if 2048 in row:
            return True
    return False

def check_game_over(board):
    """
    check if game is over: no further move allowed.
    """
    # if empty (0) still exist, game continue. not over.
    for row in board:
        if 0 in row:
            return False

    # check if move to four directions allowed (allow if there will be change on board)
    if can_move_left(board) or can_move_right(board) or can_move_up(board) or can_move_down(board):
        return False

    return True

def can_move_left(board):
    """
    check if numbers can move left
    """
    temp_board, moved = move_left(board)
    return moved

def can_move_right(board):
    """
    check if numbers can move right
    """
    temp_board, moved = move_right(board)
    return moved

def can_move_up(board):
    """
    check if numbers can move up
    """
    temp_board, moved = move_up(board)
    return moved

def can_move_down(board):
    """
    check if numbers can move down
    """
    temp_board, moved = move_down(board)
    return moved
