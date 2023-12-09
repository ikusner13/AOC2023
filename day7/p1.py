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
    counter = Counter()
    best_type = T["high card"]
    for card in hand:
        counter[card] += 1
        if counter[card] == 4:
            best_type = T["four of a kind"]
        elif counter[card] == 5:
            best_type = T["five of a kind"]
        elif counter[card] == 2:
            if best_type == T["pair"]:
                best_type = T["two pair"]
            elif 3 in counter.values():
                best_type = T["full house"]
            else:
                best_type = T["pair"]
        elif counter[card] == 3:
            if 2 in counter.values():
                best_type = T["full house"]
            else:
                best_type = T["three of a kind"]

    return best_type


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
