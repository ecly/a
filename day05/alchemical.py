def part1(s):
    i = 0
    while i < len(s) - 1:
        react = abs(ord(s[i]) - ord(s[i+1])) == 32
        if react:
            if i == len(s) - 1:
                s = s[:i]
            else:
                s = s[:i] + s[i+2:]
                i = max(0, i-1)
        else:
            i += 1

    return len(s)

def part2(s):
    shortest = 999999
    for c in "abcdefghijklmnopqrstuvxyz":
        shortest = min(shortest, part1(s.replace(c, "").replace(c.upper(), "")))

    return shortest

s = input().strip()
print(part1(s))
print(part2(s))
