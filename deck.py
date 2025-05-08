from card import Card
import random

class Deck:
    def __init__(self, deck_count =  1):
        self.deck_count = deck_count
        self.deck = self.generate_decks()
        random.shuffle(self.deck)

    def generate_decks(self):
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        ranks = ['2', '3', '4', '5', '6','7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        cards = []
        for i in range(self.deck_count):
            for suit in suits:
                for rank in ranks:
                    cards.append(Card(suit, rank))
        special_cards = [ Card('Special','',is_special = True),
        Card('Special','',is_special = True), Card('Special','',is_special = True), Card('Special','',is_special = True)]
        return cards

    def draw(self):
        if not self.deck:
            print("Brak kart w talii.")
            return None
        return self.deck.pop()

    def reset(self):
        self.deck = self.generate_decks()
        random.shuffle(self.deck)