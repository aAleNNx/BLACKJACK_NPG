from card import Card
from deck import Deck
import os
from stats import load_stats ,save_stats,display_stats,reset_stats,update_stats


def play_game(name,stats):
    while True:
        try:
            num_decks = int(input("Z ilu talii ma się składać deck? (np. 1, 2, 3): "))
            if num_decks <= 0:
                raise ValueError
            break
        except ValueError:
            print("Podaj poprawną, dodatnią liczbę całkowitą.")

    target_card = Card("Diamonds", "J")
    deck = Deck(num_decks)

    print(f"\n{name}, Twoja karta docelowa to: {target_card}")
    print("Losuję karty...")

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

    if found:
        print(f"\n🎉 {name}, jesteś bardzo fajny! Trafiłeś w {attempts} próbie.")
        update_stats(stats, name, "win")
    else:
        print(f"\n😢 {name}, niestety nie udało się znaleźć {target_card}.")
        update_stats(stats, name, "loss")

    save_stats(stats)


def main():
    os.makedirs("data", exist_ok=True)

    stats = load_stats()

    name = input("Podaj swoje imię: ")
    while True:
        print("\n📋 MENU:")
        print("1. Zagraj")
        print("2. Wyświetl statystyki")
        print("3. Zresetuj statystyki")
        print("4. Wyjdź")
        choice = input("Wybierz opcję (1-4): ")

        if choice == "1":
            play_game(name, stats)
        elif choice == "2":
            display_stats(stats)
        elif choice == "3":
            confirm = input("Na pewno zresetować statystyki? (t/n): ").lower()
            if confirm == "t":
                reset_stats()
                stats = {}
        elif choice == "4":
            print("👋 Do zobaczenia!")
            break
        else:
            print("Nieprawidłowa opcja. Wybierz 1, 2, 3 lub 4.")

if __name__ == "__main__":
    main()
