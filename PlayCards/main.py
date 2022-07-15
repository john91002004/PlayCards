# -*- coding: utf-8 -*-
"""
Created on 2022-06-27

@author: Arcobaleno4869
"""
from Game import Game
from Player import Player
from ExpertPlayer import ExpertPlayer

N = 20
players = [ExpertPlayer('John'), Player('Yuri'), Player('Jenny'), Player('Mary')]
game = Game(players) 

# Run N Games 
for i in range(0, 100):
    game.goAllRounds() 
    game.updateRound() 
    game.restart()

game.GameRecorder.decideWinner() 

# Print results 
for player in game.Players: 
    print(player, end='\t')
print()
for WinRound in game.GameRecorder.WinRounds: 
    print(WinRound, end='\t')
print()
print(f'Final Winner: {game.GameRecorder.Winner}')
