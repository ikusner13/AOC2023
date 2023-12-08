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
    print(starting_points)

    steps = 0
    seen = []
    for i in instructions:
        if len(seen) == len(starting_points):
            break
        if all(point.endswith("Z") for point in starting_points):
            break
        for spi, sp in enumerate(starting_points):
            next_location = paths[sp][directions[i]]
            if next_location.endswith("Z"):
                seen.append(sp)
            starting_points[spi] = next_location

        steps += 1

    print(steps)
    print(seen)


if __name__ == "__main__":
    part2()
