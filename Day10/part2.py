from matplotlib.path import Path

with open('input.txt', 'r') as f:
    lines = f.read()

directions = {
    ("|", (0, 1)): (0, 1),
    ("|", (0, -1)): (0, -1),
    ("-", (1, 0)): (1, 0),
    ("-", (-1, 0)): (-1, 0),
    ("L", (-1, 0)): (0, -1),
    ("L", (0, 1)): (1, 0),
    ("J", (1, 0)): (0, -1),
    ("J", (0, 1)): (-1, 0),
    ("7", (1, 0)): (0, 1),
    ("7", (0, -1)): (-1, 0),
    ("F", (-1, 0)): (0, 1),
    ("F", (0, -1)): (1, 0),
}

map = [[x for x in y] for y in lines.split()]

last_move = (0, -1)
position = next(
    (j, i - 1) for i, row in enumerate(map) for j, v in enumerate(row) if v == "S"
)

path = []

while(map[position[1]][position[0]] != 'S'):
    path.append(position)
    tile = map[position[1]][position[0]]
    next = directions[(tile, last_move)]
    position = (position[0] + next[0], position[1] + next[1])
    last_move = next

answer = 0

p = Path(path)

for y in range(len(map)):
    for x in range(len(map[0])):
        if (x,y) in path:
            continue
        if p.contains_point((x,y)):
            answer += 1

print(answer)