str_to_num = {
    "one": "o1e",
    "two": "t2",
    "three": "t3e",
    "four": "4",
    "five": "5e",
    "six": "6",
    "seven": "7n",
    "eight": "t8t",
    "nine": "9e"
}


def resolve(s: str) -> str:
    for key, val in str_to_num.items():
        s = s.replace(key, val)

    return s


print(sum([int("".join([x[0], x[-1]])) for x in [[c for c in resolve(line) if c.isdigit()] for line in open("input.txt").readlines()]]))
