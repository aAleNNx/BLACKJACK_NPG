class Card:
    def __init__(self, suit: str,  rank: str, multiplier = 1, is_special: bool = False):
        self.suit = suit
        self.rank = rank
        self.is_special = is_special
        self.multiplier = multiplier

    def __str__(self):
        if self.is_special:
            return f"[Special card: {self.rank}]"
        return f"{self.suit} {self.rank}"

    def get_value(self) -> int:
        if self.is_special:
            return 0
        if self.rank in ['J', 'Q', 'K']:
            return 10
        elif self.rank == 'A':
            return 11
        else:
            return int(self.rank)

    def is_ace(self):
        return self.rank == 'A'

    def to_dict(self):
        return {
            "suit": self.suit,
            "rank": self.rank,
            "is_special": self.is_special
        }

    @staticmethod
    def from_dict(data):
        return Card(data["suit"], data["rank"], data["is_special"])