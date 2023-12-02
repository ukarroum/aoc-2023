print(sum([int("".join([x[0], x[-1]])) for x in [[c for c in line if c.isdigit()] for line in open("input.txt").readlines()]]))
