D = open(0).read().splitlines()


def part1():
    lines = lines = [list(map(int, x.split())) for x in D]

    differences = []
    for line in lines:
        row = []
        for i, step in enumerate(line):
            if i == len(line) - 1:
                break
            row.append(line[i + 1] - step)

        diffs = []
        c = list(row)
        while c.count(0) < len(c):
            c = [c[d + 1] - c[d] for d in range(0, len(c) - 1)]
            diffs.append(c)

        diffs.insert(0, row)
        diffs.insert(0, line)
        for i, item in enumerate(reversed(diffs)):
            if i == 0:
                item.append(0)
                continue
            item.append(item[-1] + list(reversed(diffs))[i - 1][-1])
        differences.append(diffs)

    print(sum([l[0][-1] for l in differences]))


if __name__ == "__main__":
    part1()
