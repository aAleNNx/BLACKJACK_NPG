import random
from card import *
from computer import *
from deck import *


def apply_special_effect(card, player, deck, computer):
    if card.rank == "X":
        # Usuwa kartę przeciwnika
        effect_remove_card(computer)
    elif card.rank == "D":
        effect_multiplier(player)
        # Podwaja wartość następnej dobranej karty
    elif card.rank == "C":
        effect_copy_card(player)
        # Kopiuje poprzednio dobraną kartę
    elif card.rank == "Z":
        effect_draw_two(player, deck, computer)
        # Dobiera 2 karty


def effect_remove_card(computer):
    if computer.hand:
        removed_card = random.choice(computer.hand)
        computer.hand.remove(removed_card)
        print(f"{computer.name} traci kartę: {removed_card}")
    else:
        print(f"{computer.name} nie ma kart do usunięcia.")


def effect_draw_two(player, deck, computer):
    for i in range(2):
        extra_card = deck.draw()
        if extra_card:
            player.add_card(extra_card, deck)
        else:
            print("Brak kart w talii.")


def effect_multiplier(player):
    player.next_card_mult = 2.0


def effect_copy_card(player):
    if len(player.hand) >= 2:
        # Ostatnia normalna karta to przedostatnia (ostatnia to karta specjalna C)
        last_card = player.hand[-2]
        copied_card = Card(rank=last_card.rank, suit=last_card.suit)
        player.add_card(copied_card)
        print(
            f"{player.name} używa C: kopiuje kartę {last_card} → otrzymuje {copied_card}"
        )
    else:
        print(f"{player.name} nie ma żadnej karty do skopiowania.")
