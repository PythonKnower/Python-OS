from colorama import Fore, Style, init
import sys
import os

init()

PYC_VERSION = "v0.0.1-Alpha-7"
PYOS_VERSION = "v0.10.0-dev"


# -------------------------
# Settings
# -------------------------

settings = {
    "theme": {
        "name": "Cyan",
        "primary": "LIGHTCYAN_EX",
        "secondary": "CYAN"
    },
    "user": {
        "name": "Guest"
    }
}


def get_color(color):
    return getattr(Fore, color, Fore.WHITE)


# -------------------------
# System
# -------------------------

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def show_help():
    print("""
PyShell Commands:

 help       - Show this help
 version    - Show PyOS version
 print      - Print text
 settings   - Open settings
 clear      - Clear screen
 exit       - Exit PyShell

""")


def show_settings():

    print("""
--- PyOS Settings ---

Username:
 {username}

Theme:
 {theme}

Primary:
 {primary}

Secondary:
 {secondary}

""".format(
        username=settings["user"]["name"],
        theme=settings["theme"]["name"],
        primary=settings["theme"]["primary"],
        secondary=settings["theme"]["secondary"]
    ))


# -------------------------
# Settings Menu
# -------------------------

def settings_menu():

    while True:

        print("""
--- Settings ---

1. Change theme
2. Change username
3. View settings
4. Exit

""")

        choice = input("Settings> ")


        if choice == "1":

            print("""
Themes:

1. Cyan
2. Green
3. Red
4. Blue
5. Yellow
6. White

""")

            theme_choice = input("Theme> ").lower()


            themes = {

                "cyan": {
                    "name": "Cyan",
                    "primary": "LIGHTCYAN_EX",
                    "secondary": "CYAN"
                },

                "green": {
                    "name": "Green",
                    "primary": "LIGHTGREEN_EX",
                    "secondary": "GREEN"
                },

                "red": {
                    "name": "Red",
                    "primary": "LIGHTRED_EX",
                    "secondary": "RED"
                },

                "blue": {
                    "name": "Blue",
                    "primary": "LIGHTBLUE_EX",
                    "secondary": "BLUE"
                },

                "yellow": {
                    "name": "Yellow",
                    "primary": "LIGHTYELLOW_EX",
                    "secondary": "YELLOW"
                },

                "white": {
                    "name": "White",
                    "primary": "LIGHTWHITE_EX",
                    "secondary": "WHITE"
                }
            }


            if theme_choice in themes:

                settings["theme"] = themes[theme_choice]

                print("Theme changed!")

            else:

                print("Unknown theme.")



        elif choice == "2":

            name = input("New username> ")

            settings["user"]["name"] = name

            print("Username changed!")



        elif choice == "3":

            show_settings()



        elif choice == "4":

            break



        else:

            print("Invalid option.")



# -------------------------
# Shell
# -------------------------

def prompt():

    primary = get_color(
        settings["theme"]["primary"]
    )

    secondary = get_color(
        settings["theme"]["secondary"]
    )

    username = settings["user"]["name"]

    return f"{primary}{username}@PyOS{secondary}> {Style.RESET_ALL}"



def shell():

    print("Welcome to PyShell")
    print("Type 'help' for commands.")


    while True:

        try:

            command = input(prompt()).strip()


            if command == "":
                continue


            parts = command.split(maxsplit=1)

            cmd = parts[0].lower()

            argument = ""

            if len(parts) > 1:
                argument = parts[1]



            if cmd == "help":

                show_help()



            elif cmd == "version":

                print(f"PyOS {PYOS_VERSION}")
                print(f"PYC {PYC_VERSION}")



            elif cmd == "print":

                if argument.startswith('"') and argument.endswith('"'):

                    argument = argument[1:-1]

                print(argument)



            elif cmd == "settings":

                settings_menu()



            elif cmd == "clear":

                clear()



            elif cmd == "exit":

                print("Goodbye!")
                break



            else:

                print(f"Unknown command: {cmd}")



        except KeyboardInterrupt:

            print("\nUse 'exit' to quit.")


        except Exception as e:

            print("Error:", e)



if __name__ == "__main__":
    shell()