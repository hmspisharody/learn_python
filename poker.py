from itertools import product
import random

class Card:
	
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value
	def __repr__(self):
		return f"{self.value} of {self.suit}"
	
class Deck:
	count = 52
	suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
	values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
	def __init__(self):
		cards_list = list(product(Deck.suits, Deck.values))
		self.cards = [j + " of " + i for i,j in cards_list]
		
	def __repr__(self):
		return f"deck of {Deck.count} cards"
		
	def _deal(self, num):
		if Deck.count == 0:
			raise ValueError("All cards have been dealt")
		elif num>Deck.count:
			Deck.count = 0
		elif num<=Deck.count:
			Deck.count -= num
	
	def shuffle(self):
		if Deck.count == 52:
			random.shuffle(self.cards)
		else:
			raise ValueError("Only full decks can be shuffled")

	def deal_card(self):
		self._deal(1)
		return self.cards.pop(0)
	
	def deal_hand(self, num):
		self._deal(num)
		return [self.cards.pop(i) for i in range(num)]
	
		
deck1 = Deck()
print(deck1)
deck1.shuffle()
card = deck1.deal_card()
print(card)
hand = deck1.deal_hand(5)
print(hand)
print(deck1)



		
