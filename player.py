from utils import calculate_hand_value
from special_cards import *
import copy

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.standing = False
        self.busted = False
        self.next_card_mult = 1.0
        self.undo_stack = []

    def add_card(self, card, deck=None, computer=None):
        self.save_undo_state(deck)
        if self.next_card_mult != 1.0:
            card.multiplier = self.next_card_mult
            self.next_card_mult = 1.0
        self.hand.append(card)
        if calculate_hand_value(self.hand) > 21:
            self.busted = True

        if getattr(card, 'is_special', False):
            apply_special_effect(card, self, deck, computer)

    def save_undo_state(self, deck):
        # Save deep copy of hand and deck
        self.undo_stack.append({
            "hand": copy.deepcopy(self.hand),
            "busted": self.busted,
            "next_card_mult": self.next_card_mult,
            "deck": copy.deepcopy(deck.deck) if deck else None
        })

    def undo(self, deck=None):
        if self.undo_stack:
            state = self.undo_stack.pop()
            self.hand = state["hand"]
            self.busted = state["busted"]
            self.next_card_mult = state["next_card_mult"]
            if deck and state["deck"] is not None:
                deck.deck = state["deck"]
            print("🔄 Move undone!")
        else:
            print("⚠️ No moves to be undone.")

    def remove_card(self):
        return self.hand.pop()

    def can_split(self):
        return len(self.hand) == 2 and self.hand[0].get_value() == self.hand[1].get_value() != 0

    def get_hand_value(self):
        return calculate_hand_value(self.hand)

    def reset_hand(self):
        self.hand = []
        self.standing = False
        self.busted = False
        self.next_card_mult = 1.0
        self.undo_stack.clear()

    def show_hand(self):
        print(end='||| ')
        for card in self.hand:
            print(card, end=' ||| ')
        print("\n")


class Split_Hand(Player):
    def __init__(self, name, player):
        super().__init__(name)
        self.player = player

    def can_split(self):
        return False
