def square(x1, y1, x2, y2):
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)


filename = '9.1input.txt'
# filename = '9.1test.txt'

with open(filename) as f:
    tiles = [tuple(map(int, line.strip().split(','))) for line in f]

n = len(tiles)

squares = [square(*tiles[i], *tiles[j]) for i in range(n) for j in range(i + 1, n)]

print(max(squares))
