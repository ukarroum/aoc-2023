with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

res = 0

for line in lines:
    winning_nbs, elf_nbs = line.split(": ")[1].split(" | ")

    winning_nbs = {int(nb) for nb in winning_nbs.split()}
    elf_nbs = {int(nb) for nb in elf_nbs.split()}

    winning = len([nb for nb in elf_nbs if nb in winning_nbs])

    if winning:
        res += 2 ** (winning - 1)

print(res)
