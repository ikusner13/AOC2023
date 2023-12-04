S = ["*", '+', '$', "#", "/", "@", "%", '=', "&", "-"]
D = open(0).read().strip().splitlines()

def find_adjacent_numbers_sum(schematic, symbols):
    rows = len(schematic)
    cols = len(schematic[0])
    adjacent_numbers = []

    # Function to check if a cell is adjacent to a symbol
    def is_adjacent_to_symbol(x, y):
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if 0 <= x + dx < rows and 0 <= y + dy < cols:
                    if schematic[x + dx][y + dy] in symbols:
                        return True
        return False

    # Iterate over each cell in the schematic
    for x in range(rows):
        y = 0
        while y < cols:
            if schematic[x][y].isdigit():
                # Extract the complete number
                number = ''
                while y < cols and schematic[x][y].isdigit():
                    number += schematic[x][y]
                    y += 1

                # Convert to integer and check for adjacency
                number_int = int(number)
                start_y = y - len(number)  # Starting position of the number
                if any(is_adjacent_to_symbol(x, start_y + i) for i in range(len(number))):
                    adjacent_numbers.append(number_int)
            else:
                y += 1

    return sum(adjacent_numbers)


def find_valid_gears_and_calculate_ratios(schematic):
    rows = len(schematic)
    cols = len(schematic[0])
    sum_ratios = 0

    # Check if a position is within the grid
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    # Extract a number starting at (x, y), considering multi-digit numbers
    def extract_number(x, y):
        number = ''
        # Move left to the start of the number if it's multi-digit
        while y > 0 and schematic[x][y - 1].isdigit():
            y -= 1
        # Extract the full number
        while y < cols and schematic[x][y].isdigit():
            number += schematic[x][y]
            y += 1
        return int(number) if number else None

    # Check adjacent cells for part numbers
    def find_adjacent_parts(x, y):
        adjacent_parts = set()
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                nx, ny = x + dx, y + dy
                if (dx != 0 or dy != 0) and is_valid(nx, ny) and schematic[nx][ny].isdigit():
                    number = extract_number(nx, ny)
                    if number is not None:
                        adjacent_parts.add(number)
        return list(adjacent_parts)

    # Iterate over the schematic to find gears and calculate gear ratios
    for x in range(rows):
        for y in range(cols):
            if schematic[x][y] == '*':  # Check for gears
                parts = find_adjacent_parts(x, y)
                if len(parts) == 2:  # Valid gear must have exactly two adjacent numbers
                    sum_ratios += parts[0] * parts[1]

    return sum_ratios

p1 = find_adjacent_numbers_sum(D, S)
p2 = find_valid_gears_and_calculate_ratios(D)

print(p1)
print(p2)
