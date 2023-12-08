import itertools

nodes = {}

with open('input.txt', 'r') as f:
    lines = f.readlines()

    directions = [x for x in lines[0].strip()]

for line in lines[2:]:
    key = line[0:3]
    left = line[7:10]
    right = line[12:15]
    nodes[key] = (left, right)

current_node =  'AAA'
steps = 0
for d in itertools.cycle(directions):
    if d == 'L':
        current_node = nodes[current_node][0]
    elif d == 'R':
        current_node = nodes[current_node][1]

    steps += 1

    if current_node == 'ZZZ':
        break


print(steps)