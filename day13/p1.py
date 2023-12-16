D = open(0).read().split("\n\n")


def part1():
    def find_horizontal_reflection(pattern):
        height = len(pattern)

        for i, row in enumerate(pattern[:-1]):
            if row == pattern[i + 1]:
                for j in range(1, min(i + 1, height - (i + 1))):
                    if any(a != b for a, b in zip(pattern[i + j + 1], pattern[i - j])):
                        break
                else:
                    return i + 1

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
