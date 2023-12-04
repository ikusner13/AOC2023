import time


def calculate_card_points(cards):
    total_points = 0
    for card in cards:
        card = card.split(":")[1]
        winning_numbers, your_numbers = card.split(" | ")
        winning_numbers_set = set(map(int, winning_numbers.split()))
        your_numbers_set = set(map(int, your_numbers.split()))
        matches = winning_numbers_set.intersection(your_numbers_set)
        if matches:
            # Calculate points for the card
            points = 1 << (
                len(matches) - 1
            )  # Double points for each match after the first
            total_points += points
    return total_points


def count_total_scratchcards(cards):
    card_copies = [1] * len(cards)  # Each card starts with 1 original copy

    for i, card in enumerate(cards):
        card = card.split(":")[1]
        winning_numbers, your_numbers = card.split(" | ")
        winning_numbers_set = set(map(int, winning_numbers.split()))
        your_numbers_set = set(map(int, your_numbers.split()))
        matches = winning_numbers_set.intersection(your_numbers_set)
        num_matches = len(matches)

        # Distribute copies for each match to subsequent cards
        for j in range(i + 1, min(i + 1 + num_matches, len(cards))):
            card_copies[j] += card_copies[i]

    return sum(card_copies)


D = open(0).read()
cards = D.splitlines()
start_time = time.time()
total_points = calculate_card_points(cards)
execution_time = time.time() - start_time

print(f"Total points: {total_points}")
print(f"Execution time: {execution_time} seconds")
print("\n")

# Measure execution time
start_time = time.time()
total_scratchcards = count_total_scratchcards(cards)
execution_time = time.time() - start_time

print(f"Total scratchcards: {total_scratchcards}")
print(f"Execution time: {execution_time} seconds")
