from card import *
from deck import *

talia = Deck(1)
karta = Card("Diamonds", "J")

print(karta)

for i in range(40):
    a = talia.draw()
    print(a)
    if karta.suit == a.suit and karta.rank == a.rank:
        print("Jestes zajebisty! Próba:", i+1)
        break