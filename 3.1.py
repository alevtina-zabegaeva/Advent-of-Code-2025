filename = '3.1input.txt'
# filename = '3.1test.txt'

banks = []
with open(filename) as f:
    for line in f:
        banks.append(list(map(int, list(line.strip()))))

print(banks)

jolts = 0
for bank in banks:
    battery1 = max(bank[:-1])
    i1 = bank.index(battery1)
    battery2 = max(bank[i1 + 1:])
    jolts += battery1 * 10 + battery2

print(jolts)
