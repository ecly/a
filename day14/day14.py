import math

def get_digit(n, i):
    return n // 10**i % 10

def int_len(n):
    if n == 0:
        return 1
    return int(math.log10(n))+1

def get_new_recipes(n):
    recipes = []
    for i in range(int_len(n)):
        recipes.append(get_digit(n, i))

    return recipes[::-1]

def part1(count):
    recipes = [3, 7]
    elf1, elf2 = 0, 1
    while len(recipes) < count + 10:
        elf1_score = recipes[elf1]
        elf2_score = recipes[elf2]
        new_score = elf1_score + elf2_score
        new_recipes = get_new_recipes(new_score)
        recipes.extend(new_recipes)
        elf1 = (1 + elf1 + elf1_score) % len(recipes)
        elf2 = (1 + elf2 + elf2_score) % len(recipes)

    return ''.join(map(str, recipes[count:count+10]))

def part2(goal):
    recipes = [3, 7]
    elf1, elf2 = 0, 1
    while True:
        elf1_score = recipes[elf1]
        elf2_score = recipes[elf2]
        new_score = elf1_score + elf2_score
        new_recipes = get_new_recipes(new_score)
        recipes.extend(new_recipes)
        elf1 = (1 + elf1 + elf1_score) % len(recipes)
        elf2 = (1 + elf2 + elf2_score) % len(recipes)
        suffix = ''.join(map(str, recipes[-10:]))
        if goal in suffix:
            return len(recipes) -10 + suffix.index(goal)

if __name__ == '__main__':
    INPUT = 793061
    print(part1(INPUT))
    # runs for about a minute or so on my machine
    print(part2(str(INPUT)))
