import cube
import coordinates

def edge_orientation_move(index, move):
    """Returns the updated orientation index after applying move to index."""
    orientation = coordinates.edge_orientation_from_index(index)
    orientation = cube.edge_orientation_move(orientation, move)
    return coordinates.index_from_edge_orientation(orientation)

def edge_permutation_move(index, move, affected_pieces):
    """Returns the updated permutation index after applying move to index."""
    permutation = coordinates.edge_permutation_from_index(index, affected_pieces)
    permutation = cube.edge_permutation_move(permutation, move)
    return coordinates.index_from_permutation(permutation, affected_pieces)

def corner_orientation_move(index, move):
    """Returns the updated orientation index after applying move to index."""
    orientation = coordinates.corner_orientation_from_index(index)
    orientation = cube.corner_orientation_move(orientation, move)
    return coordinates.index_from_corner_orientation(orientation)

def corner_permutation_move(index, move, affected_pieces):
    """Returns the updated permutation index after applying move to index."""
    permutation = coordinates.corner_permutation_from_index(index, affected_pieces)
    permutation = cube.corner_permutation_move(permutation, move)
    return coordinates.index_from_permutation(permutation, affected_pieces)
