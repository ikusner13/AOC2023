from time import time

D = open(0).read()


def part2():
    lines = D.split("\n\n")

    seeds = lines[0].split(":")[1].strip().split()

    seed_to_soil = lines[1].splitlines()

    soil_to_fertilizer = lines[2].splitlines()

    fertilizer_to_water = lines[3].splitlines()

    water_to_light = lines[4].splitlines()

    light_to_temperature = lines[5].splitlines()

    temperature_to_humidity = lines[6].splitlines()

    humidity_to_location = lines[7].splitlines()

    def create_range(lines):
        ranges = []

        for line in lines[1::]:
            types = line.split()
            destination_start = int(types[0])
            source_start = int(types[1])
            range_length = int(types[2])

            ranges.append(
                {
                    "source_start": source_start,
                    "source_end": source_start + range_length - 1,
                    "destination_start": destination_start,
                    "destination_end": destination_start + range_length - 1,
                }
            )

        return ranges

    def create_seed_ranges(seeds):
        seed_ranges = []
        for i in range(0, len(seeds), 2):
            seed_ranges.append((seeds[i], seeds[i + 1]))

        return seed_ranges

    def is_in_range(start, end, source):
        print(f"start: {start}, end: {end}, source: {source}")
        return start >= source["source_start"] and start <= source["source_end"]

    def get_destination_range(input_num, input_range_length, rs):
        print(f"input_num: {input_num}, input_range_length: {input_range_length}")
        for r in rs:
            if is_in_range(input_num, input_num + input_range_length, r):
                print(
                    f"seed {input_num} is in range {r['source_start']} - {r['source_end']}"
                )
                destination_range_length = r["source_end"] - r["source_start"] + 1
                destination = (
                    r["destination_start"],
                    destination_range_length,
                    input_num - r["source_start"] + r["destination_start"],
                )
                print(f"destination: {destination}")
                return destination

        return (input_num, input_range_length, input_num)

    seed_ranges = create_seed_ranges(seeds)

    locations = []
    for seed_range in seed_ranges:
        print(f"seed_range: {seed_range}")
        start_num = int(seed_range[0])
        seed_range_length = int(seed_range[1])

        seed_to_soil_ranges = create_range(seed_to_soil)

        soil_destination_range = get_destination_range(
            start_num, seed_range_length, seed_to_soil_ranges
        )

        print(f"soil_destination range: {soil_destination_range}")
        print("")

        soil_to_fertilizer_ranges = create_range(soil_to_fertilizer)

        fertilizer_destination_range = get_destination_range(
            soil_destination_range[2],
            soil_destination_range[0]
            + soil_destination_range[1]
            - soil_destination_range[2]
            - 1,
            soil_to_fertilizer_ranges,
        )

        print(f"fertilizer_destination range: {fertilizer_destination_range}")
        print("")

        fertilizer_to_water_ranges = create_range(fertilizer_to_water)

        water_destination_range = get_destination_range(
            fertilizer_destination_range[2],
            fertilizer_destination_range[0]
            + fertilizer_destination_range[1]
            - fertilizer_destination_range[2]
            - 1,
            fertilizer_to_water_ranges,
        )

        print(f"water_destination range: {water_destination_range}")
        print("")

        water_to_light_ranges = create_range(water_to_light)

        light_destination_range = get_destination_range(
            water_destination_range[2],
            water_destination_range[0]
            + water_destination_range[1]
            - water_destination_range[2]
            - 1,
            water_to_light_ranges,
        )

        print(f"light_destination range: {light_destination_range}")
        print("")

        light_to_temperature_ranges = create_range(light_to_temperature)

        temperature_destination_range = get_destination_range(
            light_destination_range[2],
            light_destination_range[0]
            + light_destination_range[1]
            - light_destination_range[2]
            - 1,
            light_to_temperature_ranges,
        )

        print(f"temperature_destination range: {temperature_destination_range}")
        print("")

        temperature_to_humidity_ranges = create_range(temperature_to_humidity)

        humidity_destination_range = get_destination_range(
            temperature_destination_range[2],
            temperature_destination_range[0]
            + temperature_destination_range[1]
            - temperature_destination_range[2]
            - 1,
            temperature_to_humidity_ranges,
        )

        print(f"humidity_destination range: {humidity_destination_range}")
        print("")

        humidity_to_location_ranges = create_range(humidity_to_location)

        location_destination_range = get_destination_range(
            humidity_destination_range[2],
            humidity_destination_range[0]
            + humidity_destination_range[1]
            - humidity_destination_range[2]
            - 1,
            humidity_to_location_ranges,
        )

        print(f"location_destination range: {location_destination_range}")
        locations.append(location_destination_range[2])

    print(min(locations))


if __name__ == "__main__":
    start_time = time()
    part2()
    print(f"--- {time() - start_time} seconds ---")
