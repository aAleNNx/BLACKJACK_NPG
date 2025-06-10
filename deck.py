from card import Card
import random

class Deck:
    def __init__(self, deck_count=1):
        self.deck_count = deck_count
        self.deck = self.generate_decks()
        random.shuffle(self.deck)

    def generate_decks(self):
        suits=["Clubs", "Diamonds", "Hearts", "Spades"]
        ranks=["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        cards = []
        for i in range(self.deck_count):
            for suit in suits:
                for rank in ranks:
                    cards.append(Card(suit, rank))
        special_cards =[
            Card(suit="Special", rank="JOKER", is_special=True),
            Card(suit="Special", rank="C", is_special=True),
            Card(suit="Special", rank="D", is_special=True),
            Card(suit="Special", rank="X", is_special=True),
            Card(suit="Special", rank="Z", is_special=True),]
        for special in special_cards:
            cards.append(special)
        return cards

    def draw(self):
        if not self.deck:
            print("Brak kart w talii.")
            return None
        return self.deck.pop()

    def reset(self):
        self.deck = self.generate_decks()
        random.shuffle(self.deck)
