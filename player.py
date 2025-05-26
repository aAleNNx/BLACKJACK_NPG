from utils import calculate_hand_value

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.standing = False
        self.busted = False
        self.next_card_mult = 1.0

    def add_card(self, card):
        if self.next_card_mult != 1.0:
            card.multiplier = self.next_card_mult
            self.next_card_mult = 1.0
        self.hand.append(card)
        if calculate_hand_value(self.hand) > 21:
            self.busted = True

    def get_hand_value(self):
        return calculate_hand_value(self.hand)

    def reset_hand(self):
        self.hand = []
        self.standing = False
        self.busted = False

    def show_hand(self):
        for card in self.hand:
            print(card)
            print("\n")


