import sys
from copy import deepcopy

dirs = {">": (1, 0),
        "<": (-1, 0),
        "^": (0, -1),
        "v": (0, 1)}
chars = {v: k for k, v in dirs.items()}

def parse():
    grid = {}
    carts = {}
    for y, line in enumerate(sys.stdin.readlines()):
        for x, c in enumerate(line):
            if c in dirs:
                carts[x, y] = (dirs[c], "left")
                grid[x, y] = "-" if c in "<>" else "|"
            elif c != " ":
                grid[x, y] = c

    return grid, carts


def print_grid(grid, carts):
    "Utility function for printing the grid"
    maxx = max(x for x, y in grid.keys())
    maxy = max(y for x, y in grid.keys())
    print(carts)
    for y in range(maxy + 1):
        for x in range(maxx + 1):
            if (x, y) in carts:
                direction = carts[x, y][0]
                sys.stdout.write(chars[direction])
            elif (x, y) in grid:
                sys.stdout.write(grid[x, y])
            else:
                sys.stdout.write(" ")

        sys.stdout.write("\n")
    print()


def move(grid, nx, ny, direction, turn):
    dx, dy = direction
    if grid[nx, ny] in "|-":
        return (direction, turn)
    elif grid[nx, ny] == "\\":
        return ((dy, dx), turn)
    elif grid[nx, ny] == "/":
        return ((-dy, -dx), turn)
    elif grid[nx, ny] == "+":
        if turn == "left":
            return ((dy, -dx), "straight")
        elif turn == "straight":
            return ((dx, dy), "right")
        elif turn == "right":
            return ((-dy, dx), "left")


def part1(grid, carts):
    while True:
        # sort on y then x
        for (x, y), (direction, turn) in sorted(carts.items(), key=lambda x: x[0][::-1]):
            dx, dy = direction
            nx, ny = (x + dx, y + dy)

            if (nx, ny) in carts:
                return (nx, ny)

            del carts[x, y]
            new_val = move(grid, nx, ny, direction, turn)
            carts[nx, ny] = new_val


def part2(grid, carts):
    while True:
        # sort on y then x
        for (x, y), (direction, turn) in sorted(carts.items(), key=lambda x: x[0][::-1]):
            # if it already crashed
            if (x, y) not in carts:
                continue

            dx, dy = direction
            nx, ny = (x + dx, y + dy)

            if (nx, ny) in carts:
                del carts[nx, ny]
                del carts[x, y]
            else:
                del carts[x, y]
                new_val = move(grid, nx, ny, direction, turn)
                carts[nx, ny] = new_val
                if len(carts) == 1:
                    return list(carts.keys())[0]



def main():
    grid1, carts1 = parse()
    grid2, carts2 = deepcopy(grid1), deepcopy(carts1)

    print(part1(grid1, carts1))
    print(part2(grid2, carts2))

if __name__ == '__main__':
    main()
