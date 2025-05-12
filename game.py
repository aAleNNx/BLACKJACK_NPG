from card import *
from deck import *
from player import *

class Game:
    def __init__(self, deck_count = 1, *players):
        self.deck = Deck(deck_count)
        self.players = players
    
    def run(self):
        for i in range(10):
            play_round()
        
    def play_round(self)
        for player in self.players:
            player.add_card(self.deck.draw())
            player.add_card(self.deck.draw())
            player.show_hand()
            #tutaj hit stand itd
            player.get_hand_value()
            player.reset_hand()