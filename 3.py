import itertools


def is_valid(x, y, row_size, col_size):
    return row_size > x >= 0 and col_size > y >= 0


with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

res = 0

for row, line in enumerate(lines):
    nb = ''
    part_nb = False

    for col, c in enumerate(line):
        if c.isdigit():
            nb += c

            for i, j in itertools.product([-1, 0, 1], [-1, 0, 1]):
                if is_valid(row + i, col + j, len(lines), len(line)) and lines[row + i][col + j] != '.' and not lines[row + i][col + j].isdigit():
                    part_nb = True

        else:
            if part_nb:
                print(nb)
                res += int(nb)
            part_nb = False
            nb = ''
    if part_nb:
        res += int(nb)

print(res)