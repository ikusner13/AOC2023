import math


D = open(0).read().split("\n\n")

directions = {"R": 1, "L": 0}


def part2():
    instructions = D[0]
    paths = {}
    for node in D[1].split("\n"):
        start, rl = node.split("=")
        left, right = [x.strip().strip("()") for x in rl.split(",")]
        paths[start.strip()] = (left, right)

    starting_points = [k for k in paths if k.endswith("A")]

    steps = 0
    seen = set()
    while True:
        for i, sp in enumerate(starting_points):
            if sp.endswith("Z"):
                seen.add((sp, steps))
            starting_points[i] = paths[sp][
                directions[instructions[steps % len(instructions)]]
            ]

        if len(seen) == len(starting_points):
            break

        steps += 1

    return math.lcm(*[num for _, num in seen])


if __name__ == "__main__":
    print(part2())
