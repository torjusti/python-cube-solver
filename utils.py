from coordinates import edge_orientation_from_index, corner_orientation_from_index
import numpy

def get_correct_edge_orientations(size, pieces):
    """Returns all the indexes in the given size where all pieces
    have their edge orientation solved.
    """
    indexes = []
    for i in range(size):
        flips = edge_orientation_from_index(i)
        if all(flips[piece] == 0 for piece in flips):
            indexes.push(i)
    return indexes

def get_correct_corner_orientations(size, pieces):
    """Returns all the indexes in the given size where all pieces
    have their corner orientation solved.
    """
    indexes = []
    for i in range(size):
        twists = corner_orientation_from_index(i)
        if all(twists[piece] == 0 for piece in twists):
            indexes.push(i)
    return indexes
