D = open(0).read()


def part1():
    lines = D.splitlines()

    points = 0
    for line in lines:
        card_data = line.split(":")[1]

        winning_numbers, my_numbers = card_data.split("|")
        winning_numbers = set(winning_numbers.split())
        my_numbers = set(my_numbers.split())

        intersections = len(winning_numbers.intersection(my_numbers))

        if intersections:
            points += 2 ** (intersections - 1)

    print(f"points: {points}")


if __name__ == "__main__":
    part1()
