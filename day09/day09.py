from collections import defaultdict
import blist

def solve(players, last_marble):
    marbles = blist.blist([0, 1])
    current_idx = 1
    scores = defaultdict(int)
    for i in range(2, last_marble + 1):
        player = i % (players)
        if i % 23 == 0:
            scores[player] += i
            remove_idx = (current_idx - 7) % len(marbles)
            scores[player] += marbles[remove_idx]
            del marbles[remove_idx]
            current_idx = remove_idx
        else:
            current_idx = (current_idx + 2) % len(marbles)
            if current_idx == 0:
                current_idx = len(marbles)

            marbles.insert(current_idx, i)

    return max(scores.values())

if __name__ == '__main__':
    players = 479
    last_marble = 71035

    print(solve(players, last_marble))
    print(solve(players, last_marble * 100))
