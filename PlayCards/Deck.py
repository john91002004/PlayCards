# -*- coding: utf-8 -*-
"""
Created on 2022-06-27

@author: Arcobaleno4869
"""

from random import sample
from Constants import SUIT_LIST, VALUE_LIST
from Card import Card
from Exceptions import NoCardsToPlayException


class Deck: 
    def __init__(self):
        self.remainingCards = self.__createFiftyTwoCards() 

    def __createFiftyTwoCards(self): 
        tmp = [] 
        for suit in SUIT_LIST: 
            for value in VALUE_LIST: 
                tmp.append( Card(suit, value) )
        return tmp 

    def __isInRemainingCards(self, cardList:list): 
        for card in cardList: 
            if self.remainingCards.count(card) == 0 : 
                return False 
        return True 

    def __removeCards(self, cardList:list): 
        for card in cardList: 
            self.remainingCards.remove(card)
        
    def playCards(self, cardList:list): 
        if self.__isInRemainingCards(cardList): 
            self.__removeCards(cardList)
            return cardList 
        else: 
            raise NoCardsToPlayException('No cards to play!!!')
    
    def playRandom13Cards(self):
        index_list = self.__generateRandom13NumbersFromN( len(self.remainingCards) )
        card_list = self.__getCardsFromDeckAccordingToIndices(index_list)
        self.playCards(card_list)
        return card_list 

    def __generateRandom13NumbersFromN(self, n): 
        return sample(range(0, n),  13) 

    def __getCardsFromDeckAccordingToIndices(self, index_list):
        cards = []
        for index in index_list: 
            cards.append(self.remainingCards[index]) 
        return cards     

         
