from card import Card

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []        
        
    def receive(self, card):
        self.cards.append(card)
    
    def total(self):
        total = 0
        aces = 0
        for c in self.cards:
            if c.symbol == 'A':
                aces += 1
            total += c.value
        
        while aces > 0:
            if total > 21:
                total = total - 10 + 1
                aces -= 1
            else:
                break

        return total

    def __str__(self):
        ret = ''
        for c in self.cards:
            ret += str(c) + ' '
        return '{} -> {} / {}'.format(self.name, ret, self.total())
    