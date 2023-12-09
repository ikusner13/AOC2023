from time import time

D = open(0).read()


def part2():
    lines = D.split("\n\n")

    seeds = [int(x) for x in lines[0].split(":")[1].split()]

    maps = [line.split("\n") for line in lines[1:]]

    seed_ranges = [
        (seeds[i], seeds[i] + seeds[i + 1] - 1) for i in range(0, len(seeds), 2)
    ]

    input_ranges = list(seed_ranges)  # [(79, 92)]  # seed_ranges
    for m in maps[0:5]:
        destination_ranges = []
        mapping_rules = list(map(lambda x: list(map(int, x.split())), m[1::]))
        print(f"map: {m[0]}")
        print(f"inputs: {input_ranges}")
        print("#################")
        for d, s, r in mapping_rules:
            source_range = (s, s + r - 1)
            destination_range = (d, d + r - 1)
            print(
                f"source_range: {source_range} destination_range: {destination_range}"
            )

            for i, input_range in enumerate(input_ranges):
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
                    del input_ranges[i]
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
                    del input_ranges[i]
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
                    del input_ranges[i]

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
                    del input_ranges[i]
                else:
                    print("outside")
            print(" ")

        if len(destination_ranges) == 0 or len(input_ranges) > 0:
            destination_ranges.extend(input_ranges)

        print(f"next: {destination_ranges}")
        input_ranges = list(destination_ranges)

    output = input_ranges
    print(f"output: {min(output, key=lambda x: x[0])[0]}")


if __name__ == "__main__":
    start_time = time()
    part2()
    print(f"--- {time() - start_time} seconds ---")
