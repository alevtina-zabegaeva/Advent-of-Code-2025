import math
import heapq
from collections import defaultdict


def get_all_connected_groups(graph):
    already_seen = set()
    result = []
    for node in graph:
        if node not in already_seen:
            connected_group, already_seen = get_connected_group(node, already_seen)
            result.append(connected_group)
    return result


def get_connected_group(node, already_seen):
        result = set()
        nodes = {node}
        while nodes:
            node = nodes.pop()
            already_seen.add(node)
            nodes.update(graph[node] - already_seen)
            result.add(node)
        return result, already_seen


def dist(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2)


filename = '8.1input.txt'
# filename = '8.1test.txt'

# cables = 10
cables = 1000

with open(filename) as f:
    boxes = [tuple(map(int, line.strip().split(','))) for line in f]

n = len(boxes)

distances = [(dist(boxes[i], boxes[j]), (i, j)) for i in range(n) for j in range(i + 1, n)]

closest_pairs = [pair for _, pair in heapq.nsmallest(cables, distances)]

graph = defaultdict(set)
for i1, i2 in closest_pairs:
    graph[i1].add(i2)
    graph[i2].add(i1)

components = get_all_connected_groups(graph)

components.sort(key=lambda item: len(item), reverse=True)

print(len(components[0]) * len(components[1]) * len(components[2]))
