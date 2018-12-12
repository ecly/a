INPUT = 5235
def solve(grid, size):
    topleft = {}
    for x in range(1, 300-size+1):
        for y in range(1, 300-size+1):
            score = 0
            for xoff in range(size):
                score += sum(grid[x+xoff][y:y+size])

            topleft[x, y] = score

    return max(topleft.items(), key=lambda l: l[1])

grid = [[None for _ in range(301)] for _ in range(301)]
for y in range(1, 301):
    for x in range(1, 301):
        rack_id = x + 10
        power = rack_id * y
        power += INPUT
        power *= rack_id
        power = int(str(power)[-3])
        grid[x][y] = power - 5


def part1():
    (p1x, p1y), _ = solve(grid, 3)
    return "%d,%d" % (p1x, p1y)

def part2():
    max_score = 0
    max_corner = None
    max_size = None
    for size in range(300):
        corner, score = solve(grid, size)
        if score > max_score:
            max_score = score
            max_corner = corner
            max_size = size

    return "%d,%d,%d" % (max_corner[0], max_corner[1], max_size)

print(part1())
#part2, takes a couple of minutes using pypy
print(part2())
