# -*- coding: utf-8 -*-
"""
Created on 2022-06-27

@author: Arcobaleno4869
"""

import unittest
from Judger import Judger
from Card import Card

class JudgerTest(unittest.TestCase): 

    def setUp(self) -> None:
        self.Judger = Judger()
        self.Cards = [Card('spade', 'A'), Card('spade', '2'), Card('diamond', 'J'), Card('club', 'J')]
        return super().setUp()

    def testBiggestOfCards(self): 
        BiggestCard = self.Judger.judgeBiggest(self.Cards)
        self.assertEqual(BiggestCard, Card('spade', 'A'))


if __name__ == '__main__':
    unittest.main(verbosity=4)