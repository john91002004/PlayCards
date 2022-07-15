# -*- coding: utf-8 -*-
"""
Created on 2022-06-27

@author: Arcobaleno4869
"""
import unittest

from Card import Card
from Deck import Deck

class DeckTest(unittest.TestCase):

    def setUp(self) -> None:
        self.Deck = Deck() 
        return super().setUp()

    def testDeckStartsWithFiftyTwoCards(self): 
        self.assertEqual( len(self.Deck.remainingCards), 52) 

    def testPlayFourOfKindShouldBe47Cards(self):
        FourOfKind = [Card('spade', 'A'), Card('heart', 'A'), Card('diamond', 'A'), Card('club', 'A'), Card('spade', 'K')]
        self.Deck.playCards(FourOfKind)
        self.assertEqual( len(self.Deck.remainingCards), 47 ) 

    def testPlayAllCardsShouldBeNoCards(self): 
        AllCards = self.Deck.remainingCards.copy()
        self.Deck.playCards(AllCards)
        self.assertEqual( len(self.Deck.remainingCards), 0 ) 

if __name__ == '__main__':
    unittest.main(verbosity=4)
