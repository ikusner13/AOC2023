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

    input_ranges = seed_ranges
    for m in maps:
        print("")
        mapping_rules = list(map(lambda x: x.split(), m[1::]))
        print(f"map: {m[0]}")
        print("#################")

        next_ranges = set()
        for i, input_range in enumerate(input_ranges):
            in_range = False
            range_start = input_range[0]
            range_end = input_range[1]

            for rule in mapping_rules:
                source_range = (int(rule[1]), int(rule[1]) + int(rule[2]) - 1)
                destination_range = (int(rule[0]), int(rule[0]) + int(rule[2]) - 1)

                # fully contained
                if range_start >= source_range[0] and range_end <= source_range[1]:
                    in_range = True
                    destination_range_start = (
                        range_start - source_range[0] + destination_range[0]
                    )
                    destination_range_end = (
                        range_end - source_range[1] + destination_range[1]
                    )

                    next_ranges.add((destination_range_start, destination_range_end))

                # partially contained
                if (
                    range_start < source_range[0]
                    and range_end < source_range[1]
                    and range_end >= source_range[0]
                ):
                    in_range = True
                    destination_range_start = destination_range[0]
                    destination_range_end = destination_range[1] - (
                        source_range[1] - range_end
                    )
                    next_ranges.add((destination_range_start, destination_range_end))

                    new_range_start = range_start
                    new_range_end = source_range[0] - 1

                    input_ranges.append((new_range_start, new_range_end))

            if len(next_ranges) == 0 or not in_range:
                next_ranges.add((range_start, range_end))

        input_ranges = list(next_ranges)

    print(f"min: {min(input_ranges, key=lambda x: x[0])[0]}")


if __name__ == "__main__":
    start_time = time()
    part2()
    print(f"--- {time() - start_time} seconds ---")
