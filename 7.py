from functools import cache
from collections import Counter

mapping = {c: n for c,n in zip("TJQKA", range(10, 15))}


@cache
def score(hand):
    ctr = Counter(hand)
    if ctr.most_common(1)[0][1] == 5:
        type = 6
    elif ctr.most_common(1)[0][1] == 4:
        type = 5
    elif ctr.most_common(1)[0][1] == 3 and ctr.most_common(2)[1][1] == 2:
        type = 4
    elif ctr.most_common(1)[0][1] == 3:
        type = 3
    elif ctr.most_common(1)[0][1] == 2 and ctr.most_common(2)[1][1] == 2:
        type = 2
    elif ctr.most_common(1)[0][1] == 2:
        type = 1
    else:
        type = 0

    return type, *hand


with open("input.txt") as f:
    hands = [line.strip().split() for line in f.readlines()]

    for i in range(len(hands)):
        hands[i][0] = tuple([mapping.get(c, int(c) if c.isdigit() else c) for c in hands[i][0]])

    hands = sorted(hands, key=lambda x: score(x[0]), reverse=True)

    print(sum([int(hand[1]) * m for hand, m in zip(hands[::-1], range(1, len(hands) + 1))]))
