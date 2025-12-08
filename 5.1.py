filename = '5.1input.txt'
# filename = '5.1test.txt'

fresh_ranges = []
IDs = []
with open(filename) as f:
    for line in f:
        if len(line) <= 1:
            break
        fresh_ranges.append(tuple(map(int, list(line.strip().split('-')))))
    for line in f:
        IDs.append(int(line.strip()))

# print(fresh_ranges)
# print(IDs)

fresh_IDs = []
for ID in IDs:
    for r1, r2 in fresh_ranges:
        if r1 <= ID <= r2:
            fresh_IDs.append(ID)
            break

# print(fresh_IDs)
print(len(fresh_IDs))
