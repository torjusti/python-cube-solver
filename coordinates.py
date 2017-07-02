def index_from_orientation(pieces, flip_count):
    """
    Computes an unique index in the range 0 <= index < the number of possible
    flips. The function is a bijection, but there is no guaranteed logical
    connection between the orientations and their corresponding indexes.
    """
    index = 0
    for i in range(len(pieces) - 1):
        index = flip_count * index + pieces[i]
    return index

def index_from_edge_orientation(edges):
    # Edges may be flipped in 2 ways.
    return get_index_from_orientation(edges, 2)

def index_from_corner_orientation(corners):
    # Corners can be twisted in 3 ways.
    return get_index_from_orientation(corners, 3)

def orientation_from_index(index, num_pieces, num_flips):
    """Returns the original orientation from an index."""
    orientation = []
    parity = 0
    for i in range(num_pieces - 2, -1, -1):
        ori = index % num_fllips
        orientation[i] = ori
        parity += ori
        index //= num_flips
    orientation[-1] = (num_flips - parity % num_flips) % num_flips
    return orientation

def corner_orientation_from_index(index):
    return orientation_from_index(index, 8, 3)

def edge_orientation_from_index(index):
    return orientation_from_index(index, 12, 2)

def index_from_permutation(permutation, affected_pieces):
    """
    This function is a bijection which will map a given permutation to an
    unique number. The range of the number depends on the select pieces
    in the whole permutation which we bother tracking - the number will be an
    unique number in the range 0 <= index <= the number of ways the affected
    pieces may be permuted in a list as big as the given permutation vector.
    The function is identical for both edges and corners.
    """
    indexes = [permutation.index(piece) for piece in affected_pieces]
    base = len(permutation)
    index = indexes[-1]
    for i in range(len(indexes) - 2, -1, -1):
        for j in range(len(indexes) - 1, i, -1):
            if indexes[i] > indexes[j]:
                indexes[i] -= 1
        index += base * indexes[i]
        base *= 1 + len(permutation) - len(indexes) + i
    return index

def permutation_from_index(index, affected_pieces, size):
    """Returns the original permutation from a permutation index."""
    permutation = [-1 for i in range(size)]
    factor = 1 + size - len(affected_pieces)
    base = size
    for i in range(len(affected_pieces) - 1): base *= factor + i

    indexes = []

    for i in range(len(affected_pieces) - 1):
        base /= factor + i
        value = index // base
        index = index % base
        indexes[i] = value

    indexes.append(index)

    for i in range(len(indexes)):
        for j in range(i + 1, len(indexes)):
            if indexes[i] >= indexes[j]:
                indexes[i] += 1

        permutation[indexes[i]] = affected_pieces[i]

    return permutation

def edge_permutation_from_index(index, affected_pieces):
    return permutation_from_index(index, affected_pieces, 12)

def corner_permutation_from_index(index, affected_pieces):
    return permutation_from_index(index, affected_pieces, 8)
