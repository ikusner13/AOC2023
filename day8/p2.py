import math


D = open(0).read().split("\n\n")

directions = {"R": 1, "L": 0}


def part2():
    instructions = D[0] * 1_000_000
    nodes_list = D[1].split("\n")
    paths = {}
    for node in nodes_list:
        start, rl = node.split("=")
        start = start.strip()
        rl = rl.split(",")
        left = rl[0].strip()[1::]
        right = rl[1].strip()[:-1]
        paths[start] = (left, right)

    starting_points = []
    for k in list(paths.keys()):
        if k[-1] == "A":
            starting_points.append(k)

    steps = 0
    seen = set()
    for i in instructions:
        for spi, sp in enumerate(starting_points):
            if sp.endswith("Z"):
                seen.add((sp, steps))
            next_location = paths[sp][directions[i]]
            starting_points[spi] = next_location

        if len(seen) == len(starting_points):
            break

        steps += 1

    numbers = [num for _, num in seen]

    lcm = math.lcm(*numbers)

    print(lcm)


if __name__ == "__main__":
    part2()
