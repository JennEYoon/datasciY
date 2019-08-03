import random

deck = list(range(0, 52))
print("deck", deck)

random.shuffle(deck)
print("shuffled deck", deck)

hand1 = deck[0:13] # first 13 cards goes into hand1
hand2 = deck[13:26]  # second 13 cards goes into hand2, etc.
print("hand1", hand1, "hand2", hand2)
# Later you can select every 4th card from the list to simulate 
# dealing to each player.

# Use a dictionary to map numbers to cards, full 52 cards in a deck.
# You don't need this step to calculate scores, but it's to help you debug.
# All diamonds first, then spades, etc.
deckdict = {0:['D', 'Ace'], 1:['D', '2'], 2:['D', 3], 13:['S', 'Ace'], 14:['S', '2']}  
# Here's how to lookup from a dictionary given a card number.
card = deckdict[2]
print("card face", card)

# Then calculate score.
# Generally, use numbers and lists to do all logic, 
# and dictionary just to lookup the card value for, for your eyes.
