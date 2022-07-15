# -*- coding: utf-8 -*-
"""
Created on 2022-06-27

@author: Arcobaleno4869
"""
from Player import Player 
from Card import Card

class ExpertPlayer(Player):
    
    def __init__(self, name):
        super().__init__(name) 
    
    def playCard(self): 
        return Card('spade', 'A')
