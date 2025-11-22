import os
import time as t
from datetime import datetime
import platform
import getpass
import sys
import importlib
import random

# first one
try:
    import requests
    requests_installed = True
except ImportError:
    requests_installed = False

start_time = t.time()
PYOS_VERSION = "v0.12.0-Beta"
PS_VERSION = "v0.19.0-Beta"
username = "PyShell"

print(
    f"Created in 2025, by ChatGPT and Max.\n"
    f"User: {username}\n"
    f"PythonShell version: {PS_VERSION}\n"
    f"Type 'help' to list all commands."
)

facts_list = [
    "Python was created by Guido van Rossum and released in 1991.",
    "The Zen of Python can be viewed with 'import this'.",
    "A list comprehension can replace a for-loop in many cases.",
    "f-strings are available from Python 3.6+.",
    "You can swap variables easily: a, b = b, a",
    "Use enumerate() to get index and value in a loop: for i, v in enumerate(lst):",
    "Use '_' in the interactive shell to get last result.",
    "Python uses indentation instead of braces for code blocks.",
    "Use sys.executable to get the current Python interpreter path.",
    "Type help() in Python to explore available functions and modules."
]

diyk_list = [
    "The first computer bug was a moth stuck in a relay!",
    "Python can be used to make games, apps, and even OS-level tools.",
    "You can swap two variables without a temporary variable: a, b = b, a",
    "Python supports multiple inheritance: class C(A, B): pass",
    "You can use '_' in the interactive shell to get the last evaluated result.",
    "List slicing can reverse a list: lst[::-1]",
    "The walrus operator (:=) lets you assign inside expressions: if (n := len(s)) > 5:",
    "You can chain comparisons: 1 < x < 10",
    "Generators are lazy iterators: use 'yield' instead of 'return'",
    "f-strings can include expressions: f'{2+3}' prints '5'",
    "32-bit integers have a problem with the year 2038!",
    "PyShell is actually a custom program by ChatGPT and Max!"
]

def weather_lookup():
    global requests_installed
    global requests
    if not requests_installed:
        choice = input(
            "Command 'weather' is disabled! Requests not installed.\n"
            "Type N to cancel, Y to download: "
        ).strip().lower()
        if choice == "y":
            os.system(f"{sys.executable} -m pip install requests")
            try:
                import requests
                importlib.reload(requests)
                requests_installed = True
                print("Requests installed successfully! You can use 'weather' now.")
            except ImportError:
                print("Failed to install requests.")
        else:
            print("Weather lookup cancelled.")
        return

    city = input("Enter city name for weather info: ").strip()
    try:
        api_url = f"http://wttr.in/{city}?format=3"
        response = requests.get(api_url)
        if response.status_code == 200:
            print(f"Weather Info: {response.text}")
        else:
            print("Failed to fetch weather info.")
    except Exception as e:
        print(f"Error fetching weather: {e}")

def ip_lookup():
    global requests
    if not requests_installed:
        print("Command 'ip' is disabled! Requests not installed.")
        return
    try:
        response = requests.get("https://api.ipify.org")
        if response.status_code == 200:
            print(f"Your external IP: {response.text}")
        else:
            print("Failed to fetch IP.")
    except Exception as e:
        print(f"Error fetching IP: {e}")

def fact_command():
    fact = random.choice(facts_list)
    print(f"Fact / Snippet: {fact}")

def diyk_command():
    item = random.choice(diyk_list)
    print(f"Did You Know? {item}")

while True:
    cmd = input("PyShell> ").strip().lower()

    if cmd in ["list"]:
        files = os.listdir()
        if files:
            for f in files:
                print(f)
        else:
            print("No files found.")
    elif cmd in ["clear", "cls"]:
        os.system("cls" if os.name == "nt" else "clear")
    elif cmd == "time":
        now = datetime.now()
        local_time = now.strftime("%H:%M:%S")
        timezone = now.astimezone().tzname()
        elapsed = int(t.time() - start_time)
        print(
            f"Local time: {local_time} | Timezone: {timezone} | "
            f"Seconds since terminal opened: {elapsed}"
        )
    elif cmd in ["dir", "directory"]:
        print(f"Current directory: {os.getcwd()}")
    elif cmd == "user":
        home = os.path.expanduser("~")
        print(f"Username: {username} | Home directory: {home}")
    elif cmd == "pyver":
        print(f"PythonShell version: {PS_VERSION}")
    elif cmd == "osver":
        print(f"OS version: {PYOS_VERSION}")
    elif cmd == "help":
        print(
            "Commands:\n"
            "list - List files\n"
            "clear / cls - Clear terminal\n"
            "time - Show local time & elapsed\n"
            "dir / directory - Current directory\n"
            "user - User info\n"
            "pyver - PythonShell version\n"
            "osver - OS version\n"
            "help - Help menu\n"
            "exit - Exit\n"
            "weather - Weather lookup\n"
            "ip - Show external IP\n"
            "fact - Random fact or code snippet\n"
            "diyk - Did You Know? fun fact or snippet"
        )
    elif cmd == "exit":
        print("Shutting down PythonShell...\n")
        break
    elif cmd == "weather":
        weather_lookup()
    elif cmd == "ip":
        ip_lookup()
    elif cmd == "fact":
        fact_command()
    elif cmd == "diyk":
        diyk_command()
    else:
        print("Invalid Command! Please type 'help' to list all commands.")
