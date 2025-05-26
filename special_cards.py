import random

def apply_special_effect(card, player, deck, opponent):
    if card.rank == "JOKER":
    #funkcjonalnosc zdefiniowana w funkcji calculate_hand_value()
        continue
    elif card.rank == "X":
        #Usuwa kartę przeciwnika
        effect_remove_card(computer)
    elif card.rank == "D":
        effect_draw_two(player)
        #Podwaja wartość następnej dobranej karty
    elif card.rank == "C":
        effect_copy_card(player)
        #Kopiuje poprzednio dobraną kartę
    elif card.rank == "Z":
        #Dobiera 2 karty

def effect_remove_card(computer):
    #trzeba dopisac computer.py

def effect_draw_two(player, deck):
    for i in range(2):
        extra_card = deck.draw()
        if extra_card:
            player.add_card(extra_card)
        else:
            print("Brak kart w talii.")

def effect_copy_card(player):
    player.next_card_mult = 2.0
