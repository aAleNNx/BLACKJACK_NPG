from game import *
import os

def play_game(stats):
    try:
        liczba_graczy = int(input("Podaj liczbę graczy (1-5): "))
        if liczba_graczy < 1 or liczba_graczy > 5:
            print("❗ Liczba graczy musi być od 1 do 5.")
            return
    except ValueError:
        print("❗ Błędna liczba graczy.")
        return
    players = []
    for i in range(liczba_graczy):
        name = input(f"Podaj imię gracza {i+1}: ")
        players.append(Player(name))
    com = ComputerPlayer("Dealer")
    game = Game(com, *players, deck_count=2, time_limit=10, stats=stats)
    try:
        rundy = int(input("Ile rund chcesz zagrać?: "))
        if rundy <= 0:
            print("❗ Liczba rund musi być większa niż 0.")
            return
    except ValueError:
        print("❗ Błędna liczba rund.")
        return
    game.run(rundy)

def main():
    os.makedirs("data", exist_ok=True)
    stats = load_stats()

    while True:
        print("\n📋 MENU:")
        print("1. Zagraj")
        print("2. Wyświetl statystyki")
        print("3. Zresetuj statystyki")
        print("4. Wyjdź")
        choice = input("Wybierz opcję (1-4): ")

        if choice == "1":
            play_game(stats)
        elif choice == "2":
            display_stats(stats)
        elif choice == "3":
            confirm = input("Na pewno zresetować statystyki? (t/n): ").lower()
            if confirm == "t":
                reset_stats()
                stats = {}
                print("✅ Statystyki zresetowane.")
        elif choice == "4":
            print("👋 Do zobaczenia!")
            break
        else:
            print("❗ Nieprawidłowa opcja. Wybierz 1, 2, 3 lub 4.")
