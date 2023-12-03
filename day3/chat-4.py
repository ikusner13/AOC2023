def find_adjacent_numbers_corrected(schematic, symbols):
    print(schematic)
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

    return adjacent_numbers

S = ["*", '+', '$', "#", "/", "@", "%", '=', "&", "-"]
D = open(0).read().strip().splitlines()


# Find numbers adjacent to a symbol with corrected logic
adjacent_numbers_corrected = find_adjacent_numbers_corrected(D, S)
print(sum(adjacent_numbers_corrected))
