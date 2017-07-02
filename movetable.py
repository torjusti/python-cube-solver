import numpy

class MoveTable:
    def __init__(self, size, do_move):
        self.table = numpy.empty((18, size))

        for i in range(size):
            for move in range(18):
                if move not in table[:, i]:
                    result = do_move(i, move)
                    self.table[i, move] = result
                    inverse = move - 2 * (move % 3) + 2
                    self.table[result, inverse] = i

    def do_move(self, index, move):
        return self.table[index, move]

    def get_size():
        return self.table.shape[1]
