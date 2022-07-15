# -*- coding: utf-8 -*-
"""
Created on 2022-06-27

@author: Arcobaleno4869
"""
import unittest
from Game import Game
from Player import Player
from ExpertPlayer import ExpertPlayer

class GameTest(unittest.TestCase): 

    def setUp(self) -> None:
        self.players = [] 
        self.players.append(ExpertPlayer('John'))
        self.players.append(Player('Mary'))
        self.players.append(Player('Jenny'))
        self.players.append(Player('Bob'))

        self.game = Game(self.players) 
        return super().setUp()

    def test20Games(self):
        for i in range(0, 20):
            self.game.goAllRounds() 
            self.game.updateRound() 
            self.game.restart() 
        
        self.game.GameRecorder.decideWinner()
        Winner = self.game.GameRecorder.Winner
        WinnerAssertion = Winner in self.players or Winner == None 
        self.assertTrue(WinnerAssertion)

if __name__ == '__main__':
    unittest.main(verbosity=4)
