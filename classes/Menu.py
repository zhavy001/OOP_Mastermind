#
# File: Menu.py
# Description: This file contains the users various menu options.
# Author: Vivienne Zhang
# Student ID: 110146861
# Email ID: zhavy001
# This is my own work as defined by the University's Academic Misconduct Policy.
#

from classes.HumanPlayer import HumanPlayer
from classes.ComputerPlayer import ComputerPlayer
from classes.Game import Game

from classes.Util import *

class Menu:
    def __init__(self):
        self.__userDatabase = {}

    def showMenu(self):
        """
        Displays the various menu options for the user. Giving the following choices:

            1) Register a User.
            2) Display the Scoreboard.
            3) Play a round of WoM.
            4) Quit.
        """
        menuOptions();
        userInput = input()

        while(userInput not in ['r', 's', 'p', 'q']):
            menuOptions()
            print("Invalid choice. Please try again.")
            userInput = input()
        
        if(userInput == 'r'):
            self.registerUser()
        elif(userInput == 's'):
            self.showScoreboard()
        elif(userInput == 'p'):
            self.playGame()
        elif(userInput == 'q'):
            self.quitGame()
    
    def getUserInDatabase(self, username):
        """
        Returns a user in the database if they exist.

        Parameters:
            string username: The username of the user to retrieve.

        Returns:
            Player user: The Player object in the userDatabase.
        """
        if(username in self.__userDatabase):
            return self.__userDatabase.get(username)

    def registerUser(self):
        """
        Functionality to register a new user.
        """
        print("What is the name of the new user?")
        userInput  = input()
        
        while(userInput in self.__userDatabase or
              userInput == "HAL9000" or
              userInput == "VIKI"):
            print("Sorry, the name is already taken.")
            userInput = input()
        
        user = HumanPlayer(userInput)
        self.__userDatabase[userInput] = user
        
        print(f"Welcome {user.getName()}!\n")

    def showScoreboard(self):
        """
        Functionality to display the WoM scoreboard.
        """
        print("=====================================")
        print("Name\tScore\tGames\tAverage")
        print("=====================================")
        for i in self.__userDatabase:
            user = self.__userDatabase[i]
            totalScore = user.getTotalScore()
            gamesPlayed = user.getGamesPlayed()
            average = 0
            try:
                average = totalScore / gamesPlayed
            except ZeroDivisionError:
                average = 0

            print(f"{user.getName()}\t{totalScore}\t{gamesPlayed}\t{average}")
        print("=====================================")


    def playGame(self):
        """
        Functionality to begin a round of WoM.
        """
        playerList = []
        numPlayers = intInputErrorCheck("How many players (2-4)?", 2, 4)
        
        print("Let’s play the game of Mastermind!")

        for i in range(numPlayers):
            print(f"What is the name of player #{i + 1}")
            username = input()
        
            while(username in playerList or 
                  username not in self.__userDatabase or
                  username == "HAL9000" or
                  username == "VIKI"):
                print("Invalid user name.")
                print(f"What is the name of player #{i + 1}")
                username = input()
            
            playerList.append(self.getUserInDatabase(username))
        
        numAttempts = intInputErrorCheck("How many attempts will be allowed for each player (5-10)?", 5, 10)
        
        # Adding Computer Players to Game
        playerList.append(ComputerPlayer("HAL9000"))
        playerList.append(ComputerPlayer("VIKI"))

        # Incrementing numPlayers to accomodate for the Computer Players.
        numPlayers += 2

        game = Game()
        game.startGame(numAttempts, playerList)

    def quitGame(self):
        """
        Functionality to quit the game.
        """
        exit(1)