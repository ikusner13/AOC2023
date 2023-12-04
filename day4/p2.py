from collections import defaultdict


D = open(0).read()


# Part 1
def part1():
    lines = D.splitlines()

    instances_per_card = defaultdict(int)
    winners_per_card = defaultdict(int)

    for i in range(len(lines)):
        instances_per_card[i + 1] = 1
    # start with line 0
    line_0 = lines[0]

    card_number, card_data = line_0.split(":")
    number_on_card = int(card_number.split()[1])
    winning_numbers, my_numbers = card_data.split("|")
    winning_numbers = winning_numbers.split()
    my_numbers = my_numbers.split()

    print(f"card_number: {card_number}")
    print(f"winning_numbers: {winning_numbers}")
    print(f"my_numbers: {my_numbers}")
    ## print a wall of #s
    print("#" * 80)

    winners = 0
    for number in my_numbers:
        if number in winning_numbers:
            winners_per_card[card_number] += 1
            winners += 1
            instances_per_card[number_on_card + winners] += 1

    print(f"Total winners: {winners}")

    print(f"winners_per_card: {winners_per_card}")

    # now go through rest of lines per times in instances_per_card, adding to instances_per_card

    number_of_lines = len(lines) - 1  # we already did line 0
    current_line = 1

    while current_line < number_of_lines:
        print(f"i: {current_line}")
        instance_on_current_line = instances_per_card.get(
            current_line + 1, 1
        )  # plus 1 because of original card

        # print(f"instance_on_current_line: {instance_on_current_line}")
        while instance_on_current_line > 0:
            if winners_per_card.get(current_line, 0) > 0:
                instance_on_current_line -= 1
                continue

            line = lines[current_line]

            card_number, card_data = line.split(":")
            number_on_card = int(card_number.split()[1])
            winning_numbers, my_numbers = card_data.split("|")
            winning_numbers = winning_numbers.split()
            my_numbers = my_numbers.split()

            winners = 0
            for number in my_numbers:
                if number in winning_numbers:
                    winners += 1
                    winners_per_card[card_number] += 1
                    instances_per_card[number_on_card + winners] += 1

            instance_on_current_line -= 1

        current_line += 1

    print(instances_per_card)

    sum_instances = sum(instances_per_card.values())
    print(f"sum_instances: {sum_instances}")


if __name__ == "__main__":
    part1()
