D = open(0).read().splitlines()


def part1():
    for line in D:
        condition, arrangement_groups = line.split()
        arrangement_groups = tuple(map(int, arrangement_groups.split(",")))


if __name__ == "__main__":
    part1()
