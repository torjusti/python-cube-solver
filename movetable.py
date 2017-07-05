import numpy

class MoveTable:
    def __init__(self, size, do_move, default_index, solved_indexes):
        """Initializes a new move table."""
        self.default_index = default_index
        self.solved_indexes = solved_indexes
        self.create_move_table(size, do_move)

    def create_move_table(self, size, do_move):
        """Create a new move table, which is a matrix where the rows are
        moves and the columns are indexes. Each cell in the matrix
        represents the resulting index after applying a move to an index.
        """
        self.table = numpy.full([size, 18], -1, dtype=numpy.int32)

        for i in range(size):
            for move in range(18):
                if self.table[i, move] < 0:
                    result = do_move(i, move)
                    self.table[i, move] = result
                    inverse = move - 2 * (move % 3) + 2
                    self.table[result, inverse] = i

    def do_move(self, index, move):
        """Returns the new index after applying move to index."""
        return self.table[index, move]

    def get_size(self):
        """Returns the number of indexes in the move table."""
        return len(self.table)
