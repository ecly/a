import sys
from collections import Counter
twice = 0
thrice = 0
lines = sys.stdin.readlines()
for line in lines:
    c = Counter(line)
    if any(count == 2 for _, count in c.items()):
        twice += 1
    if any(count == 3 for _, count in c.items()):
        thrice += 1

print(twice * thrice)

def diff(s1, s2):
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1

    return count

for i in range(len(lines)):
    for j in range(i, len(lines)):
        if diff(lines[i], lines[j]) == 1:
            print(lines[i])
            print(lines[j])
            break
