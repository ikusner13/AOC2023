from itertools import cycle

D = open(0).read().split("\n\n")

directions = {"R": 1, "L": 0}


def part1():
    instructions = D[0]
    paths = {}
    for node in D[1].split("\n"):
        start, rl = node.split("=")
        left, right = [x.strip().strip("()") for x in rl.split(",")]
        paths[start.strip()] = (left, right)

    current_location = "AAA"
    steps = 0
    # TODO: instead of cycling instructions, check for a cycle in the navigation
    for i in cycle(instructions):
        current_location = paths[current_location][directions[i]]
        steps += 1

        if current_location == "ZZZ":
            return steps

    return steps


if __name__ == "__main__":
    print(part1())
