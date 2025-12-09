import numpy as np


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

# print(x, y)
# print(splitters)

splitted = set()
flow = {x: {y,}}

for i in range(1, m):
    flow_prev = flow[i - 1]
    flow_current = set()
    for j in flow_prev:
        if not (i, j) in splitters:
            flow_current.add(j)
        else:
            splitted.add((i, j))
            flow_current.add(j - 1)
            flow_current.add(j + 1)
    flow[i] = flow_current

# print(splitted)
print(len(splitted))
