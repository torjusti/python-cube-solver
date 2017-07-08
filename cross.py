from genericsolver import GenericSolver

class CrossSolver(GenericSolver):
    def initialize(self):
        self.add_simple_edge_orientation_table([4, 5, 6, 7]);
        self.add_simple_edge_permutation_table([4, 5, 6, 7]);

solver = CrossSolver()
