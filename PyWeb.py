import requests
from bs4 import BeautifulSoup
import webbrowser


VERSION = "PyBrowser v0.2"
PYOS_VERSION = "v0.10.0-dev"


def search_web(query):
    print(f"\nSearching for: {query}...\n")

    url = "https://html.duckduckgo.com/html/"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    data = {
        "q": query
    }

    response = requests.post(
        url,
        data=data,
        headers=headers
    )

    soup = BeautifulSoup(response.text, "html.parser")

    results = []

    for result in soup.select(".result")[:5]:
        title = result.select_one(".result__title")
        link = result.select_one(".result__a")

        if title and link:
            results.append(
                (
                    title.text.strip(),
                    link["href"]
                )
            )

    if not results:
        print("No results found.")
        return

    for i, (title, link) in enumerate(results, 1):
        print(f"""
[{i}] {title}
{link}
""")

    choice = input("Open result number (or enter to cancel): ")

    if choice.isdigit():
        num = int(choice)

        if 1 <= num <= len(results):
            selected = results[num-1][1]

            print("Opening:", selected)

            webbrowser.open(selected)


def browser():

    print(VERSION)
    print(PYOS_VERSION)
    print("""
Commands:
 search <text>  Search the web
 exit           Quit
""")

    while True:
        cmd = input("\nPyBrowser > ")

        if cmd == "exit":
            break

        elif cmd.startswith("search "):
            query = cmd[7:]
            search_web(query)

        else:
            print("Unknown command")


if __name__ == "__main__":
    browser()