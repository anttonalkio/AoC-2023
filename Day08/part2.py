import  math

nodes = {}

with open('input.txt', 'r') as f:
    lines = f.readlines()

    directions = [x for x in lines[0].strip()]

for line in lines[2:]:
    key = line[0:3]
    left = line[7:10]
    right = line[12:15]
    nodes[key] = (left, right)

starting_nodes =  [x for x in nodes.keys() if x[2] == 'A']

when = []

for node in starting_nodes:
    steps = 1
    z_reached = False
    while not z_reached:
        if steps == 1:
            next_node = node
        
        for d in directions:
            if d == 'L':
                next_node = nodes[next_node][0]
            elif d == 'R':
                next_node = nodes[next_node][1]
            
            if(next_node[2] == 'Z'):
                z_reached = True
            else:
                steps += 1

    when.append(steps)

print(math.lcm(*when))