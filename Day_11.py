import numpy as np

with open('inputs/Day_11.txt', 'r') as data:
    lines = [list(line.strip()) for line in data.readlines()]


def distance(gal_1, gal_2, column_widths, row_widths):
    x_min = min(gal_1[1], gal_2[1])
    x_max = max(gal_1[1], gal_2[1])
    y_min = min(gal_1[0], gal_2[0])
    y_max = max(gal_1[0], gal_2[0])

    x_distance = sum(column_widths[x_min: x_max])
    y_distance = sum(row_widths[y_min: y_max])

    return x_distance + y_distance

column_counts = [0]*len(lines[0])
row_counts = [0]*len(lines)
galaxies = []

for row in range(len(lines)):
    for column in range(len(lines[0])):
        if lines[row][column] == '#':
            column_counts[column] += 1
            row_counts[row] += 1
            galaxies.append((row, column))

column_widths = [1 if count > 0 else 2 for count in column_counts]
row_widths = [1 if count > 0 else 2 for count in row_counts]

sum_1=0
for i, gal_1 in enumerate(galaxies[:-1]):
    for gal_2 in galaxies[i+1:]:
        dist = distance(gal_1, gal_2, column_widths, row_widths)
        sum_1 += dist

print(f'Part 1: {sum_1}')  # Answer: 9536038

column_widths = [1 if count > 0 else 1000000 for count in column_counts]
row_widths = [1 if count > 0 else 1000000 for count in row_counts]

sum_2=0
for i, gal_1 in enumerate(galaxies[:-1]):
    for gal_2 in galaxies[i+1:]:
        dist = distance(gal_1, gal_2, column_widths, row_widths)
        sum_2 += dist

print(f'Part 2: {sum_2}')  # Answer: 447744640566