D = open(0).read().split("\n\n")


def part1():
    def find_horizontal_reflection(pattern):
        for i in range(1, len(pattern)):
            if (
                sum(
                    1
                    for j in range(min(i, len(pattern) - i))
                    for a, b in zip(pattern[i - 1 - j], pattern[i + j])
                    if a != b
                )
                == 1
            ):
                return i

        return 0

    print(
        sum(
            (find_horizontal_reflection(lines) * 100)
            + find_horizontal_reflection(list(zip(*lines)))
            for p in D
            for lines in [p.splitlines()]
        )
    )


if __name__ == "__main__":
    part1()
