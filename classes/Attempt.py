#
# File: Code.py
# Description: This file contains an attempt object.
# Author: Vivienne Zhang
# Student ID: 110146861
# Email ID: zhavy001
# This is my own work as defined by the University's Academic Misconduct Policy.
#

from classes.Feedback import Feedback

class Attempt():
    def __init__(self):
        self.__feedback = Feedback()

    def getAttempt(self, code, correctCode):
        return self.__feedback.setKeypeg(code, correctCode)