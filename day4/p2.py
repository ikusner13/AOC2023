from collections import defaultdict


D = open(0).read()


# Part 2
def part2():
    lines = D.splitlines()

    instances_per_card = defaultdict(lambda: 1)
    winners_per_card = defaultdict(int)
    processed_cards = set()

    for current_line, line in enumerate(lines):
        instance_on_current_line = instances_per_card[current_line + 1]
        card_number, card_data = line.split(":")

        if card_number in processed_cards:
            continue

        number_on_card = int(card_number.split()[1])
        winning_numbers, my_numbers = card_data.split("|")
        winning_numbers = winning_numbers.split()
        my_numbers = my_numbers.split()

        winners = sum(1 for number in my_numbers if number in winning_numbers)
        winners_per_card[card_number] = winners

        for i in range(1, winners + 1):
            instances_per_card[number_on_card + i] += instance_on_current_line

        processed_cards.add(card_number)

    sum_instances = sum(instances_per_card.values())
    print(f"sum_instances: {sum_instances}")


if __name__ == "__main__":
    part2()
