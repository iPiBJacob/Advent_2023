import numpy as np

with open('inputs/Day_10.txt', 'r') as data:
    lines = [list(line.strip()) for line in data.readlines()]

layout = np.array(lines)
start_y, start_x = [coord[0] for coord in np.where(layout == 'S')]

rdlu = ['right', 'down', 'left', 'up']

vectors = {'right': np.array([0,1]),
           'down': np.array([1,0]),
           'left': np.array([0,-1]),
           'up': np.array([-1,0])}

inputs = {'right': ('-', 'J', '7', 'S'),
          'down': ('J', '|', 'L', 'S'),
          'left': ('-', 'F', 'L', 'S'),
          'up': ('|', 'F', '7', 'S')}

connections = {'-': ('left', 'right'),
               '|': ('up', 'down'),
               '7': ('left', 'down'),
               'F': ('down', 'right'),
               'L': ('up', 'right'),
               'J': ('left', 'up'),
               'S': ('right', 'down', 'left', 'up')}

def navigate(layout, start_tuple):
    path = [start_tuple]
    current_place = start_tuple
    #  Iterate until start found again
    while current_place != start_tuple or len(path) == 1:
        current_value = layout[current_place[0], current_place[1]]
        for direction in rdlu:
            if direction not in connections[current_value]:
                continue  # Only accept allowed directions

            vector = vectors[direction]
            check = tuple(np.array(current_place) + vector)

            if any(check >= np.array(np.shape(layout))):
                continue  # Index out of array

            check_value = layout[check[0], check[1]]
            # Exclude all useless cases first
            if check_value == 'S' and len(path) < 3:
                continue  # Just seeing the start again
            if check in path and check_value != 'S':
                continue  # No backtracking 
            if check_value == '.':
                continue  # Don't check if no pipe
            if check_value not in inputs[direction]:
                continue  # Pipe present but not connected
            
            # If here, pipe is connected
            path.append(check)
            current_place = check
            break

    return path

def adjacent_vals(layout, location):
    loc_y, loc_x = location
    left = layout[loc_y, loc_x - 1]
    right = layout[loc_y, loc_x + 1]
    up = layout[loc_y - 1, loc_x]
    down = layout[loc_y + 1, loc_x]
    return (left, right, up, down)


start_tuple = (start_y, start_x)
loop = navigate(layout, start_tuple)
print(f'Part 1: {len(loop[1:]) / 2}')  # Answer: 6979

# Part 2
for location in loop:  # Label all pipe parts
    layout[location[0], location[1]] = 'P'

# Temporarily label all non-loop positions as inside
layout[layout != 'P'] = 'I'

max_y, max_x = np.shape(layout,)

big_layout = np.empty((max_y * 2, max_x * 2), dtype=str)

# Space out all values
for y in range(max_y):
    for x in range(max_x):
        big_layout[y * 2, x * 2] = layout[y, x]

# Block all obstructed paths
for i in range(len(loop)):
    here = loop[i]
    next = loop[(i+1) % len(loop)]      
    diff = np.array(next) - np.array(here)
    connection = list(2 * np.array(here) + diff)
    big_layout[connection[0], connection[1]] = 'P' 

big_layout[big_layout != 'P'] = 'I'
max_y, max_x = np.shape(big_layout)

# Do edges first
for i in range(max_y):
    if big_layout[i, 0] == 'I':
        big_layout[i, 0] = 'O'
    if big_layout[i, max_x - 1] == 'I':
        big_layout[i, max_x - 1] = 'O'

for i in range(max_x):
    if big_layout[0, i] == 'I':
        big_layout[0, i] = 'O'
    if big_layout[max_y - 1, i] == 'I':
        big_layout[max_y - 1, i] = 'O'


just_changed = True
while just_changed:
    i_count = np.count_nonzero(big_layout == 'I')
    #print(f'number of I: {i_count}')
    just_changed = False
    i_locs = np.argwhere(big_layout == 'I')
    for i_loc in i_locs:
        neighbors = adjacent_vals(big_layout, i_loc)
        if 'O' in neighbors:
            big_layout[i_loc[0], i_loc[1]] = 'O'
            just_changed = True

# Space out all values
for y in range(0, max_y, 2):
    for x in range(0, max_x, 2):
        layout[int(y // 2), int(x // 2)] = big_layout[y, x]

inside = (layout == 'I').sum()
print(f'Part 2: {inside}')  # Answer: 443
