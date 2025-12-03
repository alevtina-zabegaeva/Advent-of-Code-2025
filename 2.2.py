def false_ID(number):
    number_str = str(number)
    length = len(number_str)
    for l in range(1, length // 2 + 1):
        if length % l == 0:
            seq = number_str[:l]
            for i in range(l, length + 1 - l, l):
                if number_str[i:i + l] != seq:
                    break
            else:
                return True
    return False


filename = '2.1input.txt'
# filename = '2.1test.txt'

with open(filename) as f:
    line = f.readline().strip().split(',')

ranges = []
for r in line:
    r1, r2 = map(int, r.split('-'))
    ranges.append((r1, r2))

# print(ranges)

invalid_IDs = []
for r1, r2 in ranges:
    for r in range(r1, r2 + 1):
         if false_ID(r):
            invalid_IDs.append(r)

# print(invalid_IDs)
print(sum(invalid_IDs))
