with open("input.txt") as f:
    res = 0

    lines = [line.split(": ") for line in f.readlines()]

    for line in lines:
        maxs = {
            "red": 0,
            "green": 0,
            "blue": 0
        }

        sets = line[1].split("; ")

        for s in sets:
            s = s.split(", ")

            for nb, color in [x.split(" ") for x in s]:
                if int(nb) > maxs[color.strip()]:
                    maxs[color.strip()] = int(nb)

        res += maxs["red"] * maxs["green"] * maxs["blue"]

    print(res)
