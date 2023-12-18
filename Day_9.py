with open('inputs/Day_9.txt', 'r') as input:
    lines = [line.strip() for line in input.readlines()]

def find_delta(input_list):
    #print(input_list)
    diffs = []
    for i in range(1, len(input_list)):
        diffs.append(input_list[i] - input_list[i-1])

    if all([diff == 0 for diff in diffs]):
        return 0  # Add a zero to list, then pass up

    return diffs[-1] + find_delta(diffs)


sum_1 = 0
sum_2 = 0
for line in lines:
    line = [int(val) for val in line.split()]
    sum_1 += line[-1] + find_delta(line)
    sum_2 += line[0] + find_delta(list(reversed(line)))

print(f'Part 1: {sum_1}')  # Answer: 1806615041
print(f'Part 2: {sum_2}')  # Answer: 1211