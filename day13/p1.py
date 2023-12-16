D = open(0).read().split("\n\n")

"""
plan:

find a horizontal or vertical reflection in each pattern
  - for a horizontal reflection see if row i and i+1 are the same
   - if so, verify that each pair of columns left and right are the same
   - if reflection found at 4, check pairs ()
  - for a vertical reflection see if column i and i+1 are the same
   - if so, verify that each pair of rows above and below are the same

add up columns to the left of the vertical reflection
add up rows above (less than) the horizontal reflection * 100

"""


def part1():
    def find_vertical_reflection(pattern):
        rows, cols = len(pattern), len(pattern[0])

        for i in range(cols - 1):
            if all(pattern[r][i] == pattern[r][i + 1] for r in range(rows)):
                for j in range(1, min(i + 1, cols - (i + 1))):
                    if any(
                        pattern[r][i + j + 1] != pattern[r][i - j] for r in range(rows)
                    ):
                        break
                else:
                    return i + 1
        return 0

    def find_horizontal_reflection(pattern):
        height = len(pattern)

        for i, row in enumerate(pattern[:-1]):
            if row == pattern[i + 1]:
                for j in range(1, min(i + 1, height - (i + 1))):
                    if any(a != b for a, b in zip(pattern[i + j + 1], pattern[i - j])):
                        break
                else:
                    return (i + 1) * 100

        return 0

    print(
        sum(
            find_horizontal_reflection(lines) + find_vertical_reflection(lines)
            for p in D
            for lines in [p.splitlines()]
        )
    )


if __name__ == "__main__":
    part1()
