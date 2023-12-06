from time import time
import math


D = open(0).read()
L = D.splitlines()


def part1():
    time_line = L[0].split(":")
    distance_lint = L[1].split(":")

    times = time_line[1].strip().split()
    distances = distance_lint[1].strip().split()

    time = int("".join(times))
    distance = int("".join(distances))

    print(time)
    print(distance)

    product = 1
    w = 0
    for x in range(time + 1):
        if x * (time - x) > distance:
            w += 1

    print(f"Number of ways to win: {w}")
    product *= w

    print(f"Product: {product}")


if __name__ == "__main__":
    start_time = time()
    part1()
    print(f"Time: {time() - start_time}")
