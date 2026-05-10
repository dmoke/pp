from math import comb

DECK_SIZE = 36
REDS = BLACKS = DECK_SIZE / 2
SUITS = 4
SUITE_SIZE = DECK_SIZE // SUITS  # 9
SIXES = SEVENS = EIGHTS = NINES = TENS = JACKS = QUEENS = KINGS = ACES = 4
FACE_CARDS_AMOUNT = 3 * SUITS
NUMBER_CARDS_AMOUNT = 5 * SUITS
ACES_AMOUNT = 1 * SUITS


# same suit on 6 card draws without replacement
AM = 6
prob = SUITS * comb(SUITE_SIZE, AM) / comb(DECK_SIZE, AM)     # C(n, k) = number of ways to choose k items from n, ignoring order
print(f"same suit on {AM} cards: {prob * 100:.3f}% or 1 in {1/prob:.0f}")

# 
