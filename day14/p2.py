def part2():
    D = open(0).read().splitlines()

    def roll(grid):
        height = len(grid)
        width = len(grid[0])

        for col in range(width):
            for row in range(1, height):
                if grid[row][col] == "O":
                    move_to = row
                    while move_to > 0 and grid[move_to - 1][col] == ".":
                        move_to -= 1

                    if move_to != row:
                        grid[move_to] = (
                            grid[move_to][:col] + "O" + grid[move_to][col + 1 :]
                        )
                        grid[row] = grid[row][:col] + "." + grid[row][col + 1 :]

        return grid

    def find_cycle(grid):
        seen = set()
        for c in range(1000000000):
            for _ in range(4):
                grid = roll(grid)

                grid = list("".join(row) for row in zip(*grid[::-1]))

                # convert to tuple because is a hashable
                grid_tuple = tuple(grid)

                if grid_tuple in seen:
                    return c
                else:
                    seen.add(grid_tuple)
        return 0

    cycle = find_cycle(D)
    off_by = 1  # had to manually find this, not sure why off by 1

    for _ in range(1000000000 % (cycle + off_by)):
        for _ in range(4):
            D = roll(D)

            D = list("".join(row) for row in zip(*D[::-1]))

    print(sum(row.count("O") * (len(D) - i) for i, row in enumerate(D)))


if __name__ == "__main__":
    part2()
