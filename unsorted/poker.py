import random

class Deck:
    def __init__(self):
        self.cards = self.initiate_cards()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, number):
        cards_to_deal = [self.cards.pop() for i in range(number)]
        return cards_to_deal

    @staticmethod
    def initiate_cards():
        suites = ['heart', 'clubs', 'spade', 'diamond']
        card_count_per_suite = 13
        cards = [(suite, value) for value in range(1, 14) for suite in suites]
        return cards

    # from itertools import product, *product('123123').split()
deck = Deck()
print(len(deck.cards), deck.cards)
deck.shuffle()
print('\n post shuffle', deck.cards)

hand = deck.deal(3)
print(f'my hand is: {hand}, deck size is {')


# # i. fully OO
# deck = Deck()
# deck.shuffle()
# hand_1, hand_2 = deck.deal(2), deck.deal(2)
# flop = deck.deal(3)
# turn = deck.deal(1)
# river = deck.deal(1)
# if player1.with_(flop, turn, river) > player2.with_(flop, turn, river):
#     print('Player #1 wins!')
# else:
#     print('Player #2 wins!')