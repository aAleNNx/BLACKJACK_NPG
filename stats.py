import json
import os

STATS_FILE = "data/stats.json"


def load_stats():
    if not os.path.exists(STATS_FILE):
        return {}
    with open(STATS_FILE, "r") as f:
        return json.load(f)


def save_stats(stats):
    with open(STATS_FILE, "w") as f:
        json.dump(stats, f, indent=4)


def init_player_stats(stats, player_name):
    if player_name not in stats:
        stats[player_name] = {"wins": 0, "losses": 0, "draws": 0}


def update_stats(stats, player_name, result):
    """
    result: "win", "loss", or "draw"
    """
    init_player_stats(stats, player_name)
    if result == "win":
        stats[player_name]["wins"] += 1
    elif result == "loss":
        stats[player_name]["losses"] += 1
    elif result == "draw":
        stats[player_name]["draws"] += 1


def reset_stats():
    """
    Usuwa wszystkie dane statystyczne (z pliku)
    """
    if os.path.exists(STATS_FILE):
        os.remove(STATS_FILE)
        print("Statystyki zostały zresetowane.")
    else:
        print("Nie znaleziono pliku statystyk.")


def display_stats(stats):
    if not stats:
        print("Brak statystyk do wyświetlenia.")
        return

    print("\n Statystyki graczy:")
    for player, data in stats.items():
        print(
            f"  {player}: {data['wins']} wygranych, {data['losses']} przegranych, {data['draws']} remisów"
        )
