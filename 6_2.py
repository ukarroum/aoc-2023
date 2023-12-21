res = 1

with open("input.txt") as f:
    time = int("".join(f.readline().split(": ")[1].strip().split()))
    distance = int("".join(f.readline().split(": ")[1].strip().split()))

    wins = 0
    for i in range(time):
        if (time - i)*i > distance:
            wins += 1
    res *= wins

print(res)