# -*- coding: utf-8 -*-
"""
Created on 2022-06-27

@author: Arcobaleno4869
"""

class Recorder(): 
    def __init__(self, players):
        self.Players = players 
        self.Records = [] 
        self.WinRounds = [ 0 for player in players ]
        self.Winner = None 
        
    def recordPlayerWinRound(self, player):
        IndexOfPlayer = self.Players.index( player ) 
        self.WinRounds[IndexOfPlayer] += 1

    def decideWinner(self): 
        MostWinningRound = max(self.WinRounds)
        # 單獨一個才算贏家
        if self.WinRounds.count(MostWinningRound) == 1: 
            IndexOfWinner = self.WinRounds.index(MostWinningRound)
            self.Winner = self.Players[IndexOfWinner]
    
    def updateRecord(self, card_list): 
        self.Records.append(card_list)
        self.recordPlayerWinRound(card_list[0]['Player'])
    
    
