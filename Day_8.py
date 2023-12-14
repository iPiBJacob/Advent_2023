import time
import math

with open('inputs/Day_8.txt', 'r') as input:
    lines = [line.strip() for line in input.readlines()]


def find_repeat(start):
    current_place = start
    lr_key_counter = 0
    sequence = [current_place]
    z_indices = []
    while True:
        current_place = sequence[-1]
        lr = left_right_key[left_right[lr_key_counter % key_length]]
        sequence.append(mapping[current_place][lr])
        lr_key_counter += 1

        current_place = sequence[-1]
        if current_place[-1] == 'Z':
            print(sequence)
            z_indices.append(lr_key_counter)
            index_matches = [lr_key_counter % key_length == index % key_length
                                for index in z_indices[:-1]]
            if any(index_matches):
                first_match_index = index_matches.index(True)
                start_index = z_indices[first_match_index]
                start_index = (start_index // key_length) * key_length  # Floor to sync repeat unit
                end_index = z_indices[-1] 
                end_index = (end_index // key_length) * key_length  # Floor to sync repeat unit

                return sequence[start_index : end_index], z_indices, start_index

left_right = lines[0]
left_right_key = {'L': 0, 'R': 1}
key_length = len(left_right)

instructions = lines[2:]
mapping = {}
a_starts = []
for instruction in instructions:
    key, value = [part.strip(' ()') for part in instruction.split('=')]
    if key[-1] == 'A':
        a_starts.append(key)
    value_tup = [val.strip() for val in value.split(',')]
    mapping[key] = value_tup

current_place = 'AAA'
lr_key_counter = 0
while current_place != 'ZZZ':
    lr = left_right_key[left_right[lr_key_counter % key_length]]
    current_place = mapping[current_place][lr]
    lr_key_counter += 1

print(f'Part 1: {lr_key_counter}')  # Answer: 17141

start_indices = []
for start in a_starts:
    repeat_unit, z_indices, start_index = find_repeat(start)
    start_indices.append(start_index)


print(f'Part 2: {math.lcm(*start_indices)})  # Answer 10818234074807
