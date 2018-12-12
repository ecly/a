import sys
from collections import defaultdict

def part1(initial, rules, generations=20):
    state = defaultdict(lambda: '.')
    for i, c in enumerate(initial):
        state[i] = c

    new = defaultdict(lambda: '.')
    for _ in range(generations):
        keys = state.keys()
        mini, maxi = min(keys), max(keys)

        for i in range(mini, maxi+1):
            sys.stdout.write(state[i])
        print()

        for i in range(mini - 2, maxi + 3):
           c = ""
           c += state[i-2]
           c += state[i-1]
           c += state[i]
           c += state[i+1]
           c += state[i+2]
           new[i] = rules[c]

        state = new
        new = defaultdict(lambda: '.')

    total = 0
    for k, v in state.items():
        if v == "#":
            total += k

    print(total)

    return total


def part2(initial):
    converged = "##.##.##.##....##.##.##.##.##.##.##.##.##....##.##.##.##.##.##.##.##.##....##.##.##....##.##.##.##.##.##....##.##.##.##.##.##.##.##....##.##.##.##.##.##.##.##.##.##"
    leftmost = 50000000000 - len(converged) + len(initial)
    return sum(i for i, c in enumerate(converged, leftmost) if c == '#')



lines = sys.stdin.readlines()
start = lines[0].strip().split(": ")[1]
rules = defaultdict(lambda: ".")

for line in lines[2:]:
    f, t = line.strip().split(" => ")
    rules[f] = t


print(part1(start, rules))
print(part2(start))
