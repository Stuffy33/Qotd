import gspread
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









def main():
    """Start functions"""
    intro_quotes()

main()