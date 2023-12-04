D = open(0).read()


# Part 1
def part1():
    lines = D.splitlines()

    total_points = 0
    for line in lines:
        card_number, card_data = line.split(":")
        winning_numbers, my_numbers = card_data.split("|")
        winning_numbers = winning_numbers.split()
        my_numbers = my_numbers.split()
        print(f"card_number: {card_number}")
        print(f"winning_numbers: {winning_numbers}")
        print(f"my_numbers: {my_numbers}")

        winners = 0
        for number in my_numbers:
            if number in winning_numbers:
                print(f"Number {number} is a winner!")
                winners += 1
            else:
                print(f"Number {number} is a loser!")

        print(f"Total winners: {winners}")
        card_total = 2 ** (winners - 1) if winners > 0 else 0
        print(f"Total score: {card_total}")
        total_points += card_total

    print(f"Total points: {total_points}")


if __name__ == "__main__":
    part1()
