#!/usr/bin/python3
from pyfiglet import Figlet
from rich import print as rprint
from rich.prompt import Confirm
from rich.prompt import Prompt
from tabulate import tabulate
import sys
import time

# ./modules/*
from modules.instagram import Instagram
from modules.snapchat import Snapchat
from modules.spotify import Spotify

def main():
    f = Figlet(font='slant')
    print(f.renderText('mailogleit'))

    while True:
        email = Prompt.ask("[blue][>][/blue] [white]Enter an e-mail address to scan[/white]")
        email_confirm = Prompt.ask(f"[green]{email}[/green] is that correct? [pink](y/n)[/pink]", default="y")

        if email_confirm.lower() in ["y", "yes"]:
            break
        else:
            rprint("[red]Error:[/red] [white]Please enter the e-mail again.[/white]")

    rprint("[bold green]Scanning the e-mail...[/bold green]")

    animation = "|/-\\"
    start_time = time.time()
    while True:
        for i in range(4):
            time.sleep(0.2)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()
        if time.time() - start_time > 3: # in seconds
            break
    sys.stdout.write("\r")

    print(tabulate([[email]], headers=["E-mail"], tablefmt="grid"))

    Instagram.run_scan(email)
    Snapchat.run_scan(email)
    Spotify.run_scan(email)

if __name__ == "__main__":
    main()