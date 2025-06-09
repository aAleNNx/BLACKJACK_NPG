import random
from card import *
from deck import *



def apply_special_effect(card, player, deck, computer):
    if card.rank == "X":
        #Usuwa kartę przeciwnika
        effect_remove_card(computer)
    elif card.rank == "D":
        effect_multiplier(player)
        #Podwaja wartość następnej dobranej karty
    elif card.rank == "C":
        effect_copy_card(player)
        #Kopiuje poprzednio dobraną kartę
    elif card.rank == "Z":
        effect_draw_two(player, deck, computer)
        #Dobiera 2 karty
    elif card.rank == "JOKER":
        effect_change_value(player)
        #Zmienia wartość jokera

def effect_remove_card(*computer):
        player = random.choice(computer)
        removed_card = random.choice(player.hand)
        player.hand.remove(removed_card)
        print(f"{player.name} traci kartę: {removed_card}")
        print(f"{player.name} nie ma kart do usunięcia.")


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
        print(f"{player.name} używa C: kopiuje kartę {last_card} → otrzymuje {copied_card}")
    else:
        print(f"{player.name} nie ma żadnej karty do skopiowania.")

def effect_change_value(player):
    player.show_hand()
    while True:
        choice = input("Wybierz wartość JOKERA od 1 do 10: ")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= 10:
                player.hand[-1].rank = choice
                player.hand[-1].is_special = False
                return
            else:
                print("Liczba spoza zakresu. Spróbuj jeszcze raz.")
        else:
            print("To nie jest liczba. Spróbuj jeszcze raz.")