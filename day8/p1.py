D = open(0).read().split("\n\n")

directions = {"R": 1, "L": 0}


def part1():
    instructions = D[0] * 60
    nodes_list = D[1].split("\n")
    paths = {}
    for node in nodes_list:
        start, rl = node.split("=")
        start = start.strip()
        rl = rl.split(",")
        left = rl[0].strip()[1::]
        right = rl[1].strip()[:-1]
        paths[start] = (left, right)

    current_location = "AAA"
    steps = 0
    for i in instructions:
        next_location = paths[current_location][directions[i]]
        current_location = next_location
        steps += 1

        if current_location == "ZZZ":
            break

    print(steps)


if __name__ == "__main__":
    part1()
