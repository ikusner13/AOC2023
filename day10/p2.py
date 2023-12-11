from collections import defaultdict
from time import time


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


def part1():
    grid = []
    distances_from_start = defaultdict(lambda: -1)
    start_location = (0, 0)
    for i, line in enumerate(D.splitlines()):
        line_list = list(line)
        line_list.append(".")
        line_list.insert(0, ".")
        if "S" in line_list:
            start_location = (line_list.index("S"), i + 1)
        grid.append(line_list)

    dots_list = ["."] * (len(grid[0]))
    grid.insert(0, dots_list)
    grid.append(dots_list)

    bounds = [start_location]

    stack = [(start_location, None, 0)]

    while stack:
        current_position, previous_movement, farthest_distance = stack.pop()

        up_symbol = grid[current_position[1] - 1][current_position[0]]
        down_symbol = grid[current_position[1] + 1][current_position[0]]
        left_symbol = grid[current_position[1]][current_position[0] - 1]
        right_symbol = grid[current_position[1]][current_position[0] + 1]
        current_symbol = grid[current_position[1]][current_position[0]]

        # loop finished
        if previous_movement and current_symbol == "S":
            continue

        curr_pos_distance = distances_from_start[current_position]
        if curr_pos_distance == -1 or curr_pos_distance > farthest_distance:
            distances_from_start[current_position] = farthest_distance

        # check if can go up
        if current_symbol in N and up_symbol in S and previous_movement != "DOWN":
            # can go up
            stack.append(
                (
                    (current_position[0], current_position[1] - 1),
                    "UP",
                    farthest_distance + 1,
                ),
            )
            bounds.append((current_position[0], current_position[1] - 1))
            continue

        # check if can go down
        if current_symbol in S and down_symbol in N and previous_movement != "UP":
            stack.append(
                (
                    (current_position[0], current_position[1] + 1),
                    "DOWN",
                    farthest_distance + 1,
                ),
            )
            bounds.append((current_position[0], current_position[1] + 1))
            continue

        # check if can go left
        if current_symbol in W and left_symbol in E and previous_movement != "RIGHT":
            stack.append(
                (
                    (current_position[0] - 1, current_position[1]),
                    "LEFT",
                    farthest_distance + 1,
                ),
            )
            bounds.append((current_position[0] - 1, current_position[1]))
            continue

        # check if can go right
        if current_symbol in E and right_symbol in W and previous_movement != "LEFT":
            stack.append(
                (
                    (current_position[0] + 1, current_position[1]),
                    "RIGHT",
                    farthest_distance + 1,
                ),
            )
            bounds.append((current_position[0] + 1, current_position[1]))
            continue

    enclosed = 0
    for ri, r in enumerate(grid):
        seen = 0
        for ci, c in enumerate(r):
            if (ci, ri) in bounds and c in ["J", "L", "|"]:
                seen += 1

            if (ci, ri) not in bounds and seen % 2 != 0:
                enclosed += 1

    print(enclosed)


if __name__ == "__main__":
    start = time()
    part1()
    print(f"Time: {(time() - start) * 1000:.3f}ms")
