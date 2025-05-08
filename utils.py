def calculate_hand_value(hand):
    total_val = 0
    aces_count = 0

    for card in hand:
        if card.is_special:
            continue
        if card.rank in ['J', 'Q', 'K']:
            total_val += 10
        elif card.rank == 'A':
            total_val += 11
            aces_count += 1
        else:
            total_val += int(card.rank)

    while total_val > 21 and aces_count > 0:
        total_val -= 10
        aces_count -= 1

    return total_val