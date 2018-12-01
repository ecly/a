import sys, itertools
lines = [int(x) for x in sys.stdin.readlines()]
print(sum(lines))
seen = {0}
freq = 0
for l in itertools.cycle(lines):
    freq += l
    if freq in seen:
        break
    seen.add(freq)
print(freq)
