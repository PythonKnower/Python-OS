from colorama import Fore, Style, init
import sys
import os
import time as t
import random as rand

init()

PYC_VERSION = "v0.0.1-Alpha-7"
PYOS_VERSION = "v0.09.0-Alpha"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def show_help():
    print("""
PyShell Commands:
  help      - Show this help
  version   - Show PyOS version
  clear     - Clear screen
  exit      - Exit PyShell
""")

def prompt():
    return f"{Fore.CYAN}PyOS{Fore.LIGHTCYAN_EX}> {Style.RESET_ALL}"

def shell():
    print("Welcome to PyShell")
    print("Type 'help' for commands.")

    while True:
        try:
            command = input(prompt())

            if command == "help":
                show_help()

            elif command == "version":
                print(f"PyOS {PYOS_VERSION}")
                print(f"PYC {PYC_VERSION}")

            elif command == "clear":
                clear()

            elif command == "exit":
                print("Goodbye!")
                break

            elif command.strip() == "":
                pass

            else:
                print(f"Unknown command: {command}")

        except KeyboardInterrupt:
            print("\nUse 'exit' to quit.")

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    shell()