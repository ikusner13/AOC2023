from collections import defaultdict
from time import time
import sys


D = open(0).read()

"""
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
"""
PIPES = ["-", "7", "|", "J", "L", "F"]

S = ["|", "7", "F", "S"]
N = ["|", "L", "J", "S"]
E = ["-", "F", "L", "S"]
W = ["-", "J", "7", "S"]

# (c,r)
sys.setrecursionlimit(100_000)


def part1():
    grid = []
    distances_from_start = defaultdict(lambda: -1)
    start_location = ()
    for i, line in enumerate(D.splitlines()):
        line_list = list(line)
        line_list.append(".")
        line_list.insert(0, ".")
        if "S" in line_list:
            start_location = (line_list.index("S"), i + 1)
        grid.append(line_list)

    dots_list = ["."] * (len(grid[0]) + 2)
    grid.insert(0, dots_list)
    grid.append(dots_list)

    def go_through_path(current_position, previous_movement="", farthest_distance=1):
        up_symbol = grid[current_position[1] - 1][current_position[0]]
        down_symbol = grid[current_position[1] + 1][current_position[0]]
        left_symbol = grid[current_position[1]][current_position[0] - 1]
        right_symbol = grid[current_position[1]][current_position[0] + 1]
        current_symbol = grid[current_position[1]][current_position[0]]

        # loop finished
        if previous_movement != "" and current_symbol == "S":
            return farthest_distance

        curr_pos_distance = distances_from_start[current_position]
        if curr_pos_distance == -1:
            distances_from_start[current_position] = farthest_distance
        else:
            distances_from_start[current_position] = min(
                curr_pos_distance, farthest_distance
            )

        # check if can go up
        if current_symbol in N and up_symbol in S and previous_movement != "DOWN":
            # can go up
            return go_through_path(
                (current_position[0], current_position[1] - 1),
                "UP",
                farthest_distance + 1,
            )

        # check if can go down
        if current_symbol in S and down_symbol in N and previous_movement != "UP":
            return go_through_path(
                (current_position[0], current_position[1] + 1),
                "DOWN",
                farthest_distance + 1,
            )

        # check if can go left
        if current_symbol in W and left_symbol in E and previous_movement != "RIGHT":
            return go_through_path(
                (current_position[0] - 1, current_position[1]),
                "LEFT",
                farthest_distance + 1,
            )

        # check if can go right
        if current_symbol in E and right_symbol in W and previous_movement != "LEFT":
            return go_through_path(
                (current_position[0] + 1, current_position[1]),
                "RIGHT",
                farthest_distance + 1,
            )

        return farthest_distance

    def path_starting_positions(current_position):
        starting_positions = []
        up_symbol = grid[current_position[1] - 1][current_position[0]]
        down_symbol = grid[current_position[1] + 1][current_position[0]]
        left_symbol = grid[current_position[1]][current_position[0] - 1]
        right_symbol = grid[current_position[1]][current_position[0] + 1]
        current_symbol = grid[current_position[1]][current_position[0]]

        # check if can go up
        if current_symbol in N and up_symbol in S:
            # can go up
            starting_positions.append(
                (current_position[0], current_position[1] - 1, "UP"),
            )

        # check if can go down
        if current_symbol in S and down_symbol in N:
            starting_positions.append(
                (current_position[0], current_position[1] + 1, "DOWN"),
            )

        # check if can go left
        if current_symbol in W and left_symbol in E:
            starting_positions.append(
                (current_position[0] - 1, current_position[1], "LEFT"),
            )

        # check if can go right
        if current_symbol in E and right_symbol in W:
            starting_positions.append(
                (current_position[0] + 1, current_position[1], "RIGHT"),
            )

        return starting_positions

    test = path_starting_positions(start_location)

    for t in test:
        go_through_path((t[0], t[1]), t[2])

    print(max(distances_from_start.values()))


if __name__ == "__main__":
    start = time()
    part1()
    print(f"Time: {(time() - start) * 1000:.3f}ms")
