#
# File: Game.py
# Description: This file contains details and functionality for a singular round of WoM.
# Author: Vivienne Zhang
# Student ID: 110146861
# Email ID: zhavy001
# This is my own work as defined by the University's Academic Misconduct Policy.
#

from classes.ComputerPlayer import ComputerPlayer
from classes.DecodingBoard import DecodingBoard
from classes.Code import Code
from classes.CodeMarbles import CodeMarbles
from classes.Attempt import Attempt
from classes.HumanPlayer import HumanPlayer

class Game:
    def __init__(self):
        self.__playerAttempts = {}
        self.__codeMarbles = CodeMarbles()
        self.__previousAttempts = {}
        self.__activePlayers = {}

    def startGame(self, numAttempts, playerList):
        """
        Functionality to run a game of WoM.

        Parameters:
            int numAttempts: The number of attempts each player has left.
            Player[] playerList: The array of active players in the game.
        """
        for player in playerList:
            self.__playerAttempts[player.getName()] = numAttempts
            self.__previousAttempts[player] = {}
            self.__activePlayers[player] = True

            if(isinstance(player, HumanPlayer)):
                player.incrementGamesPlayed()

        decodingBoard = DecodingBoard()
        decodingBoard.setPlayerCodes(playerList, self.__codeMarbles)

        gameFinished = False
        while(not gameFinished):
            for player in self.__previousAttempts:
                if self.__activePlayers.get(player) == True:
                        # The number of previous attempts and the number of attempts remaining.
                        previousAttempts = numAttempts - self.__playerAttempts.get(player.getName())
                        attemptsLeft = self.__playerAttempts.get(player.getName())

                        print(f"* {player.getName()}'s turn to guess the code.")
                        print(f"Previous attempts: {previousAttempts}")

                        # Loops through the previous attempts of a player,
                        # if the number of previous attempts if greater than 1.
                        if(previousAttempts > 0):
                            print("==============")
                            print("Code Feedback")
                            print("==============")
                            for attempt in self.__previousAttempts.get(player):
                                print(f"{attempt} {self.__previousAttempts.get(player)[attempt]}")
                            print("==============")

                        print(f"Attempts left: {attemptsLeft}")

                        # Verifys the marbles in the code.
                        code = Code(player.guessCode(self.__codeMarbles))

                        if(isinstance(player, ComputerPlayer)):
                            print(f"{player.getName()}'s guess: {code.getCode()}")

                        # Checks if the code entered is the correct code.
                        if(code.getCode() == decodingBoard.getPlayerCode(player.getName())):
                            previousAttempts += 1

                            print(f"{player.getName()} broke the code in {previousAttempts} attempts!")

                            self.__activePlayers[player] = False
                        else:
                            # Provides the corresponding feedback for that code.
                            feedback = Attempt().getAttempt(code.getCode(), decodingBoard.getPlayerCode(player.getName()))

                            self.__previousAttempts[player][code.getCode()] = feedback

                            print(f"Feedback: {feedback}")

                        # Decrements the number of remaining attempts a player has available.
                        self.__playerAttempts[player.getName()] = attemptsLeft - 1
                        if(attemptsLeft <= 0):
                            print(f"{player.getName()} failed to break the code.")

                            self.__activePlayers[player] = False

                        if(all(self.__activePlayers[status] == False for status in self.__activePlayers)):
                            print("The game is now finished.")
                            gameFinished = True

                        print()

        for player in playerList:
            if(self.__playerAttempts.get(player.getName()) > 0 and isinstance(player, HumanPlayer)):
                scoreIncrease = self.__playerAttempts.get(player.getName()) + 1
                player.incrementTotalScore(scoreIncrease)
                print(f"{player.getName()} recieves {self.__playerAttempts.get(player.getName())} + 1 points.")
        print()