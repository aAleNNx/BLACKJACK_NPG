import random
from utils import *
from special_cards import apply_special_effect

class ComputerPlayer:
    def __init__(self, name="Komputer"):
        self.name = name
        self.hand = []
        self.next_card_mult = 1.0
        self.standing = False
        self.busted = False

    def add_card(self, card, deck = None, player = None):
        if self.next_card_mult != 1.0:
            card.multiplier = self.next_card_mult
            self.next_card_mult = 1.0
        self.hand.append(card)
        if calculate_hand_value(self.hand) > 21:
            self.busted = True

        if getattr(card, 'is_special', False):
            apply_special_effect(card, self, deck, player)  # Deck i przeciwnik muszą być przekazane wyżej

    def get_hand_value(self):
        return calculate_hand_value(self.hand)

    def should_draw_card(self):
        value = calculate_hand_value(self.hand)
        return value < 17

    def reset_hand(self):
        self.hand = []
        self.standing = False
        self.busted = False

    def show_hand(self):
        print("|||", end=" ")
        for card in self.hand:
            print(card, end=' ||| ')
        print("\n")

    def __str__(self):
        return f"{self.name} — ręka: {[str(card) for card in self.hand]}"