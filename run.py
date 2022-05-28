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

def update_worksheet(value, worksheet):
    """Function that updates the worksheet."""
    
    """
    Credits Code Institutes Walkthru project - Love Sandwiches
    https://github.com/Code-Institute-Solutions/love-sandwiches-p4-sourcecode
    """
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(value)

def intro_quotes():
    """Introduction how to how use the app"""
    print(colored(("Hello, Welcome to quote of the day!\n"),  "magenta"))
    print(colored(("Get inspired by a random quote."), "magenta"))
    print(colored(("Also add your own quotes to our list.\n"), "magenta"))
    print(colored(("Enter 1 to recive a random quote."), "magenta"))
    print(colored(("Enter 2 to add one of your own favorite quotes to our list.\n"), "magenta"))


def user_option():
    """function that choose if the user wants to get a quote or add a new quote"""
    choose = input("\nPlease, make your choice press (1 or 2)\n")
    if choose == "1":
        display_random_quote()
    elif choose == "2":
        add_quote()
    else:
        print(colored(("Try again, Choose either the number (1 or 2)\n"), "red"))
    return user_option()

def display_random_quote():
    """Function that displays a random quote from the googlesheet, if nr 1 has been clicked"""
    quote_list = SHEET.worksheet("Quotes").col_values(1)
    display_quote = random.choice(quote_list)
    print(colored((display_quote), "cyan"))








def main():
    """Start functions"""
    intro_quotes()
    user_option()
main()