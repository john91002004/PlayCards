# -*- coding: utf-8 -*-
"""
Created on 2022-06-27

@author: Arcobaleno4869
"""

from Exceptions import CheatException


class Judger():

    def __init__(self, players): 
        self.__initPlayerCardsDict__(players)

    def __initPlayerCardsDict__(self, players):
        self.PlayerCards = {} 
        for player in players: 
            self.PlayerCards[player] = []

    def raiseCheatExceptionIfCheatWhenPlayerPlayCard(self, player, card): 
        if self.PlayerCards[player].count(card) == 0: 
            raise CheatException(f'{player} got no {card} but plays it. {player} is CHEATING!!!')
        else:
            self.PlayerCards[player].remove(card)

    def judgeBiggest(self, card_list): 
        sorted(card_list)
        return card_list[0]
    

