from functools import cached_property
from src.base_solver import BaseSolver


class Day2Solver(BaseSolver):

    def __init__(self, input_path: str):
        super().__init__(input_path)

    @cached_property
    def color_maxes(self) -> dict:
        return {
            'red': 12,
            'green': 13,
            'blue': 14,
        }

    def solve_pt1(self):
        """return solution"""
        possible_games = []
        for game in self.input_line_by_line():
            game_info, game_data = game.split(":")
            game_number = int(''.join([i for i in game_info if i.isdigit()]))
            sample_sets = game_data.split(';')

            for sample_set in sample_sets:
                samples = sample_set.split(',')

                is_possible = True
                for sample in samples:
                    count, color = sample.strip().split(' ')
                    if int(count) > self.color_maxes[color]:
                        is_possible = False
                        break

                if is_possible is False:
                    break

            if is_possible is True:
                possible_games.append(game_number)

        return sum(possible_games)

    def solve_pt2(self):
        game_multiples = []
        for game in self.input_line_by_line():
            # each game gets min of each color multiplied together
            _, game_data = game.split(":")
            sample_sets = game_data.split(';')
            sample_data = {
                'green': set(),
                'red': set(),
                'blue': set(),
            }
            for sample_set in sample_sets:
                for sample in sample_set.split(','):
                    count, color = sample.strip().split(' ')
                    sample_data[color].add(int(count))

            max_green, max_red, max_blue = max(sample_data['green']), max(sample_data['red']), max(sample_data['blue'])
            power = max_green * max_red * max_blue

            game_multiples.append(power)

        return sum(game_multiples)


if __name__ == "__main__":

    solver = Day2Solver('/src/Day2/input.txt')
    # print('Part 1 solution: ', solver.solve_pt1())
    # print(solver.solve_pt2())