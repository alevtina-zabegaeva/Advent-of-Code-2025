filename = '1.1input.txt'
# filename = '1.1test.txt'

instructions = []
with open(filename) as f:
    for line in f:
        direction = 1 if line[0] == 'R' else -1
        instructions.append(direction * int(line[1:]))

dial = 50
password = 0
for instruction in instructions:
    dial_prev = dial
    dial += instruction
    counter = dial // 100
    dial %= 100
    password += abs(counter)

    if dial == 0 and dial_prev != 0 and counter <= 0:
        password += 1
    if dial != 0 and dial_prev == 0 and counter < 0:
        password -= 1

print(password)
