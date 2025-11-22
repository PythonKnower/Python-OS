import os
import time as t
from datetime import datetime
import platform
import getpass
import random

start_time = t.time()

PYOS_VERSION = "v0.04.0-Beta-1"
PS_VERSION = "v0.17.0-Beta-8"
username = "PyShell"

# first set of facts/snippets only
facts = [
    "Did you know? Python was named after Monty Python.",
    "Fun fact: The first computer bug was an actual moth.",
    "Trivia: The first 1GB drive cost $40,000 in 1980.",
    "Interesting: Kazakh is written in Latin script since 2018 reforms.",
    "Cool: The first GUI OS was Xerox Alto in 1973."
]

diyk_items = [
    "DIYK: print('Hello World!')  # The classic first program",
    "DIYK: for i in range(5): print(i)  # Loop example",
    "DIYK: x = [1,2,3]; print(sum(x))  # Add numbers in list",
    "DIYK: def hi(): return 'Hello!'  # Simple function",
    "DIYK: name = input('Name: '); print(name)  # Input example"
]

print(f"Created in 2025, by ChatGPT and Max.\nUser: {username}\nPythonShell version: {PS_VERSION}\nType 'H' or 'h' to list all commands.")

while True:
    cmd = input("PyShell> ").strip().lower()

    if cmd == "list":
        files = os.listdir()
        if files:
            for f in files:
                print(f)
        else:
            print("No files found.")

    elif cmd == "clear" or cmd == "cls":
        os.system("cls" if os.name == "nt" else "clear")

    elif cmd == "time":
        now = datetime.now().strftime("%H:%M:%S")
        elapsed = int(t.time() - start_time)
        print(f"Current time: {now} | Seconds since terminal opened: {elapsed}")

    elif cmd == "uptime":
        elapsed = int(t.time() - start_time)
        hours = elapsed // 3600
        minutes = (elapsed % 3600) // 60
        seconds = elapsed % 60
        print(f"Uptime: {hours}h {minutes}m {seconds}s")

    elif cmd == "dir":
        print(f"Current directory: {os.getcwd()}")

    elif cmd == "sys":
        print(f"Platform: {platform.system()} {platform.release()}")
        print(f"Python version: {platform.python_version()}")

    elif cmd == "user":
        home = os.path.expanduser("~")
        print(f"Username: {username} | Home directory: {home}")

    elif cmd == "pyver":
        print(f"PythonShell version: {PS_VERSION}")

    elif cmd == "osver":
        print(f"OS version: {PYOS_VERSION}")

    elif cmd == "fact":
        print(random.choice(facts))

    elif cmd == "diyk":
        print(random.choice(diyk_items))

    elif cmd == "coinflip":
        result = random.choice(["Heads", "Tails"])
        print(f"Coin Flip Result: {result}")

    elif cmd == "h":
        print("Commands:\n"
              "list - List files\n"
              "clear/cls - Clear terminal\n"
              "time - Show time and seconds since opened\n"
              "uptime - Full runtime display\n"
              "dir - Current directory\n"
              "sys - System info\n"
              "user - User info\n"
              "pyver - PythonShell version\n"
              "osver - OS version\n"
              "fact - Random fact\n"
              "diyk - Extra facts/snippets\n"
              "coinflip - Flip a digital coin\n"
              "exit - Exit PyShell")

    elif cmd == "exit":
        print("Shutting down PythonShell...\n")
        break

    else:
        print("Invalid Command! Please type 'H' or 'h' to list all commands.")
