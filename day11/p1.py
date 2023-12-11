D = open(0).read().splitlines()


def part1():
    # find empty rows and columns
    empty_rows = set()
    empty_cols = set()
    for c in range(0, len(D)):
        for r in range(0, len(D[c])):
            if D[c][r] == "#":
                break
        else:
            empty_rows.add(c)

        for r in range(0, len(D[c])):
            if D[r][c] == "#":
                break
        else:
            empty_cols.add(c)

    """
    # add an extra row and column to the grid for each empty row and column
    for ri, row in enumerate(empty_rows):
        D.insert(ri, "." * len(D[0]))
    for c in empty_cols:
        for r in range(0, len(D)):
            new_row = D[r][:c] + "." + D[r][c:]
            D[r] = new_row

    print(empty_rows)
    print(empty_cols)
    print(D)
    """

    print(empty_cols)
    print(empty_rows)
    galaxy_pairs = set()
    found_galaxies = 0
    for r, row in enumerate(D):
        for c, col in enumerate(row):
            if col == "#" and (r, c) not in galaxy_pairs:
                found_galaxies += 1
                rows_to_add = sum(1 for row in empty_rows if r > row)
                cols_to_add = sum(1 for col in empty_cols if c > col)

                galaxy_pairs.add((r + rows_to_add, c + cols_to_add))

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
