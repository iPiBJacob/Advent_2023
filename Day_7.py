from functools import cmp_to_key

with open('inputs/Day_7.txt', 'r') as input:
    lines = [line.strip() for line in input.readlines()]

hands_and_bets = {hand: int(bet) for hand, bet in [line.split()for line in lines]}

def label_hand(hand):  # Assign a type to the hand
    counts = [hand.count(char) for char in card_chars]
    if 5 in counts:
        return 6  # 5 of a kind has highest value
    if 4 in counts:
        return 5  # 4 of a kind is next
    if 3 in counts and 2 in counts:
        return 4  # Then full house
    if 3 in counts:
        return 3  # Three of a kind is next
    if 2 in counts:
        if counts.count(2) == 2:
            return 2  # Followed by two pair
        return 1  # Then one pair
    return 0  # Then simple high card

def label_hand_jokers_wild(hand):
    counts = [hand.count(char) for char in card_chars]
    if counts[0] == 0:
        return label_hand(hand)
    jokers = counts.pop(0)
    if any([count + jokers >= 5 for count in counts]):
        return 6  # Jokers create 5 of a kind
    if any([count + jokers >= 4 for count in counts]):
        return 5  # If 5 not possible, 4 is next best
    if counts.count(2) == 2 and jokers == 1:
        # Only way to make full house with jokers
        return 4  # Any other possibility could make 4 instead
    if any([count + jokers >= 3 for count in counts]):
        return 3  # Either a single + 2 J or a pair + 1 J
    if any([count + jokers >= 2 for count in counts]):
        # Two pair is impossible with jokers present as 3 is better
        return 1  # Then one pair
    return 0  # Then simple high card
    

def compare_hands(hand_1, hand_2):
    
    hand_1_rank = hand_label_function(hand_1)
    hand_2_rank = hand_label_function(hand_2)
    if hand_1_rank < hand_2_rank:
        return -1  # Hand 1 is lesser and should be sorted first
    if hand_1_rank > hand_2_rank:
        return 1  # Hand 2 is lesser and should be sorted first
    # If here, both hands are same type. Compare card by card
    for i in range(5):
        if card_chars.index(hand_1[i]) < card_chars.index(hand_2[i]):
            return -1 # Hand 1 is lesser and goes first
        if card_chars.index(hand_1[i]) > card_chars.index(hand_2[i]):
            return 1 # Hand 2 is lesser and goes first
    return 0  # Hands are identical. Leave in current order

hands = [hand for hand in hands_and_bets]
hand_label_function = label_hand
card_chars = '23456789TJQKA'
hands.sort(key=cmp_to_key(compare_hands))  # Order based on comparison rules set above

sum_1 = 0
for i, hand in enumerate(hands):
    sum_1 += hands_and_bets[hand] * (i + 1)  # +1 to convert zero index to unit index

print(f'Part 1: {sum_1}')  # Answer 253313241

hands = [hand for hand in hands_and_bets]
hand_label_function = label_hand_jokers_wild
card_chars = 'J23456789TQKA'
hands.sort(key=cmp_to_key(compare_hands))  # Order based on comparison rules set above

sum_2 = 0
for i, hand in enumerate(hands):
    sum_2 += hands_and_bets[hand] * (i + 1)  # +1 to convert zero index to unit index

print(f'Part 2: {sum_2}')  # Answer 253362743


