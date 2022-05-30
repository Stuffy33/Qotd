set up an account in google cloud platform
https://console.cloud.google.com/

got to APIs and services -> library and get google drive API with json key
then get google sheets

Move the downloaded json key file into the gitpod files
rename it cred.json

set cred.json in .gitignore so it won't get pushed into github

install dependencies google-auth
https://google-auth.readthedocs.io/en/master/
by typing: "pip3 install gspread google-auth" in the terminal

Go to run.py ( where all the python will be coded)
import gspread from google.oauth2.service_account import Credentials

import gspread = import the entire gspread library ( so we can access any function, class or method)

import Credentials = imports the credentials class which is part of the service_account  function from the Google auth library. As we only need this class for our project, there is no need to import the entire library here.

add scope: (this specifies what the user have access to)


Credits
https://pypi.org/project/termcolor/


had a bug with typing the the googlesheet name instead of the page name.
solved it by watching a tutorial where i saw my mistake.
https://www.youtube.com/watch?v=bu5wXjz2KvU

#    quote_list = QUOTE_SHEET.row_values(random.randrange(len(quotes[0])))
