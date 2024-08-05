import re
from functools import cached_property

from src.base_solver import BaseSolver


class Day1Solver(BaseSolver):

    def __init__(self, input_path: str):
        super().__init__(input_path)

    @cached_property
    def num_strs(self) -> dict:
        return {
            'one': 1,
            'two': 2,
            'three': 3,
            'four': 4,
            'five': 5,
            'six': 6,
            'seven': 7,
            'eight': 8,
            'nine': 9,
            'zero': 0,
        }

    def solve_pt1(self):
        """return solution"""
        #  had already modified things in original script for pt 2 before I did this to lazy to do again.
        #  Answer was 54388.  If I ever do want to circle back

    def solve_pt2(self):
        """return solution"""
        cords = []
        pattern = r'(one|two|three|four|five|six|seven|eight|nine|ten|\d)'
        for input in self.input_line_by_line():
            matches = []
            pos = 0
            while pos < len(input):
                match = re.search(pattern, input[pos:], re.IGNORECASE)
                if match:
                    matches.append(match.group(0))
                    pos += match.start() + 1  # move to the next character after the current match starts
                else:
                    break

            cords.append(int(str(self.num_strs.get(matches[0], matches[0])) + str(self.num_strs.get(matches[-1], matches[-1]))))

        return sum(cords)


if __name__ == "__main__":
    solver = Day1Solver('/src/Day1/input.txt')

    # print('Part 1 solution: ', solver.solve_pt1())
    print('Part 2 solution: ', solver.solve_pt2())