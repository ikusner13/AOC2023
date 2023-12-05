from time import time

D = open(0).read()


def part2():
    lines = D.split("\n\n")

    seeds = lines[0].split(":")[1].strip().split()

    maps = list(map(lambda x: x.splitlines(), lines[1::]))

    print(maps)

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

        for rule in mapping_rules:
            print("")
            source_range = (int(rule[1]), int(rule[1]) + int(rule[2]) - 1)
            destination_range = (int(rule[0]), int(rule[0]) + int(rule[2]) - 1)

            print(f"source_range: {source_range}")
            print(f"destination_range: {destination_range}")

            next_ranges = []
            for input_range in input_ranges:
                # if input range is fully contained in source range
                print("fully contained")
                if (
                    input_range[0] >= source_range[0]
                    and input_range[1] <= source_range[1]
                ):
                    range_min = input_range[0] - source_range[0] + destination_range[0]
                    range_max = input_range[1] - source_range[1] + destination_range[1]

                    next_ranges.append((range_min, range_max))
                    break

                # if input range is partially contained in source range
                if (
                    input_range[0] >= source_range[0]
                    and input_range[0] <= source_range[1]
                    and input_range[1] >= source_range[1]
                ):
                    print("partially contained 1")
                    range_min = input_range[0] - source_range[0] + destination_range[0]
                    range_max = destination_range[1]

                    next_ranges.append((range_min, range_max))

                if (
                    input_range[1] >= source_range[0]
                    and input_range[1] <= source_range[1]
                    and input_range[0] <= source_range[0]
                ):
                    print("partially contained 2")
                    range_min = source_range[0]
                    range_max = input_range[1]

                    next_ranges.append((range_min, range_max))

                if len(next_ranges) == 0:
                    next_ranges.append(input_range)

            input_ranges = next_ranges

        print(f"input_ranges: {input_ranges}")

    output = input_ranges[0]

    print(f"output: {output}")
    # for i in range(output[0], output[1] + 1):
    #     print(i)


if __name__ == "__main__":
    start_time = time()
    part2()
    print(f"--- {time() - start_time} seconds ---")
