#
# File: Code.py
# Description: This file contains functionality to provide feedback for a singular code.
# Author: Vivienne Zhang
# Student ID: 110146861
# Email ID: zhavy001
# This is my own work as defined by the University's Academic Misconduct Policy.
#

class Feedback():
    def __init__(self):
        pass

    def setKeypeg(self, code, correctCode):
        """
        Functionality to provide feedback for a singular code.

        Parameters:
            string code: The attempted code by a player.
            string correctCode: The code at which they are attempting to break.

        Returns:
            string feedback: The corresponding keypegs to the players code.
        """
        feedback = ""

        for i in range(len(code)):
            if(code[i] in correctCode and code[i] in correctCode[i]):
                feedback += "K "
            elif(code[i] in correctCode):
                feedback += "W "

        return feedback