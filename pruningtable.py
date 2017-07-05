import numpy
import math
import itertools
import collections
import numpy

class PruningTable:
    def __init__(self, move_tables, move_table_indexes):
        """Initializes a new pruning table."""
        self.move_table_indexes = move_table_indexes
        self.create_move_table(move_tables)

    def create_move_table(self, move_tables):
        """Creates a new pruning table. A pruning table is an array where each
        index represents the distance from the cube represented by the index
        to one of the solved indexes as represented by the move tables - if
        more than one move table is provided, the distance is that to where
        all move tables are in a solved position. Thus, you can create move
        tables where you check for example for both orientation and permutation
        of the EOLine edge pieces. Balancing the number of move tables in a
        pruning table is difficult, as large pruning tables generate slowly.
        """
        size = numpy.prod([table.get_size() for table in move_tables])
        self.table = [-1 for i in range(math.ceil(size / 2) * 2)]
        powers = numpy.ones(len(move_tables), dtype=numpy.int32)

        for i in range(1, len(move_tables)):
            powers[i] = move_tables[i - 1].move_table.get_size() * powers[i - 1]

        depth = 0
        done = 0

        permutations = itertools.product(table.solved_indexes for table in move_tables)

        for permutation in permutations:
            index = sum(powers[i] * piece for i, piece in enumerate(permutation))
            self.set_value(index, 0)
            done += 1

        while done != size:
            for i in range(size):
                if self.get_value(i) != depth: continue

                for move in range(18):
                    indexes = collections.deque()
                    current_index = i

                    for j in range(len(powers) - 1, -1, -1):
                        indexes.appendleft(move_tables[j].do_move(int(current_index / powers[j]), move))
                        current_index = current_index % powers[j]

                    position = sum(powers[j] * index for j, index in enumerate(indexes))

                    if self.get_value(position) == 0x0f:
                        self.set_value(position, depth + 1)
                        done += 1

            depth += 1

    def set_value(self, index, value):
        """Packs two pruning values into one byte."""
        if (index & 1) == 0:
            self.table[index // 2] &= 0xf0 | value
        else:
            self.table[index // 2] &= 0x0f | (value << 4)

    def get_value(self, index):
        """Unpacks a pruning value from the pruning table."""
        if (index & 1) == 0:
            return self.table[index // 2] & 0x0f
        else:
            return (self.table[index // 2] & 0xf0) >> 4
