import sys

def parse():
    acres = []
    for y, l in enumerate(sys.stdin.readlines()):
        acres.append([])
        for x, c in enumerate(l.strip()):
            acres[y].append(c)

    return acres

def valid_pos(acres, x, y):
    return y >= 0 and y < len(acres) and x >= 0 and x < len(acres[y])


def get_adjacent(acres, x, y):
    ax = [(-1, 0), (1, 0), (-1, 1), (1, 1), (-1, -1), (1, -1), (0, 1), (0, -1)]
    ax = [(x+dx, y+dy) for dx, dy in ax if valid_pos(acres, x+dx, y+dy)]
    return ''.join([acres[ny][nx] for nx, ny in ax])

def pass_minute(acres):
    new_acres = []
    for y, line in enumerate(acres):
        new_acres.append([])
        for x, c in enumerate(line):
            adjacent = get_adjacent(acres, x, y)
            trees = adjacent.count("|")
            open_ground = adjacent.count(".")
            lumberyard = adjacent.count("#")
            if c == ".":
                new_acres[y].append("|" if trees >= 3 else ".")
            if c == "|":
                new_acres[y].append("#" if lumberyard >= 3 else "|")
            if c == "#":
                new_acres[y].append("#" if lumberyard >= 1 and trees >= 1 else ".")


    return new_acres


def solve(acres, count):
    for _ in range(count):
        acres = pass_minute(acres)

    trees = 0
    lumberyards = 0
    for l in acres:
        for c in l:
            if c == "#":
                lumberyards += 1
            elif c == "|":
                trees += 1

    return trees * lumberyards


if __name__ == '__main__':
    acres = parse()
    print(solve(acres, 10))
    # print(solve(acres, 1000000000))
