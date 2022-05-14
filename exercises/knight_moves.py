# Use DFS to find the shortest path between two squares on a chessboard using
# only the movement allowed of a knight

# Structure of search maintained in frames of recursion, no actual tree produced

# Use structural recursion to add each square in a found path to a list and return it

# Use a 'height' variable to explore all possibilities at a certain amount of
# moves, then add to it when all those possibilities are explored (same as the
# 'return all nodes at height h' method from tree.py)

# define a chessboard
chessboard = []
[[chessboard.append((x, y)) for x in range(8)] for y in range(8)]

# define legal moves for a knight
knight_moves = []
for x in (-2, -1, 1, 2):
    for y in (-2, -1, 1, 2):
        if abs(x) != abs(y):
            knight_moves.append((x, y))

# check legal moves for a position on the chessboard
def legal_moves(pos):
    # add knight moves to position
    potential_moves = [(pos[0] + move[0], pos[1] + move[1]) for move in knight_moves]
    # remove results that are not on a chessboard
    return [move for move in potential_moves if move in chessboard]


def shortest(start, end):
    def helper(pos, goal, moves):
        """Recursively explore all combinations of length move. Return the list
        of moves if a path to goal is found, else None."""
        assert (
            moves >= 0 and type(moves) == int
        ), "moves must be a positive integer or 0"
        if moves == 0:  # base case
            return pos if pos == goal else None
        else:  # recursive case: moves > 0
            # make a list of all legal moves
            pass
            # if goal in list, return [goal]
            # else return None
            # return recursive call with moves - 1

        # moves = 0
        # while type (return value of helper) is None:
        pass


def draw_board(list_of_pos):
    draw = ""
    for x in range(8):
        for y in range(8):
            if (x, y) in list_of_pos:
                draw += "x "
            else:
                draw += ". "
        draw += "\n"
    return draw
