import sys
from copy import deepcopy
from collections import defaultdict

def part1(steps):
    completed = []
    while steps:
        can_complete = []
        for step, deps in steps.items():
            if all(d in completed for d in deps):
                can_complete.append(step)

        if can_complete:
            complete = sorted(can_complete)[0]
            completed.append(complete)
            del steps[complete]

    return ''.join(completed)


WORKERS = 5
OFFSET = 60
def part2(steps):
    workers = {}
    completed = []
    can_complete = []
    seconds = 0
    while steps:
        for item in sorted(can_complete):
            if item in workers and workers[item] <= 0:
                can_complete.remove(item)
                completed.append(item)
                del workers[item]
                del steps[item]
                # break

        for step, deps in steps.items():
            if all(d in completed for d in deps) and step not in can_complete:
                can_complete.append(step)

        for item in sorted(can_complete):
            if item not in workers and len(workers) <= WORKERS:
                workers[item] = OFFSET + ord(item) - 64

        if workers:
            seconds += 1

        workers = {k: v-1 for k, v in workers.items()}


    return seconds




def read_steps():
    steps = defaultdict(list)
    for line in sys.stdin.readlines():
        l = line.strip().split()
        dep = l[1]
        step = l[-3]
        steps[step].append(dep)
        if dep not in steps:
            steps[dep] = []

    return steps

steps = read_steps()
print(part1(deepcopy(steps)))
print(part2(deepcopy(steps)))
