res = 1

with open("input.txt") as f:
    times = [int(x) for x in f.readline().split(": ")[1].strip().split()]
    distances = [int(x) for x in f.readline().split(": ")[1].strip().split()]

    for time, distance in zip(times, distances):
        wins = 0
        for i in range(time):
            if (time - i)*i > distance:
                wins += 1
        res *= wins

print(res)