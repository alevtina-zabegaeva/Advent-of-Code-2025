import numpy as np

filename = '4.1input.txt'
# filename = '4.1test.txt'

with open(filename) as f:
    input = [list(line.strip()) for line in f]

input = np.array(input)

rolls = np.where(input == '@')
rolls = set(zip(rolls[0], rolls[1]))

neihgbours = ((-1, -1), (-1, 0), (-1, 1),
              (0, -1),           (0, 1),
              (1, -1),  (1, 0),  (1, 1))

# m, n = input.shape
# maze = np.full((m + 2, n + 2), '.')
# maze[1:-1, 1:-1] = input
# print(maze)

accessed_rolls = set()
for roll_i, roll_j in rolls:
    adjacent = set((roll_i + neihgbour_i, roll_j + neihgbour_j) for neihgbour_i, neihgbour_j in neihgbours)
    if len(adjacent & rolls) < 4:
        accessed_rolls.add((roll_i, roll_j))

print(len(accessed_rolls))