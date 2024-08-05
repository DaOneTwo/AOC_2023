from functools import cached_property
import re

from src.base_solver import BaseSolver


class Day3Solver(BaseSolver):

    def __init__(self, input_path: str):
        super().__init__(input_path)
        self.row_count = 140

    def solve_pt1(self):
        """return solution"""
        lines = self.input_all_lines()

        rows = len(lines)
        cols = len(lines[0].strip())

        # # Convert lines to a grid
        # grid = [list(line.strip()) for line in lines]
        #
        # symbols = set(['$', '*', '+', '=', '-', '&', '@', '#', '/', '%'])
        #
        # def is_adjacent_to_symbol(r, c):
        #     for dr in range(-1, 2):
        #         for dc in range(-1, 2):
        #             nr, nc = r + dr, c + dc
        #             if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] in symbols:
        #                 return True
        #     return False
        #
        # part_sum = 0
        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c].isdigit():
        #             num_str = grid[r][c]
        #             # Check for multi-digit numbers
        #             while c + 1 < cols and grid[r][c + 1].isdigit():
        #                 c += 1
        #                 num_str += grid[r][c]
        #             if is_adjacent_to_symbol(r, c):
        #                 part_sum += int(num_str)
        #
        # return part_sum
        # # regex numbers from row
        # # for each c-index (ci) of a numbers position is symbol
        # # Ri = : C+1, C-1
        # # Ri - 1 : C, C+1, C-1
        # # R+1 : C, C+1, C-1
        # # add number

    def solve_pt2(self):
        """return solution"""


if __name__ == "__main__":

    solver = Day3Solver('/Users/ayeager/Code/AOC_2023/src/Day3/input.txt')
    print('printPart 1 solution: ', solver.solve_pt1())
    # print(solver.solve_pt2())