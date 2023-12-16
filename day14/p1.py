D = open(0).read().splitlines()


def part1():
    total_sum = 0
    for i in range(len(D)):
        if i == 0:
            continue
        for ji, j in enumerate(D[i]):
            if j == "O":
                move_to = i - 1
                while D[move_to][ji] == "." and move_to >= 0:
                    D[move_to] = D[move_to][:ji] + "O" + D[move_to][ji + 1 :]
                    D[move_to + 1] = (
                        D[move_to + 1][:ji] + "." + D[move_to + 1][ji + 1 :]
                    )

                    move_to -= 1
    length = len(D)
    total_sum += sum(row.count("O") * (length - i) for i, row in enumerate(D))

    print(total_sum)


if __name__ == "__main__":
    part1()
