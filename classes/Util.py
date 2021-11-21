#
# File: Util.py
# Description: This file contains any utility/redundant functions that may be called more than once.
# Author: Vivienne Zhang
# Student ID: 110146861
# Email ID: zhavy001
# This is my own work as defined by the University's Academic Misconduct Policy.
#

def intInputErrorCheck(message, min, max):
    while True:
        try:
            print(message)
            userInput  = int(input())
            if(userInput < min or userInput > max):
                print("ERROR: Invalid input. Please try again.")
                
                continue
        except ValueError:
            print(f"ERROR: Invalid input type. Please enter an integer between {min} and {max}.")
            
            continue
        else:
            return userInput

def menuOptions():
    print("What would you like to do?")
    print("(r) register a new user")
    print("(s) show the score board")
    print("(p) play a game")
    print("(q) quit")