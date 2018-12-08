import sys
from collections import Counter


def solve(coords):
    x_coords = [x for x, y in coords]
    y_coords = [y for x, y in coords]

    min_x = min(x_coords) - 1
    max_x = max(x_coords) + 1
    min_y = min(y_coords) - 1
    max_y = max(y_coords) + 1

    # Part1
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
                elif cdist == dist:
                    closest = None
            grid[x, y] = closest

    infinite = set()
    for x in range(min_x, max_x + 1):
        infinite.add(grid[x, min_y])
        infinite.add(grid[x, max_y])

    for y in range(min_y, max_y + 1):
        infinite.add(grid[min_x, y])
        infinite.add(grid[max_x, y])

    grid = {coord: closest for coord, closest in grid.items() if closest not in infinite}
    counter = Counter(grid.values())
    part1 = counter.most_common(1)[0][1]

    # Part2
    part2 = sum(sum(abs(x-cx)+abs(y-cy) for cx,cy in coords) < 10_000 for x in range(min_x, max_x+1) for y in range(min_y, max_y+1))

    return part1, part2



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
    part1, part2 = solve(coords)
    print(part1)
    print(part2)
