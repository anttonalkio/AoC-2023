from itertools import groupby, product

arrangements = 0

def is_valid_arrangement(springs, groups):
    grouped = [''.join(g) for _, g in groupby(springs)]
    grouped = [x for x in grouped if '#' in x]
    groups = groups.split(',')

    if len(grouped) != len(groups):
        return False

    return all(len(x) == int(y) for x,y in zip(grouped, groups))

def calculate_arrangements(springs, groups):
    arrangements = 0

    springs = springs.replace('?', '{}')
    for comb in product(['#', '.'], repeat=springs.count('{}')):
        if is_valid_arrangement(springs.format(*comb), groups):
            arrangements += 1

    return arrangements

with open('input.txt', 'r') as f:
    lines = f.read()

for line in lines.split('\n'):
    springs, groups = line.split(' ')
    arrangements += calculate_arrangements(springs, groups)

print(arrangements)

