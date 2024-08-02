import re
from pathlib import Path

num_strs = {
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


data_path = Path(__file__).parent.joinpath('input', 'input1.txt')
data = data_path.read_text().split('\n')

cords = []
pattern = r'(one|two|three|four|five|six|seven|eight|nine|ten|\d)'

for input in data:
    matches = []
    pos = 0
    while pos < len(input):
        match = re.search(pattern, input[pos:], re.IGNORECASE)
        if match:
            matches.append(match.group(0))
            pos += match.start() + 1  # move to the next character after the current match starts
        else:
            break

    cords.append(int(str(num_strs.get(matches[0], matches[0])) + str(num_strs.get(matches[-1], matches[-1]))))

print(sum(cords))
# answer #1 54388
# answer #2 53515
