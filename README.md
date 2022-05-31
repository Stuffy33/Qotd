# Qotd - Quote of the day

# The purpose with this project

Qotd is a console based application that gives the user a chance to get motivated by reading thought worthy quotes. The user interface is text based and it is run from a text terminal or other types of command-in interfaces. 

The application has two options either read a quote taken from our lists of quotes or add their own quote to our lists.

Target audience: Individuals that needs more food for thought during the day.

Required technologies for this project: Python

A live version of this project can be found at this url: https://git.heroku.com/qotd12.git

# Table of Content

+ [UX](#ux "UX")
  + [User Demographic](#user-demographic "User Demographic")
  + [User Stories](#user-stories "User Stories")
    + [User submitting](#user-submitting "User submitting")
  + [User Goals](#user-goals "User goals")
  + [Project Requirements](#project-requirements "Project Requirements")
  + [Design diagram](#design-diagram "Design diagram")
+ [Features](#features "Features")
  + [Existing Features](#existing-features "Existing Features")
    + [Start Read and submit](#start-read-and-submit "Start read and submit")
  + [Features Left to Implement](#features-left-to-implement "Features Left to Implement")
+ [Technologies used](#technologies-used "Technologies used")
  + [Data storage](#data-storage "Data Storage")
+ [Testing](#testing "Testing")
  + [Bugs during development](#bugs-during-development "Bugs during development")
  + [Validator Testing](#validator-testing "Validator Testing")
  + [Unfixed Bugs](#unfixed-bugs "Unfixed Bugs")
+ [Development and Deployment](#development-and-deployment "Development and Deployment")
+ [Content](#content "Content")
+ [Credits](#credits "Credits")

## UX

### User Demographic

This application is ment for:

 - Individuals that wants to read intressting quotes that makes the gear in their head turn.
 - Individuals who wants to share their own quotes.

### User Stories

I have divided the user stories for this application in to two different sections, User Reading and User Submitting.

#### User submitting

 - I want to submit a intressting quote.
 - I want other users to read my quotes.

### User Goals

To get food for thought on daily bases either by reading or submiting quotes.

### Project Requirements

Python application using libraries/API and deployed to a cloud-based platform.

### Design diagram

Qotd is a console based application. For that reason no work was put in to graphical design. Instead focus was put on creating a diagram of the entire application and use that as the base for the code. The diagram also include the Google Sheet used for data storage.


This is the initial diagram:

![Intial diagram](/README_images/Wire%20frame%20python.JPG)

[Back to top](#Qotd)

## Features 

Qotd consists of two features. The user chooses the option of feature from the start section of the application. The features are:

 - Read quote
 - Submit a quote

### Existing Features

#### Start read and rate

The user starts the read and submit option from the start section of the application. To read a quote click the number 1 then click enter.

![Start page with options](/README_images/start%20page.JPG)

After the number 1 has been clicked you recive a quote then the option of reading a new quote, submit your own or quit the program will be presented

![Give quote click 1](/README_images/click%201.JPG)

After the number 2 has been clicked you get told to enter a quote and the autor of the quote. If the quote is shorter than 15 symbols you will recive an error message. no name has been added the name section in the spread sheet will be filled in automaticly with the name "Unknown"

![quote added successfully](/README_images/successfull%20quote%20added.JPG)

If any requirement is not meet the user will recive a information text what has happend and what should be done next.
![Error message](/README_images/error%20messages.JPG)

Different information has been color coded:
Purple: ask you to do a certain task.
Yellow: gives information
Red: Error has occured
Green: the program has done what you wanted / positive reinforcement

![The entire program](/README_images/The%20entire%20program.JPG)

## Features Left to Implement

Future versions of this application will contain a graphical user interface and an option to rate quotes.

[Back to top](#Qotd)

## Technologies and libraries used

Main languages

- [Python](https://en.wikipedia.org/wiki/Python_programming_language)
- [HTML](https://en.wikipedia.org/wiki/HTML) - Provided in the Code Institute template
- [CSS](https://en.wikipedia.org/wiki/CSS) - Provided in the Code Institute template
- [JavaScript](https://en.wikipedia.org/wiki/javascript) - Provided in the Code Institute template

Python libraries and api used

- [Sys](https://docs.python.org/3/library/sys.html)
- [Random](https://docs.python.org/3/library/random.html)
- [Google auth](https://google-auth.readthedocs.io/en/master/index.html)
- [Termcolor](https://pypi.org/project/termcolor/)
- [Gspread](https://docs.gspread.org/en/latest/)

### Data storage

Quotes, submitted quotes, sumbmitted authors are fetched and stored in a Google Sheet using:

- [Google Drive API](https://developers.google.com/drive/api)
- [Google Sheet API](https://developers.google.com/sheets/api)


## Testing 

Testing has been conducted by the author and my mentor [Martina Terlevic](https://www.linkedin.com/in/martinaterlevic/) 

### Bugs during development

- I couldn't strictly use colored on my fquote therefor did i make it into a variable and colored the variable instead called "saythis"

- Had a bug with typing the the googlesheet name instead of the page name.
solved it by watching a tutorial where i saw my mistake.
https://www.youtube.com/watch?v=bu5wXjz2KvU

- i had issues with connecting the quote with the author first i used this code:
    quote_list = QUOTE_SHEET.row_values(random.randrange(len(quotes[0])))
The issue with this is that i wasen't able to pair the two rows.
Therefor with a hint from my friend "angry olive"
To use get_all_values and some googeling on stackoverflow did i find this solution:
    quotes = QUOTE_SHEET.get_all_values()
    display_quote = random.choice(quotes)
    saythis = (f"{display_quote[0]}\n{display_quote[1]}")
    print(colored((saythis), "green"))

https://stackoverflow.com/questions/31303581/get-all-values-from-google-spreadsheet

### Validator Testing 

The code has also been tested by using PEP8 Online http://pep8online.com/.

Final testing warned about long lines. I am aware of this but it has not been corrected since i deemed that the lines look more readable in its current state.

![PEP8](/README_images/PEP8.JPG)

### Unfixed Bugs

- No known bugs at this point

 [Back to top](#Qotd)

## Development and Deployment

The development environment used for this project was GitPod. To track the development stage and handle version control regular commits and pushes to GitHub has been conducted. The GitPod environment was created using a template provided by Code Institute.

The live version of the project is deployed using Heroku(https://heroku.com)

This is how this project was deployed using Heroku:

To prepare for deployment on Heroku a requirements.txt needs to be created in the same folder as the .py file in GitPod. This file needs to contain a list of all libraries the project needs to run as a Heroku App.

Then follow these steps:

 - Login to Heroku (Create an account if necessary)
 - Click on New in the Heroku dashboard and select ”Create new app”
 - Write a name for the app and choose your region and click ”Create App”
 - In the settings tab for the new application I created two Config vars.
   - One is named CREDS and contains the credentials key for Google Drive API
   - One is name PORT and has the value of 8000
 - Two buildpack scripts were added: Python and Nodejs (in that order)

Heroku CLI was used to deploy the project. The following steps were taken in the terminal in GitPod

Deploying your app to heroku
1. Login to heroku and enter your details.
 - command: heroku login -i
2. Get your app name from heroku.
 - command: heroku apps
3. Set the heroku remote. (Replace <i>app_name</i> with your actual app name)
 - command: heroku git:remote -a <i>app_name</i>
4. Add, commit and push to github
 - command: git add . && git commit -m "Deploy to Heroku via CLI"
5. Push to both github and heroku
 - command: git push origin main
 - command: git push heroku main

After those steps were taken the application was deployed at the following link: https://git.heroku.com/qotd12.git

## Content 

- All text content in the application is created by the author of the project.
- The initial quotes in the Google Sheet are credited to [OnlineDailys](https://medium.com/@irfanmoeen704/motivational-quotes-top-100-quotes-about-life-work-success-student-and-inspiration-c1d88aa0220a) 

## Credits 

### For code inspiration, design inputs, help and advice.

 - [Google Sheets for Developers](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/cells) for information about exctracting information from a Google Sheet.
 - [Code Institute - Love Sandwiches](https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode) for inspiration and understanding on how to develope the project.
 - [Code Institute](https://codeinstitute.net/) for all course material leading up to this project.
 - [stack overflow](https://stackoverflow.com/questions/31303581/get-all-values-from-google-spreadsheet) Get all values

### Acknowledgment

 - [Martina Terlevic](https://www.linkedin.com/in/martinaterlevic/) My mentor at Code Institute.

 - [Angry olive] (My friend)

 -[Pelikantapeten] student at code institute, Borrowed his readme as a template.

[Back to top](#Qotd)