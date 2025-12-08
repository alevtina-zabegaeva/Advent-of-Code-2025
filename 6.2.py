import re


filename = '6.1input.txt'
# filename = '6.1test.txt'

operators = []
first_line = True
with open(filename) as f:
    for line in f:
        if line[-1] == '\n':
            line = line.strip('\n')
            if first_line:
                numbers = [''] * len(line)
                first_line = False
            for i, char in enumerate(line):
                if char != ' ':
                    numbers[i] = numbers[i] + char
        else:
            operators = re.split(' +', line.strip())


total = []
i = 0
n = len(numbers)
for operator in operators:
    vals = []
    while i < n and numbers[i] != '':
        vals.append(int(numbers[i]))
        i += 1
    i += 1

    if operator == '+':
        total.append(sum(vals))
    else:
        prod = 1
        for v in vals:
            prod *= v
        total.append(prod)

# print(total)
print(sum(total))
