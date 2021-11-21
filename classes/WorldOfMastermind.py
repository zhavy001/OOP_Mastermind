#
# File: WorldOfMastermind.py
# Description: This file contains all core functionality of the game.
# Author: Vivienne Zhang
# Student ID: 110146861
# Email ID: zhavy001
# This is my own work as defined by the University's Academic Misconduct Policy.
#

from classes.Menu import Menu

class WorldOfMastermind():
    def __init__(self):
        self.__menu = Menu()

    def run(self):
        """
        This function will call the game menu, where all other functionality will run from.
        """
        print("Welcome to the World of Mastermind!")
        print("Developed by Vivienne Zhang")
        print("COMP 1046 Object-Oriented Programming\n")

        while True:
            self.__menu.showMenu()