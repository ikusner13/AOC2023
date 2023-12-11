from itertools import combinations


D = open(0).read().splitlines()

expansion = 1_000_000


def part2():
    empty_rows = {r for r in range(len(D)) if all(cell != "#" for cell in D[r])}
    empty_cols = {
        c for c in range(len(D[0])) if all(D[r][c] != "#" for r in range(len(D)))
    }

    galaxy_pairs = {
        (
            # -1 because we don't want to count the empty rows/cols in the expansion
            r + sum(map(lambda row: r > row, empty_rows)) * (expansion - 1),
            c + sum(map(lambda col: c > col, empty_cols)) * (expansion - 1),
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
    part2()
