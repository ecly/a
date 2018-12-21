import sys, re


def parse():
    entries1 = []
    part1, part2 = sys.stdin.read().strip().split("\n\n\n\n")
    for e in part1.split("\n\n"):
        entries1.append(
            tuple(
                map(
                    lambda l: tuple(map(int, l)),
                    map(lambda l: re.findall(r"\d+", l), e.split("\n")),
                )
            )
        )

    entries2 = []
    for e in part2.split("\n"):
        entries2.append(tuple(map(int, re.findall(r"\d+", e))))

    return entries1, entries2


def addr(registers, op):
    r = list(registers)
    r[op[3]] = r[op[1]] + r[op[2]]
    return tuple(r)

def addi(registers, op):
    r = list(registers)
    r[op[3]] = r[op[1]] + op[2]
    return tuple(r)

def mulr(registers, op):
    r = list(registers)
    r[op[3]] = r[op[1]] * r[op[2]]
    return tuple(r)

def muli(registers, op):
    r = list(registers)
    r[op[3]] = r[op[1]] * op[2]
    return tuple(r)

def banr(registers, op):
    r = list(registers)
    r[op[3]] = r[op[1]] & r[op[2]]
    return tuple(r)

def bani(registers, op):
    r = list(registers)
    r[op[3]] = r[op[1]] & op[2]
    return tuple(r)

def borr(registers, op):
    r = list(registers)
    r[op[3]] = r[op[1]] | r[op[2]]
    return tuple(r)

def bori(registers, op):
    r = list(registers)
    r[op[3]] = r[op[1]] | op[2]
    return tuple(r)

def setr(registers, op):
    r = list(registers)
    r[op[3]] = r[op[1]]
    return tuple(r)

def seti(registers, op):
    r = list(registers)
    r[op[3]] = op[1]
    return tuple(r)

def gtir(registers, op):
    r = list(registers)
    r[op[3]] = 1 if op[1] > r[op[2]] else 0
    return tuple(r)

def gtri(registers, op):
    r = list(registers)
    r[op[3]] = 1 if r[op[1]] > op[2] else 0
    return tuple(r)

def gttr(registers, op):
    r = list(registers)
    r[op[3]] = 1 if r[op[1]] > r[op[2]] else 0
    return tuple(r)

def eqir(registers, op):
    r = list(registers)
    r[op[3]] = 1 if op[1] == r[op[2]] else 0
    return tuple(r)

def eqri(registers, op):
    r = list(registers)
    r[op[3]] = 1 if r[op[1]] == op[2] else 0
    return tuple(r)

def eqrr(registers, op):
    r = list(registers)
    r[op[3]] = 1 if r[op[1]] == r[op[2]] else 0
    return tuple(r)

ACTIONS = [addr, addi, mulr, muli, mulr, banr, bani, borr, bori, setr, seti, gtir, gtri, gttr, eqir, eqri, eqrr]

def matches(before, op, after):
    return len(list(filter(lambda a: a(before, op) == after, ACTIONS)))


def part1(entries):
    count = 0
    for before, op, after in entries:
        if matches(before, op, after) >= 3:
            count += 1

    return count

def part2(entries1, entries2):
    op_ids = {i: set(ACTIONS) for i in range(16)}
    for before, op, after in entries1:
        op_id = op[0]
        bad_ops = set(filter(lambda a: a(before, op) != after, ACTIONS))
        op_ids[op_id] = op_ids[op_id] - bad_ops

    # deduce which item is what by iteratively removing
    # those functions that have already been deduced
    while any(len(v) > 1 for k, v in op_ids.items()):
        finished = set()
        for k, v in op_ids.items():
            if len(v) == 1:
                finished = finished | v
        for k, v in op_ids.items():
            if len(v) > 1:
                op_ids[k] = op_ids[k] - finished


    actions = {i: s.pop() for i, s in op_ids.items()}
    registers = [0, 0, 0, 0]
    for op in entries2:
        action = actions[op[0]]
        registers = action(registers, op)

    return registers[0]


if __name__ == "__main__":
    entries1, entries2 = parse()
    print(part1(entries1))
    print(part2(entries1, entries2))
