from time import time

D = open(0).read()


C = {
    "T": 10,
    "Q": 12,
    "K": 13,
    "A": 14,
    "J": 1,
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
    j_count = hand.count("J")

    current_best = "high card"

    counted = set()
    for h in hand:
        if h in counted or h == "J":
            continue

        count = hand.count(h)
        counted.add(h)

        if count == 1:
            current_best = current_best
        elif count == 2:
            if current_best == "pair":
                current_best = "two pair"
            elif current_best == "three of a kind":
                current_best = "full house"
            else:
                current_best = "pair"

        elif count == 3:
            if current_best == "pair":
                current_best = "full house"
            else:
                current_best = "three of a kind"
        elif count == 4:
            current_best = "four of a kind"
        else:
            current_best = "five of a kind"

    if current_best == "high card":
        if j_count == 1:
            current_best = "pair"
        elif j_count == 2:
            current_best = "three of a kind"
        elif j_count == 3:
            current_best = "four of a kind"
        elif j_count == 4:
            current_best = "five of a kind"
        elif j_count == 5:
            current_best = "five of a kind"

    elif current_best == "pair":
        if j_count == 1:
            current_best = "three of a kind"
        elif j_count == 2:
            current_best = "four of a kind"
        elif j_count == 3:
            current_best = "five of a kind"

    elif current_best == "two pair":
        if j_count == 1:
            current_best = "full house"

    elif current_best == "three of a kind":
        if j_count == 1:
            current_best = "four of a kind"
        elif j_count == 2:
            current_best = "five of a kind"

    elif current_best == "four of a kind" and j_count == 1:
        current_best = "five of a kind"

    return T[current_best]


def part2():
    lines = D.splitlines()

    types_in_hand = [
        (determine_hand_type(hand), hand, int(bet))
        for hand, bet in (line.split() for line in lines)
    ]

    s = sorted(types_in_hand, key=lambda t: (t[0], [C.get(char, 0) for char in t[1]]))

    print(sum((i + 1) * h[2] for i, h in enumerate(s)))


if __name__ == "__main__":
    start = time()
    part2()
    print(f"Time: {(time() - start) * 1000:.3f}ms")
