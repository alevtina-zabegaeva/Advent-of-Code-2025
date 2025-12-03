def false_ID(number):
    number_str = str(number)
    length = len(number_str)
    return length % 2 == 0 and number_str[:length // 2] == number_str[length // 2:]


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
