import numpy as np


def remove_accesed(rolls):
    neihgbours = ((-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1),  (1, 0),  (1, 1))
    
    accessed_rolls = set()
    for roll_i, roll_j in rolls:
        adjacent = set((roll_i + neihgbour_i, roll_j + neihgbour_j) for neihgbour_i, neihgbour_j in neihgbours)
        if len(adjacent & rolls) < 4:
            accessed_rolls.add((roll_i, roll_j))
    return rolls - accessed_rolls


filename = '4.1input.txt'
# filename = '4.1test.txt'

with open(filename) as f:
    input = [list(line.strip()) for line in f]

input = np.array(input)

rolls = np.where(input == '@')
rolls = set(zip(rolls[0], rolls[1]))

start_size = len(rolls)

while True:
    current_size = len(rolls)
    rolls = remove_accesed(rolls)
    if current_size == len(rolls):
        break

print(start_size - current_size)
