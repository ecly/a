import sys
from collections import Counter


def part1(coords):
    x_coords = [x for x, y in coords]
    y_coords = [y for x, y in coords]

    min_x = min(x_coords) - 1
    max_x = max(x_coords) + 1
    min_y = min(y_coords) - 1
    max_y = max(y_coords) + 1

    grid = {}
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            dist = sys.maxsize
            closest = None
            for cx, cy in coords:
                cdist = abs(x - cx) + abs(y - cy)
                if cdist < dist:
                    closest = (cx, cy)
                    dist = cdist
                elif cdist == closest:
                    closest = None

            grid[x, y] = closest

    infinite = set()
    for x in range(min_x, max_x + 1):
        infinite.add(grid[x, min_y])
        infinite.add(grid[x, max_y])

    for y in range(min_y, max_y + 1):
        infinite.add(grid[min_x, y])
        infinite.add(grid[max_x, y])

    # grid = {coord: closest for coord, closest in grid.items() if closest not in infinite}
    counter = Counter(grid.values())
    for q in infinite:
        counter.pop(q, infinite)
        print(counter.most_common(1))
    return counter.most_common(1)[0][1]


if __name__ == "__main__":
    coords = list(
        map(
            tuple,
            map(
                lambda c: map(int, c),
                map(lambda l: l.split(", "), sys.stdin.readlines()),
            ),
        )
    )
    print(coords)
    print(part1(coords))
