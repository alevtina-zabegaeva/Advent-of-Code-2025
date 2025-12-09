import numpy as np
from collections import Counter


filename = '7.1input.txt'
# filename = '7.1test.txt'

with open(filename) as f:
    input = [list(line.strip()) for line in f]

input = np.array(input)
m, n = input.shape

x, y = np.where(input == 'S')
x, y = x[0], y[0]

splitters = np.where(input == '^')
splitters = set(zip(splitters[0], splitters[1]))

timeline_current = Counter({y: 1})

for i in range(x + 1, m):
    timeline_prev = timeline_current.copy()
    timeline_current = Counter()
    for j, q in timeline_prev.items():
        if not (i, j) in splitters:
            timeline_current[j] += q
        else:
            timeline_current.update({j - 1: q, j + 1: q})

print(sum(q for q in timeline_current.values()))
