D = open(0).read().splitlines()


def beam_path(grid, start_point, start_dir):
    beams = [(start_point, start_dir)]
    visited = set()

    while len(beams) > 0:
        new_beams = []
        for pos, dir in beams:
            x, y = pos

            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                continue

            if (pos, dir) in visited:
                continue
            visited.add((pos, dir))

            space = grid[x][y]
            if space == "/":
                dir = {"r": "u", "l": "d", "u": "r", "d": "l"}[dir]
            elif space == "\\":
                dir = {"r": "d", "l": "u", "u": "l", "d": "r"}[dir]
            elif space == "|" and dir in ["r", "l"]:
                new_beams.append(((x - 1, y), "u"))
                new_beams.append(((x + 1, y), "d"))
                continue
            elif space == "-" and dir in ["u", "d"]:
                new_beams.append(((x, y + 1), "r"))
                new_beams.append(((x, y - 1), "l"))
                continue

            x += {"u": -1, "d": 1}.get(dir, 0)
            y += {"r": 1, "l": -1}.get(dir, 0)
            new_beams.append(((x, y), dir))

        beams = new_beams
    return visited


def process_beam(grid, start_pos, direction):
    visits = beam_path(grid, start_pos, direction)
    unique_points = {point for point, _ in visits}
    return len(unique_points)


def part1():
    print(process_beam(D, (0, 0), "r"))


if __name__ == "__main__":
    part1()
