def square(x1, y1, x2, y2):
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)


def point_inside_polygon(x, y, poly):
    inside = False
    for i in range(len(poly)):
        ax, ay = poly[i]
        bx, by = poly[i - 1]
        if ay == by == y and min(ax, bx) <= x <= max(ax, bx):
            return True
        
        if ax == bx:
            if min(ay, by) <= y < max(ay, by):
                if x == ax:
                    return True
                if x < ax:
                    inside = not inside
    return inside


def rectangle_intersects_polygon(i, j, poly):
    ix, iy = poly[i]
    jx, jy = poly[j]

    xmin, xmax = sorted((ix, jx))
    ymin, ymax = sorted((iy, jy))

    n = len(poly)

    for k in range(n):
        x1, y1 = red_tiles[k]
        x2, y2 = red_tiles[k - 1]

        if x1 == x2:
            if xmin < x1 < xmax and max(y1, y2) > ymin and min(y1, y2) < ymax:
                return True

        if y1 == y2:
            if ymin < y1 < ymax and max(x1, x2) > xmin and min(x1, x2) < xmax:
                return True

    return False


def rectangle_inside_polygon(i, j, poly):
    if rectangle_intersects_polygon(i, j, poly):
        return False
    
    ix, iy = poly[i]
    jx, jy = poly[j]

    xmin, xmax = sorted((ix, jx))
    ymin, ymax = sorted((iy, jy))

    cx = (xmin + xmax) // 2
    cy = (ymin + ymax) // 2

    return point_inside_polygon(cx, cy, poly)


filename = '9.1input.txt'
# filename = '9.1test.txt'

with open(filename) as f:
    red_tiles = [tuple(map(int, line.strip().split(','))) for line in f]
# print(red_tiles)

n = len(red_tiles)

rectangles = [(square(*red_tiles[i], *red_tiles[j]), i, j) for i in range(n) for j in range(i + 1, n)]
rectangles.sort(reverse=True)
# print(rectangles)

for s, i, j in rectangles:
    if rectangle_inside_polygon(i, j, red_tiles):
        print("square =", s, " i, j = (", i, j, ")")
        print("ix, iy = (", red_tiles[i], ") jx, jy = (", red_tiles[j], ")")
        break
