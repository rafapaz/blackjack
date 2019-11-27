from card import Card
from deck import Deck
from player import Player

class BlackJack:
    def __init__(self):
        self.deck = Deck()    
        self.deck.shuffle()
        self.dealer = Player('Dealer')
        self.dealer.receive(self.deck.give())

        self.player = Player('Jogador 1')
        self.player.receive(self.deck.give())
        self.player.receive(self.deck.give())
    
    def hit(self):
        while True:
            option = input('Press (H)it or (S)tand: ')
            if option.lower() == 'h':
                self.player.receive(self.deck.give())
                self.show_table()
                if self.player.total() > 21:
                    print('BUST!')
                    return False
            else:
                return True

    def show_table(self):
        print(' ')
        print(self.dealer)
        print(self.player)

    def dealer_plays(self):
        while self.dealer.total() < self.player.total():
            self.dealer.receive(self.deck.give())
    
    def final_result(self):
        if self.dealer.total() > 21 or self.player.total() > self.dealer.total():
            print('YOU WIN!')        
        elif self.player.total() == self.dealer.total():
            print('DRAW!')
        else:
            print('YOU LOSE!')

    def continue_game(self):
        game = input('Continue playing? (Y)es or (N)o: ')
        return True if game.lower() == 'y' else False
