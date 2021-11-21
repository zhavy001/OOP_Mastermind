#
# File: Player.py
# Description: This file contains the Player details to be inherited by Human and Computer Player.
# Author: Vivienne Zhang
# Student ID: 110146861
# Email ID: zhavy001
# This is my own work as defined by the University's Academic Misconduct Policy.
#

from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, name):
        self.__name = name
    
    @abstractmethod
    def guessCode(self):
        pass
    
    @abstractmethod
    def setCode(self):
        pass
    
    def getName(self):
        return self.__name