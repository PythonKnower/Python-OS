import sys
import os
import time as t
import random as rand

PYC_VERSION = "v0.0.2-Alpha-1"
PYOS_VERSION = "v0.09.0-Alpha-1"

facts = [
    "Did you know? Python was named after Monty Python.",
    "Fun fact: The first computer bug was an actual moth.",
    "Trivia: The first 1GB drive cost $40,000 in 1980.",
    "Interesting: Kazakh is written in Latin script since 2018 reforms.",
    "Cool: The first GUI OS was Xerox Alto in 1973."
]

diyk = [
    "DIYK: print('Hello World!')  # The classic first program",
    "DIYK: for i in range(5): print(i)  # Loop example",
    "DIYK: x = [1,2,3]; print(sum(x))  # Add numbers in list",
    "DIYK: def hi(): return 'Hello!'  # Simple function",
    "DIYK: name = input('Name: '); print(name)  # Input example"
]

class ansi:
    def clear():
        sys.stdout.write("\033[2J\033[H")
        sys.stdout.flush()

class sys:
    def clear():
        os.system("cls" if os.name == "nt" else "clear")

class command:
    def clear():
        sys.clear()
    
    def exit():
        sys.exit()
        sys.clear()
    
    def help():
        print("PyShell Help")
        print("============")
        print("clear - Clears the screen")
        print("exit - Exits the program")
        print("help - Displays this help message")
        print("version - Displays the version of PyShell")
        print("facts - Displays a random fact")
        print("diyk - Displays a random DIYK item")
    
    def version():
        print("PyShell Version: " + PYC_VERSION)
        print("PyOS Version: " + PYOS_VERSION)
    
    def facts():
        print(rand.choice(facts))

    def diyk():
        print(rand.choice(diyk))
