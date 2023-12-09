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
for input in data:
    nums = re.findall(r'\d', input.lower())
    i = int(f'{nums[0] if nums[0].isdigit() else num_strs[nums[0]]}{nums[-1]}')
    cords.append(i)



print(sum(cords))
# answer 54388
