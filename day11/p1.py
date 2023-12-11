D = open(0).read().splitlines()


def part1():
    # find empty rows and columns
    empty_rows = {r for r in range(len(D)) if all(cell != "#" for cell in D[r])}
    empty_cols = {
        c for c in range(len(D[0])) if all(D[r][c] != "#" for r in range(len(D)))
    }

    galaxy_pairs = set()
    for r, row in enumerate(D):
        for c, col in enumerate(row):
            if col == "#":
                row_offset = sum(1 for row in empty_rows if r > row)
                col_offset = sum(1 for col in empty_cols if c > col)

                galaxy_pairs.add((r + row_offset, c + col_offset))

    # find the shortest distance between each galaxy pair
    distances = {}
    for galaxy in galaxy_pairs:
        for galaxy2 in galaxy_pairs:
            if galaxy == galaxy2:
                continue

            if (galaxy2, galaxy) in distances or (galaxy, galaxy2) in distances:
                continue

            x_distance = abs(galaxy[0] - galaxy2[0])
            y_distance = abs(galaxy[1] - galaxy2[1])

            distances[(galaxy, galaxy2)] = x_distance + y_distance

    print(sum(distances.values()))


if __name__ == "__main__":
    part1()
