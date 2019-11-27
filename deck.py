import random
from card import Card

class Deck:
    def __init__(self):
        self.naipes = ['heart', 'diamond', 'club', 'spade']
        self.symbols = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']    
        self.cards = []
        
        for n in self.naipes:
            for i,s in enumerate(self.symbols):
                self.cards.append(Card(n, s, int(s) if i <= 8 else 10))
        
    def shuffle(self):
        random.shuffle(self.cards)

    def give(self):
        return self.cards.pop()

    def __str__(self):
        ret = ''
        for c in self.cards:
            ret += str(c) + ' '
        return ret
