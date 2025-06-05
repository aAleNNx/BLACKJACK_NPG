from card import *
from deck import *
from player import *
from computer import *
import time

class Game:
    def __init__(self, player, opponent, deck_count = 1):
        self.deck = Deck(deck_count)
        self.player = player
        self.opponent = opponent
    
    def run(self):
        for i in range(1):
            self.play_round()
        
    def play_round(self):
        print(self.opponent.name,":\n")
        self.opponent.add_card(self.deck.draw(), self.deck, self.player)
        self.opponent.add_card(self.deck.draw(), self.deck, self.player)
        print(f"{self.opponent.name}'s first card:", self.opponent.hand[0])
        print(f"{self.opponent.name}'s first card value:", self.opponent.hand[0].get_value(), "\n")

        print(self.player.name,":\n")
        self.player.add_card(self.deck.draw(), self.deck, self.opponent)
        self.player.add_card(self.deck.draw(), self.deck, self.opponent)
        print(f"{self.player.name}'s hand:")
        self.player.show_hand()
        print(f"{self.player.name}'s hand value:", self.player.get_hand_value(), "\n")

        if self.player.get_hand_value() == 21:
            print("BLACKJACK!")
            if self.opponent.get_hand_value() == 21:
                print(f"{self.opponent.name}'s hand:")
                self.opponent.show_hand()
                print(f"{self.opponent.name}'s hand value:", self.opponent.get_hand_value(), "\n")
                print("BLACKJACK DRAW!")
            else:
                print(f"{self.opponent.name}'s hand value:", self.opponent.get_hand_value(), "\n")
                print(f"{self.player.name} wins!")

        else:
            while self.player.get_hand_value() < 21:
                print("1. Hit\n2. Stand")
                choice = int(input())
                if choice == 1:
                    self.player.add_card(self.deck.draw(), self.deck, self.opponent)
                    print(f"{self.player.name}'s hand:")
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
                print(f"{self.opponent.name}'s hand value: ", self.opponent.get_hand_value())
                if self.player.get_hand_value() > self.opponent.get_hand_value():
                    print(f"{self.player.name} wins!")
                elif self.player.get_hand_value() < self.opponent.get_hand_value() <= 21:
                    print(f"{self.opponent.name} wins!")
                elif self.opponent.get_hand_value() > 21:
                    print(f"{self.player.name} wins!")
                elif self.opponent.get_hand_value() == self.player.get_hand_value():
                    print("Draw.\n")
                pass
        print("\n\n\n")
        time.sleep(5)
        self.player.reset_hand()
        self.opponent.reset_hand()

player = Player("Leon")
computer = ComputerPlayer("Dealer")
game = Game(player, opponent=computer)
game.run()