def calculate_hand_value(hand):
    total_val = 0
    aces_count = 0
    jokers_count = 0

    for card in hand:
        mult = getattr(card, 'multiplier', 1.0)
        if card.is_special and card.rank != "JOKER":
            continue
        if card.rank in ['J', 'Q', 'K']:
            total_val += 10 * mult
        elif card.rank == 'A':
            total_val += 11 * mult
            aces_count += 1
        elif card.rank == "JOKER":
            jokers_count += 1
        else:
            total_val += int(card.rank)

    while total_val > 21 and aces_count > 0:
        total_val -= 10 * mult
        aces_count -= 1

    for i in range(jokers_count):
        best_value = 21 - total_val
        if best_value >= 11:
            joker_value = 11
        elif best_value >= 10:
            joker_value = 10
        elif best_value >= 2:
            joker_value = best_value
        else:
            joker_value = 1
        total_val += joker_value

    return total_val