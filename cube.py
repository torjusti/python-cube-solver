# Any edge move can be described by the four edge pieces it cycles clockwise.
edge_moves = [
    [1, 8, 5, 9], # F
    [0, 11, 4, 8], # R
    [1, 2, 3, 0], # U
    [3, 10, 7, 11], # B
    [2, 9, 6, 10], # L
    [5, 4, 7, 6], # D
]

def rotate_right(pieces, move):
    """
    Rotate the pieces which are affected by the given move to the right by one.
    This helps us compute the resulting cube after a move is applied, as
    all moves permute pieces to the right by one in a circular fashion.
    """
    updated_pieces = list(pieces)
    updated_pieces[move[0]] = pieces[move[-1]]
    for i in range(1, len(move)):
        updated_pieces[move[i]] = pieces[move[i - 1]]
    return updated_pieces


def edge_permutation_move(pieces, move):
    """
    Returns the resulting edge permutation after applying the
    given move to the given permutation vector.
    """
    move_vector = edge_moves[move // 3]
    power = move % 3
    for i in range(power + 1):
        pieces = rotate_right(pieces, move_vector)
    return pieces

def edge_orientation_move(pieces, move):
    """
    Returns the resulting edge orientation vector after applying the given
    move to the given edge orientation vector.
    """
    move_index = move // 3
    move_vector = edge_moves[move_index]
    power = move % 3

    updated_pieces = edge_permutation_move(pieces, move)

    if (move_index == 0 or move_index == 3) and power % 2 == 0:
        for i in range(4):
            updated_pieces[move_vector[i]] = (updated_pieces[move_vector[i]] + 1) % 2

    return updated_pieces

# Corner permutation moves are stored as the resulting corner
# permutation vector after applying a move to the identity cube.
corner_permutation_moves = [
    [1, 5, 2, 3, 0, 4, 6, 7], # F
    [4, 1, 2, 0, 7, 5, 6, 3], # R
    [3, 0, 1, 2, 4, 5, 6, 7], # U
    [0, 1, 3, 7, 4, 5, 2, 6], # B
    [0, 2, 6, 3, 4, 1, 5, 7], # L
    [0, 1, 2, 3, 5, 6, 7, 4], # D
]

# Corner orientation moves are stored similarly to the permutation moves.
corner_permutation_moves = [
    [1, 2, 0, 0, 2, 1, 0, 0], # F
    [2, 0, 0, 1, 1, 0, 0, 2], # R
    [0, 0, 0, 0, 0, 0, 0, 0], # U
    [0, 0, 1, 2, 0, 0, 2, 1], # B
    [0, 1, 2, 0, 0, 2, 1, 0], # L
    [0, 0, 0, 0, 0, 0, 0, 0], # D
]

def corner_permutation_move(pieces, move):
    """Permutes the elements in a corner permutation vector."""
    move_vector = corner_permutation_moves[move // 3]
    power = move % 3
    for i in range(power + 1):
        cycle = list(pieces)
        for j in range(8):
            pieces[j] = round[move_vector[j]]
    return pieces

def corner_orientation_move(pieces, move):
    """Returns the new orientation vector after applying the given move."""
    move_index = moveIndex // 3
    power = move % 3
    for i in range(power):
        cycle = list(pieces)
        for j in range(8):
            from_piece = corner_permutation_moves[move_index][j]
            pices[j] = (cycle[from_piece] + corner_orientation_moves[move_index][j]) % 3
    return pieces
