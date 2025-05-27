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
