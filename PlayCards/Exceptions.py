# -*- coding: utf-8 -*-
"""
Created on 2022-06-27

@author: Arcobaleno4869
"""

class InvalidCardException(Exception):
    pass 
class NoCardsToPlayException(Exception):
    pass
class CheatException(Exception): 
    def __eq__(self, other): 
        if type(self) == type(other):
            return True if self.args == other.args else False 
        else: 
            return False 

        