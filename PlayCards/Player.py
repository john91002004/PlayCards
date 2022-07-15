# -*- coding: utf-8 -*-
"""
Created on 2022-06-27

@author: Arcobaleno4869
"""

class Player():
    
    def __init__(self, name):
        self.name = name 
        self.remainingCards = []

    def __repr__(self):
        return self.name 

    def __eq__(self, other): 
        if type(self) == type(other): 
            return True if self.name == other.name else False 
        else : 
            return False 

    def __hash__(self):
        return hash(str(self))

    def getCards(self, card_list): 
        self.remainingCards.extend(card_list)
    
    def playCard(self): 
        card = self.remainingCards.pop()
        return card 