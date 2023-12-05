from collections import defaultdict
from memory_profiler import profile
import time


D = open(0).read()


@profile
def part2():
    lines = D.splitlines()

    instances_per_card = defaultdict(lambda: 1)

    for current_line, line in enumerate(lines):
        # get the number of instances (original + copies) of the current card, or create a new one with 1
        instance_on_current_line = instances_per_card[current_line + 1]
        card_number, card_data = line.split(":")

        number_on_card = int(card_number.split()[1])
        winning_numbers, my_numbers = card_data.split("|")
        winning_numbers = set(winning_numbers.split())
        my_numbers = set(my_numbers.split())

        # get the number of winning numbers on the current card
        # another way to write this would be:
        # for number in my_numbers:
        #     if number in winning_numbers:
        #         winners += 1
        intersections = len(winning_numbers.intersection(my_numbers))

        # loop through the winners and add copies to the next lines
        for i in range(1, intersections + 1):
            # add the number of instances on the current line to the next line
            # for example, if there are 2 instances of the current card on the current line,
            # add 2 instances of the next card to the next line
            # this is because each copy of the current card will add 1 instance of the next card
            instances_per_card[number_on_card + i] += instance_on_current_line

    print(sum(instances_per_card.values()))


if __name__ == "__main__":
    start_time = time.time()
    part2()
    print(f"--- {time.time() - start_time} seconds ---")
