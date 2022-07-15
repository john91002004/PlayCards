# -*- coding: utf-8 -*-
"""
Created on 2022-06-27

@author: Arcobaleno4869
"""
import unittest
from Card import Card
from Exceptions import InvalidCardException

class CardTest(unittest.TestCase):

    def setUp(self) -> None:
        self.SpadeQ = Card('spade', 'Q')
        self.Spade9 = Card('spade', '9')
        self.HeartQ = Card('heart', 'Q')
        return super().setUp()
    
    def testCardComparison(self): 
        self.assertEqual(self.SpadeQ, self.SpadeQ)
        self.assertGreaterEqual(self.SpadeQ, self.SpadeQ)
        self.assertGreater(self.SpadeQ, self.HeartQ)
        self.assertGreater(self.HeartQ, self.Spade9)

    def testInvalidCardShouldRaiseException(self):
        for item in [('dqwd', 'A'), ('club', '1')]: 
            with self.subTest(Card=item): 
                with self.assertRaises(InvalidCardException):
                    Card(item[0], item[1])
            

if __name__ == '__main__':
    unittest.main(verbosity=4)
