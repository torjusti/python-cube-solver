from genericsolver import GenericSolver

class EOLineSolver(GenericSolver):
    def initialize(self):
        self.add_simple_edge_orientation_table([i for i in range(12)])
        self.add_simple_edge_permutation_table([5, 7])

solver = EOLineSolver()

print(solver.solve('F R D2'))
