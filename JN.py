def KARTA(wartosc):
    for i in range(10):
        print("-", end="")
    print(f"\n| {wartosc}      |")
    for i in range(3):
        print("|        |")
    print(f"|      {wartosc} |")
    for i in range(10):
        print("-", end="")
        
KARTA("J")
