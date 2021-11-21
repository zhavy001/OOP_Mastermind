#
# File: HumanPlayer.py
# Description: This file contains the Human Player details and overrides the methods defined in the Player class.
# Author: Vivienne Zhang
# Student ID: 110146861
# Email ID: zhavy001
# This is my own work as defined by the University's Academic Misconduct Policy.
#

from classes.Player import Player

class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.__totalScore = 0
        self.__gamesPlayed = 0

    def guessCode(self, codeMarbles):
        print("Please enter the code:")
        guess = input()

        while(not codeMarbles.isValidCodeMarble(guess)):
            print("Invalid code.\nIt must be exactly four characters, each can be R, G, B, Y, W, or K.")
            print("Please enter the code:")
            guess = input()

        return guess

    def setCode(self, codeMarbles):
        print("Please enter the code:")
        code = input()

        while(not codeMarbles.isValidCodeMarble(code)):
            print("Invalid code.\nIt must be exactly four characters, each can be R, G, B, Y, W, or K.")
            print("Please enter the code:")
            code = input()

        return code
    
    def incrementTotalScore(self, score):
        self.__totalScore += score

    def incrementGamesPlayed(self):
        self.__gamesPlayed += 1

    def getTotalScore(self):
        return self.__totalScore

    def getGamesPlayed(self):
        return self.__gamesPlayed