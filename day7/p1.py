from collections import Counter
from time import time

D = open(0).read()

C = {
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}

T = {
    "high card": 1,
    "pair": 2,
    "two pair": 3,
    "three of a kind": 4,
    "full house": 5,
    "four of a kind": 6,
    "five of a kind": 7,
}


def determine_hand_type(hand):
    counter = Counter(hand)
    counts = list(counter.values())

    if 4 in counts:
        return T["four of a kind"]
    elif 5 in counts:
        return T["five of a kind"]
    elif 2 in counts:
        if counts.count(2) == 2:
            return T["two pair"]
        elif 3 in counts:
            return T["full house"]

        return T["pair"]
    elif 3 in counts:
        if 2 in counts:
            return T["full house"]

        return T["three of a kind"]

    return T["high card"]


def part2():
    lines = D.splitlines()

    types_in_hand = []
    for line in lines:
        hand, bet = line.split()
        type = determine_hand_type(hand)
        types_in_hand.append((type, hand, int(bet)))

    sum = 0

    def custom_sort_key(tuple):
        return (tuple[0], [C.get(char, 0) for char in tuple[1]])

    s = sorted(types_in_hand, key=custom_sort_key)
    for i, h in enumerate(s):
        sum += (i + 1) * h[2]

    print(f"sum: {sum}")


if __name__ == "__main__":
    start = time()
    part2()
    print(f"Time: {(time() - start) * 1000:.3f}ms")
