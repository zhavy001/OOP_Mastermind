#
# File: ComputerPlayer.py
# Description: This file contains the Computer Player details and overrides the methods defined in the Player class.
# Author: Vivienne Zhang
# Student ID: 110146861
# Email ID: zhavy001
# This is my own work as defined by the University's Academic Misconduct Policy.
#

from classes.Player import Player

import random

class ComputerPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def guessCode(self, codeMarbles):
        """
        This function randomly selects 4 charactes from the array of valid characters,
        and appends them to a string named guess.
        """
        guess = ""
        
        for _ in range(4):
            guess += codeMarbles.getCodeMarbles()[random.randint(0, len(codeMarbles.getCodeMarbles()) - 1)]

        return guess

    def setCode(self, codeMarbles):
        """
        This function randomly selects 4 charactes from the array of valid characters,
        and appends them to a string named code.
        """
        code = ""
        
        for _ in range(4):
            code += codeMarbles.getCodeMarbles()[random.randint(0, len(codeMarbles.getCodeMarbles()) - 1)]

        return code