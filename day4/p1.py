D = open(0).read()


def part1():
    lines = D.splitlines()

    points = 0
    for line in lines:
        card_data = line.split(":")[1]

        winning_numbers, my_numbers = card_data.split("|")
        winning_numbers = winning_numbers.split()
        my_numbers = my_numbers.split()

        winners = sum(1 for number in my_numbers if number in winning_numbers)

        if winners != 0:
            points += 2 ** (winners - 1)

    print(f"points: {points}")


if __name__ == "__main__":
    part1()
