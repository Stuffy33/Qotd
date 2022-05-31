import sys
import gspread
import random
from google.oauth2.service_account import Credentials
from termcolor import colored

# The scope was inspired by and borrowed from
# Code Instituet Love Sandwiches project
# https://github.com/Code-Institute-Solutions/love-sandwiches-p4-sourcecode

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Quotes_gs')
QUOTE_SHEET = SHEET.worksheet("Quotes")


def intro_quotes():
    """
    Introduction how to how use the app
    """
    print(colored(("Welcome Qotd,\n"),  "yellow"))
    print(colored(("Get inspired by a random quote."), "yellow"))
    print(colored(("or add your own quotes to our list.\n"), "yellow"))
    print(colored(("Click 1 then Enter to recive a random quote."), "magenta"))
    print(colored(("Click 2 then Enter to add your own quotes to our list."), "magenta"))
    print(colored(("Click 3 then Enter to end the program."), "magenta"))


def user_option():
    """
    function that choose if the user wants to:
        1) get a quote
        2) add a new quote
        3) Exit the program
    """
    choose = input("\nPlease, make your choice click (1, 2 or 3) then click Enter \n")
    if choose == "1":
        display_random_quote()
    elif choose == "2":
        add_quote()
    elif choose == "3":
        sys.exit(colored(("Exiting the program now, Thanks for using our service\n"), "yellow"))
    else:
        print(colored(("Try again, Choose either the number (1, 2 or 3)\n"), "red"))
    return user_option()


def display_random_quote():
    """
    Function that displays a random quote taken from our googlesheet list, if nr 1 has been clicked
    """
    quotes = QUOTE_SHEET.get_all_values()
    display_quote = random.choice(quotes)
    saythis = (f"{display_quote[0]}\n{display_quote[1]}")
    print(colored((saythis), "green"))


def add_quote():
    """
    Function will allow the user to add a quote of their own to our list aswell as the name of the author
    """
    input_quote = input(colored(("Please enter your quote: "), "magenta"))
    while len(input_quote) < 15:
        print(colored(("Sorry we only allow quotes longer than 15 characters, try to make a little longer <3\n"), "red"))
        input_quote = input(colored(("Please enter your quote: "), "magenta"))
    input_name = input(colored(("Please enter your name: "), "magenta"))
    while len(input_name) < 1:
        input_name = "Unknown"
        print(colored(('\nSince no name has been submitted have we given your quote the author of "unknown"'), "yellow"))
    update_list = [f'"{input_quote}"', f'- {input_name}']
    QUOTE_SHEET.append_row(update_list)
    print(colored(("\nThank you! \nYour quote have been added to our list"), "green"))


def main():
    """Start functions"""
    intro_quotes()
    user_option()
main()
