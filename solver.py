import math
from pruningtable import PruningTable
from movetable import MoveTable
from coordinates import index_from_permutation
from moves import *
from scrambles import *
from utils import *
import numpy

class Solver:
    move_tables = []
    pruning_tables = []
    initialized = False

    def add_pruning_table(self, move_table_indexes):
        print('Adding a pruning table')
        move_table_indexes = [b for a, b in sorted(zip(self.move_tables,
            move_table_indexes), key=lambda data: data[0]['move_table'].get_size())]

        pruning_table = PruningTable([self.move_tables[i] for i in move_table_indexes])

        self.pruning_tables.append({
            'table': pruning_table,
            'move_table_indexes': move_table_indexes,
        })

    def add_table(self, settings, pruning_table=True):
        print('Adding a move table')
        solved_indexes = settings.get('solved_indexes', settings['default_index'])

        move_table = MoveTable(settings['size'], settings['do_move'])

        self.move_tables.append({
            'move_table': move_table,
            'default_index': settings['default_index'],
            'solved_indexes': solved_indexes,
        })

        if not pruning_table: return len(self.move_tables) - 1

        self.add_pruning_table([len(self.move_tables) - 1])

    def add_simple_edge_orientation_table(self, pieces, pruning_table=True):
        self.add_table({
            'size': 2 ** 11,
            'do_move': edge_orientation_move,
            'default_index': 0,
            'solved_indexes': 0 if len(pieces) == 12 else get_correct_edge_orientations(2 ** 11, pieces),
        }, pruning_table)

    def add_simple_corner_permutation_table(self, pieces, pruning_table=True):
        self.add_table({
            'size': 3 ** 7,
            'do_move': corner_orientation_move,
            'default_index': 0,
            'solved_indexes': 0 if len(pieces) == 8 else get_correct_corner_orientations(3 ** 7, pieces),
        }, pruning_table)

    def add_simple_edge_permutation_table(self, pieces, pruning_table=True):
        self.add_table({
            'size': math.factorial(12) // math.factorial(12 - len(pieces)),
            'do_move': lambda index, move: edge_permutation_move(index, move, pieces),
            'default_index': index_from_permutation([i for i in range(12)], pieces),
        }, pruning_table)

    def add_simple_corner_permutation_table(self, pieces, pruning_table=True):
        self.add_table({
            'size': math.factorial(8) // math.factorial(8 - len(pieces)),
            'do_move': lambda index, move: corner_permutation_move(index, move, pieces),
            'default_index': index_from_permutation([i for i in range(8)], pieces),
        }, pruning_table)

    def search(self, indexes, depth, last_move, solution):
        maximum_distance = 0

        for pruning_table in self.pruning_tables:
            powers = [1]

            for i in range(1, len(pruning_table['move_table_indexes'])):
                powers.append(self.move_tables[pruning_table.move_table_indexes[i - 1]].move_table.get_size() * powers[i - 1])

            index = sum(indexes[table_index] * powers[i] for i, table_index in enumerate(pruning_table['move_table_indexes']))

            distance = pruning_table['table'].get_value(index)

            if distance > depth: return False

            maximum_distance = max(distance, maximum_distance)

        if maximum_distance == 0: return True

        for move in range(6):
            if move != last_move and move != last_move - 3:
                for power in range(3):
                    updated_indexes = [self.move_tables[i]['move_table'].do_move(indexes[i], move * 3 + power) for i in range(len(indexes))]
                    result = self.search(updated_indexes, depth - 1, move, solution)

                    if result:
                        solution.append(move * 3 + power)
                        return True

        return False

    def solve(self, scramble):
        if not self.initialized:
            self.initialize()
            self.initialized = True

        print('initialized..')
        moves = parse_scramble(scramble)

        indexes = [move_table['default_index'] for move_table in self.move_tables]

        for move in moves:
            for i in range(len(indexes)):
                indexes[i] = self.move_tables[i]['move_table'].do_move(indexes[i], move)

        solution = []

        for depth in range(20):
            if self.search(indexes, depth, -1, solution):
                 break

        solution.reverse()

        return format_move_sequence(solution)
