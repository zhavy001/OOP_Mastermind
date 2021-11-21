#
# File: DecodingBoard.py
# Description: This file contains the players code setting and code breaking loops.
# Author: Vivienne Zhang
# Student ID: 110146861
# Email ID: zhavy001
# This is my own work as defined by the University's Academic Misconduct Policy.
#

from classes.Code import Code

class DecodingBoard():
    def __init__(self):
        self.__setCodes = {}

    def setPlayerCodes(self, playerList, codeMarbles):
        """
        Functionality to prompt each Codemaker to set a code for each Codemaker.

        Parameters:
            Player[] playerList: The array of active players in the game.
        """
        for player in playerList:
            self.__setCodes[player.getName()] = None

        curCodeBreakerIndex = 1
        for player in playerList:
            curCodeBreaker = playerList[curCodeBreakerIndex]

            print(f"* {player.getName()}'s turn to set code for {curCodeBreaker.getName()} to break.")
            code = Code(player.setCode(codeMarbles))
            self.__setCodes[curCodeBreaker.getName()] = code.getCode()

            print(f"The code is now set for {curCodeBreaker.getName()} to break.\n")

            curCodeBreakerIndex += 1
            if(curCodeBreakerIndex == len(playerList)):
                curCodeBreakerIndex = 0

    def getPlayerCode(self, username):
        """
        Functionality to retrieve a CodeBreakers code in which they need to break.

        Parameters:
            string username: The username of the user to retrieve.
        """
        return self.__setCodes.get(username)