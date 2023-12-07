with open('inputs/Day_5.txt', 'r') as input:
    lines = [line.strip() for line in input.readlines()]

def flatten(container):  # Extract all values from an arbitrarily nested list
    for i in container:
        if isinstance(i, (list,tuple)):
            for j in flatten(i):
                yield j
        else:
            yield i

def convert_seed(seed, spans):
    for span in spans:  # Check if seed is in any spans
        if seed >= span[1] and seed < span[1] + span[2]:
            diff = seed - span[1]  # Calculate difference to add to destination
            return span[0] + diff  # Return mapped seed coordinate
    return seed  # If no matches, return original value

def convert_range(seed_range, spans):
    span_breakpoints = []
    output_ranges = [seed_range]
    for span in spans:  # Add start and end of every span to list
        span_breakpoints.append(span[1])
        span_breakpoints.append(span[1] + span[2])
    span_breakpoints.append(seed_range[0])  # Add seed range start
    span_breakpoints.append(seed_range[1])  # Add seed range end
    span_breakpoints = sorted(span_breakpoints)

    start_index = span_breakpoints.index(seed_range[0])  # Index of seed range start
    end_index = span_breakpoints.index(seed_range[1])  # Index of seed range end

    # Pull out all pairs of adjacent numbers from seed range start to seed range end
    sub_ranges = [[span_breakpoints[i], span_breakpoints[i+1]]
                  for i in range(start_index, end_index)]
    
    for sub_range in sub_ranges:  # Convert all sub-ranges based on spans
        length = sub_range[1] - sub_range[0]
        sub_range[0] = convert_seed(sub_range[0], spans)
        sub_range[1] = sub_range[0] + length
    return sub_ranges

def recursive_convert(seed_range, span_history):
    if not span_history:
        return seed_range  # End of spans, return as is
    spans = span_history.pop(0)
    seed_ranges = convert_range(seed_range, spans)  # Split seed_range based on span bounds
    # Need recursion because one input can spawn arbitrarily many outputs
    return [recursive_convert(seed_range, span_history.copy()) for seed_range in seed_ranges]
    
        

seeds = lines[0].split(': ')
seeds = [int(seed) for seed in seeds[1].split()]

line_types = ['seed-to-soil map:',
              'soil-to-fertilizer map:',
              'fertilizer-to-water map:',
              'water-to-light map:',
              'light-to-temperature map:',
              'temperature-to-humidity map:',
              'humidity-to-location map:']
span_history = []
spans = []
for line in lines[1:]:
    if line in line_types:  # Apply spans at end of block
        seeds = [convert_seed(seed, spans) for seed in seeds]
        span_history.append(spans)
        spans = []  # Reset spans for new block
        continue
    if line == '':
        continue
    # span format is 'destination source range'
    spans.append([int(value) for value in line.split()])

span_history.append(spans)
seeds = [convert_seed(seed, spans) for seed in seeds]  # Apply the final spans
print(f'Part 1: {min(seeds)}')

seeds = lines[0].split(': ')
seeds = [int(seed) for seed in seeds[1].split()]
seed_ranges = []
while seeds:
    seed_ranges.append([seeds.pop(0), seeds.pop(0)])
seed_ranges = [(seed_range[0], seed_range[0] + seed_range[1]) for seed_range in seed_ranges]
min_location = 9999999999999999

for seed_range in seed_ranges:
    seed_locations = recursive_convert(seed_range, span_history.copy())
    if min(list(flatten(seed_locations))) < min_location:
        min_location = min(list(flatten(seed_locations)))

print(f'Part 2: {min_location}')  # Answer: 1928058