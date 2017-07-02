import numpy
import math
import itertools
import collections

class PruningTable:
    def __init__(self, move_tables):
        size = numpy.prod([table.get_size() for table in move_tables])
        self.table = numpy.full((1, math.ceil(size / 2) * 2), -1)
        powers = numpy.ones([len(move_tables)])

        for i in range(1, len(move_tables)):
            powers[i] = move_tables[i - 1].move_table.get_size() * powers[i - 1]

        depth = 0
        done = 0

        permutations = itertools.product(lambda table: table.solved_indexes, move_tables)

        for permutation in permutations:
            index = sum(powers[i] * piece for i, piece in enumerate(permutation))
            self.set_value(index, 0)
            done += 1

        while done != size:
            for i in range(size):
                if self.get_value(index) != depth: continue

                for move in range(18):
                    indexes = collections.deque()
                    current_index = i

                    for j in range(len(powers) - 1, 0, -1):
                        indexes.appendleft(move_tables[j].move_table.do_move(current_index // powers[j], move))
                        current_index = current_index % powers[j]

                    position = sum(powers[i] * index for i, index in enumerate(indexes))

                    if self.get_value(position) == 0x0f:
                        self.set_value(position, depth + 1)
                        done += 1

            depth += 1

    def set_value(self, index, value):
        if (index & 1) == 0:
            self.table[index // 2] &= 0xf0 | value
        else:
            self.table[index // 2] &= 0xf0 | (value << 4)

    def get_value(self, index):
        if (index & 1) == 0:
            return self.table[index // 2] & 0x0f
        else:
            return (self.table[index // 2] & 0xf0) >> 4