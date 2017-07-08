from genericsolver import GenericSolver

class FirstBlockSolver(GenericSolver):
    def initialize(self):
        eo_moves = self.add_simple_edge_orientation_table([6, 9, 10], pruning_table=False)
        co_moves = self.add_simple_corner_orientation_table([5, 6], pruning_table=False)
        ep_moves = self.add_simple_edge_permutation_table([6, 9, 10], pruning_table=False)
        cp_moves = self.add_simple_corner_permutation_table([5, 6], pruning_table=False)

        self.add_pruning_table([eo_moves, cp_moves])
        self.add_pruning_table([co_moves, cp_moves])
        self.add_pruning_table([ep_moves, cp_moves])

solver = FirstBlockSolver()

print(solver.solve('F'))
