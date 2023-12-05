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
                    "source_end": source_start + range_length,
                    "destination_start": destination_start,
                    "destination_end": destination_start + range_length,
                }
            )

        return ranges

    seed_to_soil_range = create_range(seed_to_soil)

    def get_destination(seed, range):
        seed = int(seed)
        for m in range:
            if seed >= m["source_start"] and seed < m["source_end"]:
                seed_destination = seed - m["source_start"] + m["destination_start"]
                return seed_destination
        return seed

    locations = []
    for seed in seeds:
        soil = get_destination(seed, seed_to_soil_range)
        fertilizer = get_destination(soil, create_range(soil_to_fertilizer))
        water = get_destination(fertilizer, create_range(fertilizer_to_water))
        light = get_destination(water, create_range(water_to_light))
        temperature = get_destination(light, create_range(light_to_temperature))
        humidity = get_destination(temperature, create_range(temperature_to_humidity))
        location = get_destination(humidity, create_range(humidity_to_location))
        locations.append(location)

    print(min(locations))


if __name__ == "__main__":
    start_time = time()
    part2()
    print(f"--- {time() - start_time} seconds ---")
