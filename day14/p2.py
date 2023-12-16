D = open(0).read().splitlines()


def part1():
    total_sum = 0

    def roll(grid):
        for i in range(len(grid)):
            if i == 0:
                continue
            for ji, j in enumerate(grid[i]):
                if j == "O":
                    move_to = i - 1
                    while grid[move_to][ji] == "." and move_to >= 0:
                        grid[move_to] = (
                            grid[move_to][:ji] + "O" + grid[move_to][ji + 1 :]
                        )
                        grid[move_to + 1] = (
                            grid[move_to + 1][:ji] + "." + grid[move_to + 1][ji + 1 :]
                        )

                        move_to -= 1
        return grid

    # North
    n = roll(D)

    print("rolled north")
    print("\n".join(n))
    print(" ")

    print("rotated west")
    print("\n".join(["".join(row) for row in zip(*n[::-1])]))
    print(" ")

    # West
    w = roll(["".join(row) for row in zip(*n[::-1])])

    print("rolled west")
    print("\n".join(w))
    print(" ")

    print("rotated south")
    print("\n".join([row for row in w[::-1]]))
    print(" ")

    # South
    s = roll([row for row in w[::-1]])

    print("rolled south")
    print("\n".join(s))
    print(" ")

    print("rotated east")
    print("\n".join(["".join(row) for row in zip(*s)][::-1]))
    print(" ")
    # East
    e = roll(["".join(row) for row in zip(*s)][::-1])

    print("rolled east")
    print("\n".join(e))
    print(" ")

    length = len(e)
    total_sum += sum(row.count("O") * (length - i) for i, row in enumerate(e))

    print(total_sum)


if __name__ == "__main__":
    part1()
