from card import Card
from deck import Deck
import os


def main():
    os.makedirs("data", exist_ok=True)

    # 1. Powitanie i dane wejściowe
    name = input("Podaj swoje imię: ")
    while True:
        try:
            num_decks = int(input("Z ilu talii ma się składać deck? (np. 1, 2, 3): "))
            if num_decks <= 0:
                raise ValueError
            break
        except ValueError:
            print("Podaj poprawną, dodatnią liczbę całkowitą.")

    # 2. Inicjalizacja gry
    target_card = Card("Diamonds", "J")
    deck = Deck(num_decks)

    print(f"\n{name}, Twoja karta docelowa to: {target_card}")
    print("Losuję karty...")

    # 3. Losowanie kart
    attempts = 0
    found = False
    while True:
        drawn_card = deck.draw()
        attempts += 1
        print(f"[{attempts}] Wylosowana karta: {drawn_card}")
        if drawn_card.suit == target_card.suit and drawn_card.rank == target_card.rank:
            found = True
            break
        if deck.is_empty():
            print("Skończyły się karty w talii.")
            break

    # 4. Statystyki końcowe
    if found:
        print(f"\n🎉 {name}, jesteś bardzo fajny Trafiłeś w {attempts} próbie.")
    else:
        print(f"\n😢 {name}, niestety nie udało się znaleźć {target_card}.")


if __name__ == "__main__":
    main()
