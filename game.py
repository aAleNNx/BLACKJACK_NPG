from card import *
from deck import *
from player import *

class Game:
    def __init__(self, *players, deck_count = 1):
        self.deck = Deck(deck_count)
        self.players = players
    
    def run(self):
        for i in range(10):
            self.play_round()
        
    def play_round(self):
        for player in self.players:
            print(player.name)
            player.add_card(self.deck.draw())
            player.add_card(self.deck.draw())
            player.show_hand()
            print("Hand value:", player.get_hand_value(), "\n")
            if player.get_hand_value() == 21:
                print("BLACKJACK")

            while player.get_hand_value() < 21:
                print("1. Hit\n2. Stand")
                choice = int(input())
                if choice == 1:
                    player.add_card(self.deck.draw())
                    player.show_hand()
                    print("Hand value:", player.get_hand_value(), "\n")
                elif choice == 2:
                    break
                else:
                    print("Invalid choice")

            if player.get_hand_value() > 21:
                print("Bust!")
            else:
                # porównanie do ręki dealera albo innych graczy
                pass
            player.reset_hand()

player = Player("Leon")
game = Game(player)
game.run()