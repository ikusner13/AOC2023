from time import time
import math


D = open(0).read()
L = D.splitlines()


def part2():
    time_line = L[0].split(":")
    distance_lint = L[1].split(":")

    times = time_line[1].strip().split()
    distances = distance_lint[1].strip().split()

    time = int("".join(times))
    distance = int("".join(distances))

    x1 = (time - math.sqrt(time**2 - 4 * distance)) / 2
    x2 = (time + math.sqrt(time**2 - 4 * distance)) / 2

    x1 = x1 + 1 if x1 == int(x1) else x1
    x2 = x2 - 1 if x2 == int(x2) else x2

    x1_rounded = math.ceil(max(0, x1))
    x2_rounded = math.floor(min(time - 1, x2))

    winning_ways = x2_rounded - x1_rounded + 1

    print(f"winning_ways: {winning_ways}")


if __name__ == "__main__":
    start_time = time()
    part2()
    print(f"Time: {time() - start_time}")
