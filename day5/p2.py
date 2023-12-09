from time import time

D = open(0).read()


def part2():
    lines = D.split("\n\n")

    seeds = [int(x) for x in lines[0].split(":")[1].split()]

    maps = [line.split("\n") for line in lines[1:]]

    seed_ranges = [
        (seeds[i], seeds[i] + seeds[i + 1] - 1) for i in range(0, len(seeds), 2)
    ]

    input_ranges = list(seed_ranges)
    for m in maps[0:7]:
        mapping_rules = [[int(x) for x in rule.split()] for rule in m[1::]]
        new_inputs = []

        while input_ranges:
            input_range_start, input_range_end = input_ranges.pop(0)
            for d, s, r in mapping_rules:
                source_range = (s, s + r - 1)
                destination_range = (d, d + r - 1)

                if (
                    input_range_end < source_range[0]
                    or input_range_start > source_range[1]
                ):
                    continue  # No overlap

                if (
                    input_range_start <= source_range[1]
                    and input_range_end >= source_range[0]
                ):
                    # Overlap exists
                    start_offset = input_range_start - source_range[0]
                    if start_offset < 0:
                        start_offset = 0

                    end_offset = input_range_end - source_range[1]
                    if end_offset > 0:
                        end_offset = 0

                    new_inputs.append(
                        (
                            destination_range[0] + start_offset,
                            destination_range[1] + end_offset,
                        )
                    )

                    # new outside ranges need to go through map
                    if input_range_start < source_range[0]:
                        input_ranges.append((input_range_start, source_range[0] - 1))
                    if input_range_end > source_range[1]:
                        input_ranges.append((source_range[1] + 1, input_range_end))
                    break
            else:  # break was not encountered (no overlap on any rule)
                new_inputs.append((input_range_start, input_range_end))

        # set inputs for next map section
        input_ranges = new_inputs

    print(f"output: {min(input_ranges, key=lambda x: x[0])[0]}")


if __name__ == "__main__":
    start_time = time()
    part2()
    print(f"--- {time() - start_time} seconds ---")
