with open('inputs/Day_4.txt', 'r') as input:
    lines = [line.strip() for line in input.readlines()]

def count_winners(card):
    winners, hand = card.split(' | ')
    winners = winners.split()  # String to list
    hand = hand.split()  # String to list
    win_count = 0
    for number in hand:
        if number in winners:
            win_count += 1
    return win_count

sum_1 = 0

labels, cards = zip(*[line.split(': ') for line in lines])
for card in cards:
    win_count = count_winners(card)
    if win_count > 0:  # No winners means no points
        sum_1 += 2 ** (win_count - 1)

print(f'Part 1: {sum_1}')  # Answer 26443

card_counts = {label:1 for label in labels}

for i, card in enumerate(cards):
    label = labels[i]
    card_quantity = card_counts[label]
    win_count = count_winners(card)
    for j in range(i + 1, i + win_count + 1):  # count from next card
        if j >= len(lines):  # Don't copy cards beyond end of list
            break
        card_counts[labels[j]] += card_quantity
    
sum_2 = sum(card_counts.values())

print(f'Part 2: {sum_2}')  # Answer 6284877