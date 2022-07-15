# -*- coding: utf-8 -*-
"""
Created on 2022-06-27

@author: Arcobaleno4869
"""

from Constants import SUIT_LIST, VALUE_LIST
from Exceptions import InvalidCardException

class Card: 
    def __init__(self, suit, value): 
        s,v = self.__normalizeSuitAndValue(suit, value) 
        self.__setCard(s, v)

    # 當print()函式被呼叫時，會調用__str__
    def __str__(self):  
        return f"('{self.__Suit}','{self.__Value}')"

    # 當物件被表示時，會調用__repr__，如果沒有定義，就會顯示物件所在的記憶體位置
    def __repr__(self):
        return f"('{self.__Suit}','{self.__Value}')"

    def __eq__(self, other): 
        return True if self.getCard() == other.getCard() else False             

    def __lt__(self, other): 
        value_comparison = self.__valueComparision(self.__Value, other.__Value)
        suit_comparison = self.__suitComparison(self.__Suit, other.__Suit)
        if value_comparison == -1: 
            return True 
        elif value_comparison == 1: 
            return False  
        else: 
            return True if suit_comparison == -1 else False 

    def __le__(self, other): 
        return True if self.__eq__(other) or self.__lt__(other) else False 

    def __valueComparision(self, v1, v2): 
        if self.__valueIndex(v1) < self.__valueIndex(v2): 
            return -1 
        elif self.__valueIndex(v1) > self.__valueIndex(v2): 
            return 1 
        else :
            return 0 

    def __suitComparison(self, s1, s2): 
        if self.__suitIndex(s1) < self.__suitIndex(s2): 
            return -1 
        elif self.__suitIndex(s1) > self.__suitIndex(s2): 
            return 1 
        else :
            return 0 

    def __valueIndex(self, v): 
        return VALUE_LIST.index(v)

    def __suitIndex(self, s): 
        return SUIT_LIST.index(s)

    def __normalizeSuitAndValue(self, suit, value):
        return suit.lower(), str(value).upper()

    def __setCard(self, suit, value): 
        self.__setSuit( suit )
        self.__setValue( value )

    def __setSuit(self, suit):
        if not self.__isSuitIllegal(suit) :
            self.__Suit = suit
        else: 
            raise InvalidCardException("Illegal card suit!!!")

    def __setValue(self, value):
        if not self.__isValueIllegal(value) :
            self.__Value = value 
        else: 
            raise InvalidCardException("Illegal card value!!!")

    def __isSuitIllegal(self, suit): 
        return True if suit not in SUIT_LIST else False 

    def __isValueIllegal(self, suit): 
        return True if suit not in VALUE_LIST else False 

    def getCard(self): 
        return (self.__Suit, self.__Value) 

