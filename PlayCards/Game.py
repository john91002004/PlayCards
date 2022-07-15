# -*- coding: utf-8 -*-
"""
Created on 2022-06-27

@author: Arcobaleno4869
"""

from Deck import Deck
from Judger import Judger
from Recorder import Recorder

class Game(): 
    def __init__(self, players):
        self.Round = 0 
        self.Players = players
        self.Deck = Deck()
        self.RoundRecorder = Recorder(self.Players)
        self.GameRecorder = Recorder(self.Players)
        self.Judger = Judger(self.Players)
        self.__distributeCards()

        self.__CardListInOneRound = []  

    def __distributeCards(self): 
        for player in self.Players:
            card_list = self.Deck.playRandom13Cards()
            player.getCards(card_list)
            self.Judger.PlayerCards[player] = card_list 

    def goOneRound(self): 
        self.__callEveryPlayerPlayCard() 
        self.__checkPlayerCardInOneRoundIfCheat() 
        self.__callEveryPlayerPlayCardAndCheckIfCheat()
        self.__CardListInOneRound.sort( key=lambda s:s['Card'], reverse=True )
        self.RoundRecorder.updateRecord(self.__CardListInOneRound)
        self.updateRound() 

    def __checkPlayerCardInOneRoundIfCheat(self):
        for item in self.__CardListInOneRound:
            player = item.key 
            card = item.value 
            self.Judger.raiseCheatExceptionIfCheatWhenPlayerPlayCard(player, card)

    def __callEveryPlayerPlayCard(self):
        for player in self.Players: 
            card = player.playCard() 
            self.__CardListInOneRound.append( { 'Player': player, 'Card': card } )

    def updateRound(self): 
        self.Round += 1
        if self.Round == 13: 
            self.RoundRecorder.decideWinner() 
            winner = self.RoundRecorder.Winner 
            if winner != None : 
                self.GameRecorder.recordPlayerWinRound(winner)

    def goAllRounds(self): 
        for i in range(0,13): 
            self.goOneRound() 

    def restart(self):
        self.Round = 0 
        self.Deck = Deck()
        self.RoundRecorder = Recorder(self.Players)
        self.__distributeCards() 
