from card import *
from deck import *
from player import *
from computer import *

class Game:
    def __init__(self, player, opponent, deck_count = 1):
        self.deck = Deck(deck_count)
        self.player = player
        self.opponent = opponent
    
    def run(self):
        for i in range(10):
            self.play_round()
        
    def play_round(self):
        print(self.opponent.name)
        self.opponent.add_card(self.deck.draw(), self.deck, self.player)
        self.opponent.add_card(self.deck.draw(), self.deck, self.player)
        print(self.opponent.hand[0])
        print(f"{self.opponent.name}'s hand value:", self.opponent.hand[0].get_value(), "\n")

        print(self.player.name)
        self.player.add_card(self.deck.draw(), self.deck, self.opponent)
        self.player.add_card(self.deck.draw(), self.deck, self.opponent)
        self.player.show_hand()
        print("Your hand value:", self.player.get_hand_value(), "\n")

        if self.player.get_hand_value() == 21:
            print("BLACKJACK")

        while self.player.get_hand_value() < 21:
            print("1. Hit\n2. Stand")
            choice = int(input())
            if choice == 1:
                self.player.add_card(self.deck.draw(), self.deck, self.opponent)
                self.player.show_hand()
                print("Your hand value:", self.player.get_hand_value(), "\n")
            elif choice == 2:
                break
            else:
                print("Invalid choice")

        if self.player.get_hand_value() > 21:
            print(f"Bust! {self.opponent.name} wins!")
        else:
            print(f"{self.opponent.name}'s hand: \n")
            self.opponent.show_hand()
            while self.opponent.should_draw_card():
                self.opponent.add_card(self.deck.draw(), self.deck, self.opponent)
                print(self.opponent.hand[-1])
            print(f"{self.opponent.name}'s hand value:",self.opponent.get_hand_value())
            if self.player.get_hand_value() > self.opponent.get_hand_value():
                print(f"{self.player.name} wins!")
            elif self.player.get_hand_value() < self.opponent.get_hand_value() <= 21:
                print(f"{self.opponent.name} wins!")
            elif self.opponent.get_hand_value() > 21:
                print(f"{self.player.name} wins!")
            elif self.opponent.get_hand_value() == self.player.get_hand_value():
                print("Draw.\n")
            pass
        self.player.reset_hand()

player = Player("Leon")
computer = ComputerPlayer("Dealer")
game = Game(player, opponent=computer)
game.run()