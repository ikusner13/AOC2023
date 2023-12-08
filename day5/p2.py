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

    input_ranges = [(74, 87)]  # seed_ranges
    destination_ranges = []
    for m in [maps[4]]:
        mapping_rules = list(map(lambda x: x.split(), m[1::]))
        print(f"map: {m[0]}")
        print("#################")

        for rule in mapping_rules:
            print(f"rule: {rule}")
            source_range = (int(rule[1]), int(rule[1]) + int(rule[2]) - 1)
            destination_range = (int(rule[0]), int(rule[0]) + int(rule[2]) - 1)

            next_ranges = []
            print(f"input_ranges: {input_ranges}")
            print(f"source_range: {source_range}")
            print("-" * 20)
            for input_range in input_ranges:
                print(f"input range: {input_range}")
                """
                # fully outside
                if input_range[0] > source_range[1] or input_range[1] < source_range[0]:
                    print("fully outside\n")
                    # destination_ranges.append((input_range[0], input_range[1]))
                    continue

                # if input range is fully contained in source range
                elif (
                    input_range[0] >= source_range[0]
                    and input_range[1] <= source_range[1]
                ):
                    print("fully inside\n")
                    destination_start = destination_range[0] + (
                        input_range[0] - source_range[0]
                    )
                    destination_end = destination_range[1] + (
                        input_range[1] - source_range[1]
                    )
                    destination_ranges.append((destination_start, destination_end))
                    continue
                """

                # partially contained
                if (
                    input_range[1] > source_range[0]
                    and input_range[1] < source_range[1]
                    and input_range[0] < source_range[0]
                ):
                    print("partial 1")
                    # split into 2 groups
                    # outside group
                    next_ranges.append((input_range[0], source_range[0] - 1))

                    # inside group
                    next_ranges.append((source_range[0], input_range[1]))

                elif (
                    input_range[0] < source_range[1]
                    and input_range[1] > source_range[1]
                    and input_range[0] > source_range[0]
                ):
                    print("partial 2")
                    # outside group
                    next_ranges.append((source_range[1] + 1, input_range[1]))

                    # inside group
                    next_ranges.append((input_range[0], source_range[1]))
                elif (
                    input_range[0] < source_range[0]
                    and input_range[1] > source_range[1]
                ):
                    print("partial 3")
                    # outside left group
                    next_ranges.append((input_range[0], source_range[0] - 1))

                    # contained group
                    next_ranges.append((source_range[0], source_range[1]))

                    # outside right group
                    next_ranges.append((source_range[1] + 1, input_range[1]))

                print(f"next ranges: {next_ranges}\n")

                # input_ranges.extend(next_ranges)

        input_ranges = destination_ranges
        print(f"new input ranges: {input_ranges}")
        print("")

    output = input_ranges

    print(f"output: {output}")


if __name__ == "__main__":
    start_time = time()
    part2()
    print(f"--- {time() - start_time} seconds ---")
