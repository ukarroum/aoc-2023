possible = 0

limits = {
    "red": 12,
    "green": 13,
    "blue": 14
}

with open("input.txt") as f:
    lines = [line.split(": ") for line in f.readlines()]

    for line in lines:
        imp = False
        sets = line[1].split("; ")

        for s in sets:
            s = s.split(", ")

            for nb, color in [x.split(" ") for x in s]:
                if limits[color.strip()] < int(nb):
                    imp = True
                    break
            if imp:
                break
        else:
            possible += int(line[0][5:])

    print(possible)
