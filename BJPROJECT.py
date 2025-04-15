def KARTA(wartosc, symbol):
    for i in range(11):
        print("-", end="")
    print(f"\n| {wartosc}       |")
    print("|         |")
    print(f"|    {symbol}    |")
    print("|         |")
    print(f"|       {wartosc} |")
    for i in range(11):
        print("-", end="")
    print("\n")
        
KARTA("J", "♠")
KARTA("Q","♦")
