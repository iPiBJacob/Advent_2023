import re

with open('inputs/Day_3.txt', 'r') as input:
    lines = [line.strip() for line in input.readlines()]

def check_touching(span, index):
    span_range = range(span[0]-1, span[-1]+1)
    return index in span_range

number_regex = '[0-9]+'
symbol_regex = '\+|-|&|%|@|/|\$|#|\*|='


sum_1 = 0
for i, line in enumerate(lines):
    numbers = re.finditer(number_regex, line)

    for number in numbers:
        number_span = number.span()

        # Check previous line for touching symbols
        if i > 0:
            prev_line = lines[i-1]
            prev_symbols = re.finditer(symbol_regex, prev_line)
            if any([check_touching(number_span, symbol.start()) for symbol in prev_symbols]):
                sum_1 += int(number.group())
                continue

        # Check same line for touching symbols
        same_symbols = re.finditer(symbol_regex, line)
        if any([check_touching(number_span, symbol.start()) for symbol in same_symbols]):
            sum_1 += int(number.group())
            continue

        # Check next line for touching symbols
        if i < len(lines) -1:
            next_line = lines[i+1]
            next_symbols = re.finditer(symbol_regex, next_line)
            if any([check_touching(number_span, symbol.start()) for symbol in next_symbols]):
                sum_1 += int(number.group())
                continue

print(f'part 1: {sum_1}')  # Answer: 536576

sum_2 = 0
for i, line in enumerate(lines):
    symbols = re.finditer(symbol_regex, line)
    

    for symbol in symbols:
        gear_partners = []
        symbol_index = symbol.start()

        # Check previous line for touching numbers
        if i > 0:
            prev_line = lines[i-1]
            prev_numbers = re.finditer(number_regex, prev_line)
            for number in prev_numbers:
                if check_touching(number.span(), symbol_index):
                    gear_partners.append(int(number.group()))

        # Check same line for touching numbers
        same_numbers = re.finditer(number_regex, line)
        for number in same_numbers:
            if check_touching(number.span(), symbol_index):
                gear_partners.append(int(number.group()))

        # Check next line for touching numbers
        if i < len(lines) -1:
            next_line = lines[i+1]
            next_numbers = re.finditer(number_regex, next_line)
            for number in next_numbers:
                if check_touching(number.span(), symbol_index):
                    gear_partners.append(int(number.group()))
        
        if len(gear_partners) == 2:
            sum_2 += gear_partners[0] * gear_partners[1]

print(f'part 2: {sum_2}')  # Answer: 75741499