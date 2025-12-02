filename = '1.1input.txt'
# filename = '1.1test.txt'

instructions = []
with open(filename) as f:
    for line in f:
        direction = 1 if line[0] == 'R' else -1
        instructions.append(direction * int(line[1:]))

# print(instructions)

dial = 50
password = 0
for instruction in instructions:
    dial = (dial + instruction) % 100
    if dial == 0:
        password += 1

print(password)
