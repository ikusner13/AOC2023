from time import time

D = open(0).read()


def part2():
    lines = D.split("\n\n")

    seeds = lines[0].split(":")[1].strip().split()

    maps = list(map(lambda x: x.splitlines(), lines[1::]))

    def create_seed_ranges(seeds):
        seed_ranges = []
        for i in range(0, len(seeds), 2):
            seed_ranges.append((int(seeds[i]), int(seeds[i]) + int(seeds[i + 1]) - 1))

        return seed_ranges

    seed_ranges = create_seed_ranges(seeds)

    input_ranges = list(seed_ranges)  # [(79, 92)]  # seed_ranges
    for m in maps[0:7]:
        destination_ranges = list(input_ranges)
        mapping_rules = list(map(lambda x: x.split(), m[1::]))
        print(f"map: {m[0]}")
        print("#################")

        for rule in mapping_rules:
            source_range = (int(rule[1]), int(rule[1]) + int(rule[2]) - 1)
            destination_range = (int(rule[0]), int(rule[0]) + int(rule[2]) - 1)

            for input_range in input_ranges:
                # fully outside
                if input_range[0] > source_range[1] or input_range[1] < source_range[0]:
                    # destination_ranges.append((input_range[0], input_range[1]))
                    continue

                if input_range[0] < source_range[0]:
                    destination_start = destination_range[0]
                    destination_end = destination_range[1] + (
                        input_range[1] - source_range[1]
                    )
                    assert destination_start > 0 and destination_end > 0
                    destination_ranges.append((destination_start, destination_end))

                if input_range[1] > source_range[1]:
                    destination_start = destination_range[0] + (
                        input_range[0] - source_range[0]
                    )
                    destination_end = destination_range[1]
                    print(f"start: {destination_start}")
                    print(f"end: {destination_end}")
                    assert destination_start > 0 and destination_end > 0
                    destination_ranges.append((destination_start, destination_end))

                if (
                    input_range[0] >= source_range[0]
                    and input_range[1] <= source_range[1]
                ):
                    destination_start = destination_range[0] + (
                        input_range[0] - source_range[0]
                    )
                    destination_end = destination_range[1] + (
                        input_range[1] - source_range[1]
                    )
                    assert destination_start > 0 and destination_end > 0

                    destination_ranges.append((destination_start, destination_end))

                    if input_range in destination_ranges:
                        destination_ranges.remove(input_range)
        if len(destination_ranges) == 0:
            destination_ranges.extend(input_ranges)

        input_ranges = list(destination_ranges)

    output = input_ranges
    print(f"output: {min(output, key=lambda x: x[0])[0]}")


if __name__ == "__main__":
    start_time = time()
    part2()
    print(f"--- {time() - start_time} seconds ---")
