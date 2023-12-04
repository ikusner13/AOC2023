from collections import defaultdict


D = open(0).read()


def part2():
    lines = D.splitlines()

    instances_per_card = defaultdict(lambda: 1)
    processed_cards = set()

    for current_line, line in enumerate(lines):
        instance_on_current_line = instances_per_card[current_line + 1]
        card_number, card_data = line.split(":")

        if card_number in processed_cards:
            continue

        number_on_card = int(card_number.split()[1])
        winning_numbers, my_numbers = card_data.split("|")
        winning_numbers = set(winning_numbers.split())
        my_numbers = my_numbers.split()

        winners = sum(1 for number in my_numbers if number in winning_numbers)

        for i in range(1, winners + 1):
            instances_per_card[number_on_card + i] += instance_on_current_line

        processed_cards.add(card_number)

    print(sum(instances_per_card.values()))


if __name__ == "__main__":
    part2()
