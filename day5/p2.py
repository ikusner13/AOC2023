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
    print(seed_ranges)

    input_ranges = list(seed_ranges)  # [(79, 92)]  # seed_ranges
    for m in maps[0:5]:
        destination_ranges = []
        mapping_rules = list(map(lambda x: x.split(), m[1::]))
        print(f"map: {m[0]}")
        print(f"inputs: {input_ranges}")
        print("#################")
        for rule in mapping_rules:
            source_range = (int(rule[1]), int(rule[1]) + int(rule[2]) - 1)
            destination_range = (int(rule[0]), int(rule[0]) + int(rule[2]) - 1)
            print(
                f"source_range: {source_range} destination_range: {destination_range}"
            )

            for input_range in input_ranges:
                print(f"input_range: {input_range}")
                if (
                    input_range[0] >= source_range[0]
                    and input_range[1] <= source_range[1]
                ):
                    start_offset = input_range[0] - source_range[0]
                    end_offset = input_range[1] - source_range[1]
                    destination_ranges.append(
                        (
                            destination_range[0] + start_offset,
                            destination_range[1] + end_offset,
                        )
                    )
                    print("full in")
                elif (
                    input_range[0] < source_range[0]
                    and input_range[1] > source_range[1]
                ):
                    print("full in and overlap")
                    # full in
                    destination_ranges.append(
                        (destination_range[0], destination_range[1])
                    )

                    # left out
                    # right out
                    input_ranges.extend(
                        [
                            (source_range[1] + 1, input_range[1]),
                            (input_range[0], source_range[0] - 1),
                        ]
                    )
                elif (
                    input_range[0] >= source_range[0]
                    and input_range[0] < source_range[1]
                ):
                    print(f"overlap start in")
                    # inside
                    start_offset = input_range[0] - source_range[0]
                    destination_ranges.append(
                        (destination_range[0] + start_offset, destination_range[1])
                    )

                    # outside
                    input_ranges.append((source_range[1] + 1, input_range[1]))

                elif (
                    input_range[1] >= source_range[0]
                    and input_range[1] <= source_range[1]
                ):
                    print("overlap end in")
                    end_offset = input_range[1] - source_range[1]
                    # inside
                    destination_ranges.append(
                        (destination_range[0], destination_range[1] + end_offset)
                    )

                    # outside
                    input_ranges.append((input_range[0], source_range[0] - 1))
                else:
                    print("outside")

            print(f"dest: {destination_ranges}")

        if len(destination_ranges) == 0:
            print("empty destination range")
            destination_ranges.extend(input_ranges)

        input_ranges = list(destination_ranges)

    output = input_ranges
    print(f"output: {output}")


if __name__ == "__main__":
    start_time = time()
    part2()
    print(f"--- {time() - start_time} seconds ---")
