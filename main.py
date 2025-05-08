from card import *
from deck import *

talia = Deck()
karta = Card("Diamonds", "J")

print(karta)
print(talia.draw())

if karta == talia.draw():
    print("Jestes zajebisty!")