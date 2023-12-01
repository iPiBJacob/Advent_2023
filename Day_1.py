import re

with open('inputs/Day_1.txt', 'r') as input:
    lines = [line.strip() for line in input.readlines()]

sum_1 = 0

for line in lines:
    first = re.search('[0-9]', line).group()  # First digit in line
    last = re.search('[0-9]', line[::-1]).group()  # Last digit in line
    sum_1 += int(f'{first}{last}')

print(f'part 1: {sum_1}')  # Answer: 55208

key = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
       'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
key_regex = '|'.join(list(key.keys()))  # All digits and digit words as regex options
reverse_key_regex = '|'.join([val[::-1] for val in key.keys()])  # All digits and reversed digit words as regex options

sum_2 = 0

for line in lines:
    first = re.search(key_regex, line).group()
    last = re.search(reverse_key_regex, line[::-1]).group()
    sum_2 += int(f'{key[first]}{key[last[::-1]]}')

print(f'part 2: {sum_2}')  # Answer: 54578