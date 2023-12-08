from time import time

D = open(0).read()

"""
input:
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

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
    types = []
    pairs = set()
    for card in hand:
        if hand.count(card) == 2:
            pairs.add(card)

    if len(pairs) == 1:
        types.append("pair")
    elif len(pairs) == 2:
        types.append("two pair")

    # check for three of a kind
    for card in hand:
        if hand.count(card) == 3:
            types.append("three of a kind")
            break

    # check for 4 of a kind
    for card in hand:
        if hand.count(card) == 4:
            types.append("four of a kind")
            break

    # check for 5 of a kind
    for card in hand:
        if hand.count(card) == 5:
            types.append("five of a kind")
            break

    # check for full house
    if len(types) == 2 and types[0] == ("pair") and types[1] == ("three of a kind"):
        del types[0]
        del types[0]
        types.append("full house")

    # high card
    if len(types) == 0:
        types.append("high card")

    return T[types[0]]


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
