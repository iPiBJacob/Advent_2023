with open('inputs/Day_2.txt', 'r') as input:
    lines = [line.strip() for line in input.readlines()]


red_total, green_total, blue_total = 12, 13, 14
sum_1 = 0
for line in lines:
    legal = True
    game_num, draw_sets = line.split(': ')
    game_num = int(game_num[5:])
    draw_sets = draw_sets.split('; ')
    for draw_set in draw_sets:
        colors = draw_set.split(', ')
        for color in colors:
            if 'red' in color and int(color.split(' ')[0]) > red_total:
                legal = False
            if 'blue' in color and int(color.split(' ')[0]) > blue_total:
                legal = False
            if 'green' in color and int(color.split(' ')[0]) > green_total:
                legal = False
    if legal:
        sum_1 += game_num

print(f'part 1: {sum_1}')  # Answer: 2169

sum_2 = 0
for line in lines:
    red_min, green_min, blue_min = 0, 0, 0
    draw_sets = line.split(': ')[-1]
    draw_sets = draw_sets.split('; ')
    for draw_set in draw_sets:
        colors = draw_set.split(', ')
        for color in colors:
            if 'red' in color and int(color.split(' ')[0]) > red_min:
                red_min = int(color.split(' ')[0])
            if 'blue' in color and int(color.split(' ')[0]) > blue_min:
                blue_min = int(color.split(' ')[0])
            if 'green' in color and int(color.split(' ')[0]) > green_min:
                green_min = int(color.split(' ')[0])
    sum_2 += red_min * green_min * blue_min

print(f'part 2: {sum_2}')  # Answer: 60948