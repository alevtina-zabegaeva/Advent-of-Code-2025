import numpy as np
import re


filename = '6.1input.txt'
# filename = '6.1test.txt'

numbers = []
operators = []
with open(filename) as f:
    for line in f:
        line = re.split(' +', line.strip())
        if line[0] == '+' or line[0] == '*':
            operators = line
        else:
            numbers.append(list(map(int, line)))

numbers = np.array(numbers)

total = []
for i in range(numbers.shape[1]):
    if operators[i] == '+':
        total.append(sum(numbers[:, i]))
    else:
        total.append(np.prod(numbers[:, i]))

print(sum(total))
