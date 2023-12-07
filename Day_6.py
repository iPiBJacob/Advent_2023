import numpy as np

with open('inputs/Day_6.txt', 'r') as input:
    lines = [line.strip() for line in input.readlines()]

def quadratic(a, b, c):
    determinant = (b**2 - 4*a*c)**(1/2)
    return [(-b + determinant) / (2*a), (-b - determinant) / (2*a)]

times = lines[0].split()[1:]
distances = lines[1].split()[1:]

win_options = []
for time, distance in zip(times, distances):
    roots = quadratic(-1, int(time), -(int(distance) + 0.0001))  
    # Add small value since we want to win, not tie
    win_options.append(np.floor(max(roots)) - np.ceil(min(roots)) + 1)

print(win_options)
print(f'Part 1: {np.prod(win_options)}')

time = int(''.join(times))
distance = int(''.join(distances))
roots = quadratic(-1, time, -distance - 0.0001)
win_options = (np.floor(max(roots)) - np.ceil(min(roots)) + 1)
print(f'Part 2: {win_options}')
