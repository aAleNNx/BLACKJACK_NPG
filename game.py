from computer import ComputerPlayer
from deck import *
from player import *
import time
import threading


class Game:
    def __init__(self, com_player: ComputerPlayer, *players: Player, deck_count=1, time_limit=60):
        self.time_limit = time_limit
        self.time_left = time_limit
        self.timer_running = False
        self.timer_thread = None
        self.deck = Deck(deck_count)
        self.players = players
        self.com_player = com_player

    def run(self, num_rounds):
        for i in range(num_rounds):
            print("ROUND", i + 1)
            self.play_round()
            input("Press enter to continue...")
        print("FINISHED")  # kto wygrał

    def player_round(self, player: Player):
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

    def play_round(self):
        self.com_player.add_card(self.deck.draw())
        print(self.com_player.name)
        self.com_player.show_hand()

        for player in self.players:
            self.player_round(player)

        print(self.com_player.name)
        while self.com_player.should_draw_card():
            self.com_player.add_card(self.deck.draw())
            self.com_player.show_hand()
            print("Hand value:", self.com_player.get_hand_value(), "\n")
            input("Press enter to continue...")

        com_val = self.com_player.get_hand_value()

        if com_val > 21:
            print("Bust!\n")

        print("\tRESULTS:")
        for player in self.players:
            val = player.get_hand_value()
            if val <= 21 and (val > com_val or com_val > 21):
                print(player.name, "WINS!\n")
            elif 21 <= val == com_val:
                print(player.name, "DRAWS!\n")
            else:
                print(player.name, "LOSES!\n")
            player.reset_hand()

        self.com_player.reset_hand()


p1 = Player("Leon")
c = ComputerPlayer("Dealer")
game = Game(c, p1, deck_count=2)
game.run(3)
