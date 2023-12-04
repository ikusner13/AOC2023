# Combining solutions for both Part 1 and Part 2

def analyze_games_combined(games_data, red_limit, green_limit, blue_limit):
    def game_info_parser(game_info):
        sets_of_cubes = game_info.split("; ")
        min_red, min_green, min_blue, possible = 0, 0, 0, True

        for cube_set in sets_of_cubes:
            red_count = green_count = blue_count = 0

            for cube_info in cube_set.split(", "):
                count, color = cube_info.split(" ")
                if color.startswith("red"):
                    red_count = int(count)
                elif color.startswith("green"):
                    green_count = int(count)
                elif color.startswith("blue"):
                    blue_count = int(count)

            min_red = max(min_red, red_count)
            min_green = max(min_green, green_count)
            min_blue = max(min_blue, blue_count)

            # Check if the game is possible with the given limits
            if red_count > red_limit or green_count > green_limit or blue_count > blue_limit:
                possible = False

        return min_red, min_green, min_blue, possible

    possible_game_ids = []
    total_power = 0

    for game in games_data.split("\n"):
        game_id, game_info = game.split(": ")
        min_red, min_green, min_blue, possible = game_info_parser(game_info)

        if possible:
            possible_game_ids.append(int(game_id.split(" ")[1]))

        total_power += min_red * min_green * min_blue

    possible_games_sum = sum(possible_game_ids)
    return possible_games_sum, total_power

games_data = open(0).read()

# Example games data
combined_result = analyze_games_combined(games_data.strip(), 12, 13, 14)

print(combined_result)
