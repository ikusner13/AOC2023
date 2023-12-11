from itertools import combinations


D = open(0).read().splitlines()


def part1():
    empty_rows = {r for r in range(len(D)) if all(cell != "#" for cell in D[r])}
    empty_cols = {
        c for c in range(len(D[0])) if all(D[r][c] != "#" for r in range(len(D)))
    }

    galaxy_pairs = {
        (
            r + sum(map(lambda row: r > row, empty_rows)),
            c + sum(map(lambda col: c > col, empty_cols)),
        )
        for r, row in enumerate(D)
        for c, char in enumerate(row)
        if char == "#"
    }

    print(
        sum(
            abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
            for g1, g2 in combinations(galaxy_pairs, 2)
        )
    )


if __name__ == "__main__":
    part1()
