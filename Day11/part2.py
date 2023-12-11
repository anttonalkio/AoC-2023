import numpy as np
import itertools

def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

def expand(x, y, cols_to_expand, rows_to_expand, expansion_factor=1_000_000):
    x += sum(c < x for c in cols_to_expand) * (expansion_factor-1)
    y += sum(r < y for r in rows_to_expand) * (expansion_factor-1)
    return x,y

with open('input.txt', 'r') as f:
    lines = f.read()

map = [[0 if x == '.' else 1 for x in y] for y in lines.split()]

array = np.array(map)

answer = 0

cols_to_expand = np.where(~array.any(axis=1))[0]
rows_to_expand = np.where(~array.any(axis=0))[0]

print(cols_to_expand)
print(rows_to_expand)

galaxies = list(zip(*np.where(array == 1)))

expanded = [expand(x, y, cols_to_expand, rows_to_expand) for x, y in galaxies]

for (sx, sy), (ex, ey) in list(itertools.combinations(expanded, 2)):
    path = manhattan((sx, sy), (ex, ey))

    answer += path
    
print(answer)