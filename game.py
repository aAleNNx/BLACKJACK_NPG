from typing import Any

from computer import ComputerPlayer
from deck import *
from player import *
import time
import threading
import sys
from stats import *



def clear_timer_line():
    sys.stderr.write('\r' + ' ' * 80 + '\r')
    sys.stderr.flush()


class Game:
    def __init__(self, com_player: ComputerPlayer, *players: Player, deck_count=1, time_limit=10, stats = None):
        self.time_limit = time_limit
        self.time_left = time_limit
        self.timer_running = False
        self.timer_thread = None
        self.deck = Deck(deck_count)
        self.players = players
        self.com_player = com_player
        self.time_up = False
        self.stats = stats

    def on_tick(self, sekundy):
        total = self.time_limit
        progress = int((total - sekundy) / total * 30)
        bar = "█" * progress + "-" * (30 - progress)
        print(f"\r[TIMER] ⏳ Left: {sekundy:2d}s |{bar}|", end='', flush=True, file=sys.stderr)

    def start_timer(self):
        self.time_left = self.time_limit
        self.time_up = False
        self.timer_running = False
        self.timer_thread = threading.Thread(target=self._run_timer)
        self.timer_thread.start()

    def _run_timer(self):
        self.timer_running = True
        while self.time_left > 0 and self.timer_running:
            time.sleep(1)
            self.time_left -= 1
            self.on_tick(self.time_left)
        if self.time_left <= 0:
            self.time_up = True
            if self.on_tick:
                self.on_tick(0)


    def stop_timer(self):
        self.timer_running = False
        if self.timer_thread and self.timer_thread.is_alive():
            self.timer_thread.join()
        self.time_left = self.time_limit

    def run(self, num_rounds):
        for i in range(num_rounds):
            print(f"\n===== ROUND {i + 1} =====")
            self.play_round()
            self.stop_timer()
            clear_timer_line()
            input("Press enter to continue...")
        print("Finished")

    def player_round(self, player: Player):
        print(f"\n▶️ {player.name}'s turn")
        player.add_card(self.deck.draw(), self.deck, self.com_player)
        player.add_card(self.deck.draw(), self.deck, self.com_player)
        player.show_hand()
        print("Hand value:", player.get_hand_value(), "\n")

        if player.get_hand_value() == 21:
            print("🎉 BLACKJACK!")
            return

        while player.get_hand_value() < 21:
            print("1. Hit\n2. Stand")
            self.start_timer()

            choice_holder = {'choice': None}

            def get_choice():
                try:
                    choice_holder['choice'] = int(input("Choose: "))
                except ValueError:
                    choice_holder['choice'] = None

            input_thread = threading.Thread(target=get_choice)
            input_thread.start()

            input_thread.join(timeout=self.time_limit)
            self.stop_timer()
            clear_timer_line()

            if input_thread.is_alive():
                print("\n⏱️ Time's up! Defaulting to Stand.")
                choice_holder['choice'] = 2
                break

            choice = choice_holder['choice']
            if choice == 1:
                player.add_card(self.deck.draw(), self.deck, self.com_player)
                player.show_hand()
                print("Hand value:", player.get_hand_value(), "\n")
            elif choice == 2:
                break
            else:
                print("Invalid choice")

        if player.get_hand_value() > 21:
            print("💥 Bust!")


    def play_round(self):
        self.com_player.add_card(self.deck.draw(), self.deck, self.players)
        self.com_player.add_card(self.deck.draw(), self.deck, self.players)
        print(f"\n🤖 {self.com_player.name}'s initial hand: ", self.com_player.hand[0])

        for player in self.players:
            self.player_round(player)

        print(f"\n🤖 {self.com_player.name}'s turn:")
        self.com_player.show_hand()
        while self.com_player.should_draw_card():
            self.com_player.add_card(self.deck.draw(), self.deck, self.players)
            print("|||",self.com_player.hand[-1], end=" ")
        if(len(self.com_player.hand) > 2):
            print("|||")
        print("\nHand value:", self.com_player.get_hand_value(), "\n")
        clear_timer_line()


        com_val = self.com_player.get_hand_value()
        if com_val > 21:
            print("💥 Dealer busts!")

        print("\n🎯 RESULTS:")
        for player in self.players:
            val = player.get_hand_value()
            if val <= 21 and (val > com_val or com_val > 21):
                print(f"✅ {player.name} WINS!")
                update_stats(self.stats, player.name, "win")
            elif val == com_val and val <= 21:
                print(f"🤝 {player.name} DRAWS!")
                update_stats(self.stats, player.name, "draw")
            else:
                print(f"❌ {player.name} LOSES!")
                update_stats(self.stats, player.name, "loss")
            player.reset_hand()
        save_stats(self.stats)
        self.com_player.reset_hand()

