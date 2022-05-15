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
    """Returns a list of all legal moves for a knight on a chessboard from pos"""
    assert pos in chessboard, "only positions on a chessboard allowed"
    # add knight moves to position
    potential_moves = [(pos[0] + move[0], pos[1] + move[1]) for move in knight_moves]
    # remove results that are not on a chessboard
    return [move for move in potential_moves if move in chessboard]


def shortest(start, end):
    """Test all move combinations in increasing order of length to find the
    shortest path between start and end using only the moves available to a
    knight on a chessboard. Returns a list of all possible paths of the
    shortest length."""
    assert (
        start in chessboard and end in chessboard
    ), "shortest only accepts legal squares on a chessboard"

    def helper(pos, goal, m):
        """Generator that recursively explores all possible combinations of
        moves a knight on a chessboard can take to reach the goal square from
        the current square (pos). Yield the list of moves if a path to goal is
        found."""
        assert m >= 0 and type(m) == int, "m must be a positive integer or 0"
        if m == 0:  # base case
            if pos == goal:
                yield [pos]
        else:  # recursive case: moves > 0
            # make a list of all legal moves from pos and search their trees
            # for a solution
            to_check = legal_moves(pos)
            for c in to_check:
                next_level_gen = helper(c, goal, m - 1)
                yield from [[pos] + result for result in list(next_level_gen)]

    m = 0
    results = None
    while not results:
        # combine all results of legal combinations of moves of length m
        # if any are found, stop the search and return the list of legal combinations
        results = list(helper(start, end, m))
        m += 1
    return results


def draw_board(list_of_pos):
    """Returns a string of a simple representation of a chessboard. Accepts
    a list of position coordinates and includes them on the board with their
    index number in the list."""
    draw = ""
    for x in range(8):
        for y in range(8):
            if (x, y) in list_of_pos:
                draw += str(list_of_pos.index((x, y))) + " "
            else:
                draw += ". "
        draw += "\n"
    return draw
