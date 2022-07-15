# -*- coding: utf-8 -*-
"""
Created on 2022-06-27

@author: Arcobaleno4869
"""
import unittest
from Exceptions import CheatException
from Game import Game
from Player import Player
from Card import Card
from ExpertPlayer import ExpertPlayer

class GameTest(unittest.TestCase): 

    def setUp(self) -> None:
        self.players = [] 
        self.players.append(Player('John'))
        self.players.append(Player('Mary'))
        self.players.append(Player('Jenny'))
        self.players.append(Player('Bob'))

        self.game = Game(self.players) 
        return super().setUp()

    def testGameStartsWithFourPlayers(self): 
        self.assertEqual( len(self.game.Players), 4 )
        for player in self.game.Players:
            with self.subTest(player=player): 
                self.assertIsInstance(player, Player)

    def testPlayerWithThirteenCardsAfterDistribute(self):
        for player in self.game.Players:
            with self.subTest(player=player):
                self.assertEqual( len(player.remainingCards), 13)
                for i in range(0,13):
                    with self.subTest(i=i): 
                        self.assertIsInstance(player.remainingCards[i], Card)

    def testPlayerWith12CardsAfterOneRound(self): 
        self.game.goOneRound()
        for player in self.game.Players: 
            with self.subTest(player = player):
                self.assertEqual( len(player.remainingCards) , 12 ) 

    def testPlayerWith0CardsAfter13Rounds(self): 
        self.game.goAllRounds()
        for player in self.game.Players: 
            with self.subTest(player = player):
                self.assertEqual( len(player.remainingCards) , 0 ) 

    def testRecordSequenceForOneRound(self):
        self.game.goOneRound()
        self.assertGreater( self.game.RoundRecorder.Records[0][0]['Card'], self.game.RoundRecorder.Records[0][1]['Card'])
        self.assertGreater( self.game.RoundRecorder.Records[0][0]['Card'], self.game.RoundRecorder.Records[0][2]['Card'])
        self.assertGreater( self.game.RoundRecorder.Records[0][0]['Card'], self.game.RoundRecorder.Records[0][3]['Card'])

    def testWinner(self): 
        # 因為不一定有贏家，所以重開賽局到有贏家為止。
        while True: 
            self.setUp()
            self.game.goAllRounds() 
            if self.game.RoundRecorder.Winner != None : 
                break 
        # 有贏家之後，就看看他贏的回合數是不是真的高於其他人。
        IndexOfWinner = self.game.Players.index( self.game.RoundRecorder.Winner ) 
        WinnerWinRound = self.game.RoundRecorder.WinRounds[IndexOfWinner]
        for i in range(0, len(self.game.Players)): 
            with self.subTest(player = self.game.Players[i]): 
                if i == IndexOfWinner : 
                    pass
                else: 
                    PlayerWinRound = self.game.RoundRecorder.WinRounds[i]
                    self.assertGreater(WinnerWinRound, PlayerWinRound) 

    def test20Games(self):
        for i in range(0, 20):
            self.game.goAllRounds() 
            self.game.updateRound() 
            self.game.restart() 
        
        self.game.GameRecorder.decideWinner()
        Winner = self.game.GameRecorder.Winner
        WinnerAssertion = Winner in self.players or Winner == None 
        self.assertTrue(WinnerAssertion)

    def testBreakingRule(self): 
        players = [] 
        players.append(ExpertPlayer('John'))
        players.append(Player('Mary'))
        players.append(Player('Jenny'))
        players.append(Player('Bob'))
        self.game = Game(players)

        with self.assertRaises(CheatException):
            self.game.goAllRounds() 



if __name__ == '__main__':
    unittest.main(verbosity=4)
