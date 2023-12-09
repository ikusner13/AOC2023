D = open(0).read().splitlines()


def part1():
    lines = lines = [list(map(int, x.split())) for x in D]

    differences = []
    for line in lines:
        d = [line]
        while d[-1].count(0) < len(d[-1]):
            d.append([d[-1][r + 1] - d[-1][r] for r in range(0, len(d[-1]) - 1)])

        for i in range(1, len(d) + 1):
            if i == 1:
                d[-i].append(0)
            else:
                d[-i].append(d[-i][-1] + d[-i + 1][-1])

        differences.append(d)

    print(sum([l[0][-1] for l in differences]))


if __name__ == "__main__":
    part1()
