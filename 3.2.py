filename = '3.1input.txt'
# filename = '3.1test.txt'

banks = []
with open(filename) as f:
    for line in f:
        banks.append(list(map(int, list(line.strip()))))

digits = 12
jolts = []
for bank in banks:
    length = len(bank)
    digit = max(bank[:-digits + 1])
    digit_ind = bank.index(digit)
    battery = digit * 10**(digits - 1)
    for i in range(1, digits):
        digits_to_search = bank[digit_ind + 1:length - digits + i + 1]
        digit = max(digits_to_search)
        digit_ind += digits_to_search.index(digit) + 1
        battery += digit * 10**(digits - i - 1)
    jolts.append(battery)

# print(jolts)
print(sum(jolts))
