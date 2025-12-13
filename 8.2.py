import math


def dist(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2)


filename = '8.1input.txt'
# filename = '8.1test.txt'

# cables = 10
cables = 1000

with open(filename) as f:
    boxes = [tuple(map(int, line.strip().split(','))) for line in f]

n = len(boxes)

distances = {dist(boxes[i], boxes[j]): (i, j) for i in range(n) for j in range(i + 1, n)}
distances = dict(sorted(distances.items()))
closest_pairs = [pair for _, pair in distances.items()]

boxes_groups = [-1] * n
ind_groups = 0

for i, j in closest_pairs:
    i_group = boxes_groups[i]
    j_group = boxes_groups[j]
    if i_group == -1 and j_group == -1:
        boxes_groups[i] = ind_groups
        boxes_groups[j] = ind_groups
        ind_groups += 1
    elif i_group == -1 and j_group != -1:
        boxes_groups[i] = j_group
    elif i_group != -1 and j_group == -1:
        boxes_groups[j] = i_group
    elif i_group != j_group:
        boxes_groups[j] = i_group
        boxes_groups = [i_group if group == j_group else group for group in boxes_groups]
        ind_groups -= 1
    first = boxes_groups[0]
    if all(first == x for x in boxes_groups):
        break

print(boxes[i][0] * boxes[j][0])
