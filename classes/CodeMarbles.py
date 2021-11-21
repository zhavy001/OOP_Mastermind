#
# File: CodeMarbles.py
# Description: This file contains functionality to verify a Player attempt.
# Author: Vivienne Zhang
# Student ID: 110146861
# Email ID: zhavy001
# This is my own work as defined by the University's Academic Misconduct Policy.
#

class CodeMarbles():
    def __init__(self):
        self.__codeMarbles = ['R', 'G', 'B', 'Y', 'W', 'K']
    
    def isValidCodeMarble(self, code):
        """
        Functionality to check if a specified code is valid.

        Parameters:
            string code: A users code to be verified.
        """
        if(len(code) > 4):
            return False
            
        for marble in code:
            if(marble not in self.__codeMarbles):
                return False
        return True

    def getCodeMarbles(self):
        return self.__codeMarbles