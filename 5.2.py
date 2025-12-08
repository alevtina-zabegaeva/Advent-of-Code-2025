def check_last_range(fresh_ranges):
    rl1, rl2 = fresh_ranges[-1]
    for j in range(len(fresh_ranges) - 1):
        rj1, rj2 = fresh_ranges[j]
        if max(rl1, rj1) <= min(rl2, rj2):
            return j, min(rl1, rj1), max(rl2, rj2)
    else:
        return -1, -1, -1


filename = '5.1input.txt'
# filename = '5.1test.txt'

fresh_ranges = []
with open(filename) as f:
    for line in f:
        if len(line) <= 1:
            break
        fresh_ranges.append(tuple(map(int, list(line.strip().split('-')))))

# print(fresh_ranges)

IDs_quantity = 0
while len(fresh_ranges) > 0:
    j, r1, r2 = check_last_range(fresh_ranges)
    if j >= 0:
        fresh_ranges[j] = (r1, r2)
        fresh_ranges.pop()
    else:
        r1, r2 = fresh_ranges.pop()
        IDs_quantity += r2 - r1 + 1

print(IDs_quantity)
