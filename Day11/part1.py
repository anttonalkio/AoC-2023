import numpy as np
import itertools

def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

with open('input.txt', 'r') as f:
    lines = f.read()

map = [[0 if x == '.' else 1 for x in y] for y in lines.split()]

array = np.array(map)

for i, x in enumerate(np.where(~array.any(axis=1))[0]):
    array = np.insert(array, x+i, np.zeros(array.shape[1]), axis=0)

for i, y in enumerate(np.where(~array.any(axis=0))[0]):
    array = np.insert(array, y+i, np.zeros(array.shape[0]), axis=1)

answer = 0

for comb in list(itertools.combinations(list(zip(*np.where(array == 1))), 2)):
    path = manhattan(comb[0], comb[1])
    answer += path
    
print(answer)