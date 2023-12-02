# Calculating the minimum set of cubes required for each game and summing their powers

def min_cubes_power(game_data):
    # Split the data into individual sets of revealed cubes
    sets_of_cubes = game_data.split("; ")

    min_red, min_green, min_blue = 0, 0, 0

    # Determine the minimum number of each color cube required
    for cube_set in sets_of_cubes:
        red_count = green_count = blue_count = 0

        # Count the number of each color cube in the set
        for cube_info in cube_set.split(", "):
            count, color = cube_info.split(" ")
            if color.startswith("red"):
                red_count = int(count)
            elif color.startswith("green"):
                green_count = int(count)
            elif color.startswith("blue"):
                blue_count = int(count)

        # Update the minimum count if this set has more cubes of a certain color
        min_red = max(min_red, red_count)
        min_green = max(min_green, green_count)
        min_blue = max(min_blue, blue_count)

    return min_red * min_green * min_blue

def sum_of_powers_of_min_cubes(games_data):
    total_power = 0
    for game in games_data.split("\n"):
        _, game_info = game.split(": ")
        total_power += min_cubes_power(game_info)

    return total_power


games_data = open(0).read()

# Summing the powers of the minimum sets of cubes for the example games
print(sum_of_powers_of_min_cubes(games_data.strip()))
