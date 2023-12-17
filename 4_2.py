from functools import cache

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

res = 0


@cache
def scratch_card(i):
    line = lines[i]

    winning_nbs, elf_nbs = line.split(": ")[1].split(" | ")

    winning_nbs = {int(nb) for nb in winning_nbs.split()}
    elf_nbs = {int(nb) for nb in elf_nbs.split()}

    nb_wins = len([nb for nb in elf_nbs if nb in winning_nbs])

    return nb_wins + sum(scratch_card(i + j + 1) for j in range(nb_wins))


res = 0

for i in range(len(lines)):
    res += scratch_card(i) + 1

print(res)
