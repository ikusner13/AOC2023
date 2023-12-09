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
    for m in maps[0:7]:
        mapping_rules = list(map(lambda x: list(map(int, x.split())), m[1::]))
        destination_ranges = []
        while input_ranges:
            input_range = input_ranges.pop(0)
            for d, s, r in mapping_rules:
                source_range = (s, s + r - 1)
                destination_range = (d, d + r - 1)
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
                    break

                elif (
                    input_range[0] < source_range[0]
                    and input_range[1] > source_range[1]
                ):
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
                    break
                elif (
                    input_range[0] >= source_range[0]
                    and input_range[0] < source_range[1]
                ):
                    # inside
                    start_offset = input_range[0] - source_range[0]
                    destination_ranges.append(
                        (destination_range[0] + start_offset, destination_range[1])
                    )

                    # outside
                    input_ranges.append((source_range[1] + 1, input_range[1]))
                    break

                elif (
                    input_range[1] >= source_range[0]
                    and input_range[1] <= source_range[1]
                ):
                    end_offset = input_range[1] - source_range[1]
                    # inside
                    destination_ranges.append(
                        (destination_range[0], destination_range[1] + end_offset)
                    )

                    # outside
                    input_ranges.append((input_range[0], source_range[0] - 1))
                    break

            else:
                destination_ranges.append((input_range[0], input_range[1]))
        input_ranges = destination_ranges

    output = input_ranges
    print(f"output: {min(output, key=lambda x: x[0])[0]}")


if __name__ == "__main__":
    start_time = time()
    part2()
    print(f"--- {time() - start_time} seconds ---")
