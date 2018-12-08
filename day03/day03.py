import sys
from collections import defaultdict
grid = defaultdict(set)
claims = set()
for l in sys.stdin.readlines():
    claim, r = l.strip().split(" @ ")
    claims.add(claim)
    coords, dim = r.split(": ")
    x, y = [int(n) for n in coords.split(",")]
    i, j = [int(n) for n in dim.split("x")]
    for a in range(x, x+i):
        for b in range(y, y+j):
            grid[(a, b)].add(claim)

print(len([c for _, c in grid.items() if len(c) > 1]))
for s in grid.values():
    if len(s) >= 2:
        for c in s:
            claims.discard(c)

print(claims)
