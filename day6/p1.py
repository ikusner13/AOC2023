from time import time
import math


D = open(0).read()
L = D.splitlines()


def part1():
    time_line = L[0].split(":")
    distance_lint = L[1].split(":")

    times = time_line[1].strip().split()
    distances = distance_lint[1].strip().split()

    product = 1
    for i in range(len(times)):
        # wait table for 7 ms time:
        # 0 ms: 0 mm/ms
        # 1 ms: 1 mm/ms * 6ms (7-1) = 6 mm
        # 2 ms: 2 mm/ms * 5ms (7-2) = 10 mm (answer)
        # 3 ms: 3 mm/ms * 4ms (7-3) = 12 mm (answer)
        # 4 ms: 4 mm/ms * 3ms (7-4) = 12 mm (answer)
        # 5 ms: 5 mm/ms * 2ms (7-5) = 10 mm (answer)
        # 6 ms: 6 mm/ms * 1ms (7-6) = 6 mm
        # 7 ms: 7 mm/ms * 0ms (7-7) = 0 mm

        # equation: x(t-x) > d
        # x^2 - xt + d < 0
        # x = (t +- sqrt(t^2 - 4d)) / 2
        # x = (t +- sqrt(t^2 - 4d)) / 2
        # x = (t + sqrt(t^2 - 4d)) / 2

        time = int(times[i])
        distance = int(distances[i])

        x1 = (time - math.sqrt(time**2 - 4 * distance)) / 2
        x2 = (time + math.sqrt(time**2 - 4 * distance)) / 2

        x1 = x1 + 1 if x1 == int(x1) else x1
        x2 = x2 - 1 if x2 == int(x2) else x2

        x1_rounded = math.ceil(max(0, x1))
        x2_rounded = math.floor(min(time - 1, x2))

        winning_range = x2_rounded - x1_rounded + 1

        print(f"winning_range: {winning_range}")
        product *= winning_range

    print(f"Product: {product}")


if __name__ == "__main__":
    start_time = time()
    part1()
    print(f"Time: {time() - start_time}")
