D = open(0).read().splitlines()


def part2():
    lines = lines = [list(map(int, x.split())) for x in D]

    differences = []
    for line in lines:
        d = [line]
        while d[-1].count(0) < len(d[-1]):
            d.append([d[-1][r + 1] - d[-1][r] for r in range(0, len(d[-1]) - 1)])

        for i, item in enumerate(d[::-1]):
            if i == 0:
                item.insert(0, 0)
            else:
                item.insert(0, (item[0] - d[::-1][i - 1][0]))

        differences.append(d)

    print(sum([l[0][0] for l in differences]))


if __name__ == "__main__":
    part2()
