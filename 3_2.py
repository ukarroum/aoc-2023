import itertools


def is_valid(x, y, row_size, col_size):
    return row_size > x >= 0 and col_size > y >= 0


with open("input.txt") as f:
    lines = [list(line.strip()) for line in f.readlines()]

res = 0
ids = 0

gears = []

for row, line in enumerate(lines):
    nb = ''
    part_nb = False

    for col, c in enumerate(line):
        if c.isdigit():
            nb += c
        else:
            if c == '*':
                gears.append((row, col))

            for i in range(len(nb)):
                line[col - i - 1] = (int(nb), ids)
            ids += 1
            nb = ''
    if nb != '':
        for i in range(len(nb)):
            line[col - i - 1] = (int(nb), ids)
        ids += 1

for gear in gears:
    adj_nbs = []

    for i, j in itertools.product([-1, 0, 1], [-1, 0, 1]):
        if is_valid(gear[0] + i, gear[1] + j, len(lines), len(lines[0])) and isinstance(lines[gear[0] + i][gear[1] + j][0], int):
            if lines[gear[0] + i][gear[1] + j] not in adj_nbs:
                adj_nbs.append(lines[gear[0] + i][gear[1] + j])
                if len(adj_nbs) > 2:
                    break

    if len(adj_nbs) == 2:
        res += adj_nbs[0][0] * adj_nbs[1][0]


print(res)
