from functools import cached_property
from src.base_solver import BaseSolver


class Day3Solver(BaseSolver):

    def __init__(self, input_path: str):
        super().__init__(input_path)

    def solve_pt1(self):
        """return solution"""

    def solve_pt2(self):
        """return solution"""


if __name__ == "__main__":

    solver = Day3Solver('/Users/ayeager/Code/AOC_2023/src/Day3/input.txt')
    # print('Part 1 solution: ', solver.solve_pt1())
    # print(solver.solve_pt2())