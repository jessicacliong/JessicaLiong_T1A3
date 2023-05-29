# Snooze It

##[GitHub Respository](https://github.com/jessicacliong/JessicaLiong_T1A3)

##[Source Control of Respository](https://github.com/jessicacliong/JessicaLiong_T1A3/commits/main)

##[Project Management Platform](https://trello.com/b/QnfB52xz/snooze-it-application)

##[Video Presentation](https://youtu.be/JwYR-spJ03Q)


## Purpose & Scope
Snooze It is an application that allows users to store a range of sleep information. This will save a user's sleep related information such as sleep hours, quality of sleep in accordance with other factors contributing to quality of sleep. The application will also allow users to view a summary of their sleep information over periods of one day and up to a week maximum.

The purpose of this project is to demonstrate my current skills and ability in a range of developer tools encompassing the python programming language. 
This project will also stretch my ability to design, implement and test an application through the creation of a terminal (command line) application. 

## Target Audience
The application is targeted for users of any age and gender who is able to run the application using the help documentation below on their computer terminal and log in inputs are welcome to utilise the application. 

## Features

### 1. Log Daily Sleep Times & Factors Affecting Sleep
Users are able to log in sleep time every day and keep track of the quality of their sleep, whether they had a goodnight's sleep or they didn't, rating it from 0 (No sleep) - 10 (Excellent).
The application allows users to write down comments and factors during the day or during the night before they slept that could impact the user's sleep.

### 2. Sleep Report (1 Day)
Gives user a report of their sleep time, quality, and other associated sleep information including a journal of a set date. Users input a desired date and the information of their sleep conditions will be displayed on their terminal. 

### 3. Sleep Report (Up to 7 consecutive days)
Gives users a report of their sleep time, quality and other relevant sleep information over a period of 1 week period before current date. The 1 week period can be specified through user inputs of the desired start date and end date. Available sleep logs saved in the system will be displayed to the user as a terminal output.
Note: The 1 week period specified will include the start date and the end date defined by the user, if a log for those dates exist in record.

### 4. Suggest Tips on better Sleep
Upon the completion of a day's sleep information entry, user's will be given a sleep tip on their terminal window to help them gain ample quantity and quality sleep for a more productive day.

## Implementation Plan

To implement the development steps of my application, I utilised Trello to keep note of all of my progress, the different features of my application and the to-do list for every feature to be completed. I listed every task that was required to do for each feature, categorised them accordingly and gave each task a deadline date to complete the task by.  

Every time a task is completed, the date deadline box can be clicked to give a green box with a tick, which marks the task as completed on trello. 

The link to my Trello can be found [here](https://trello.com/b/QnfB52xz/snooze-it-application)

## Psuedocodes

As a part of my implementation plan, I have written pseudocodes to outline the methods and functions that will be used to accomplish the features of my application utilising python code.

__Feature 1 - Request User inputs on a range of sleep information (High Priority)__

1. Import CSV Module
2. UserInformation CSV Created Prior to SleepInformationInput
3. Prompt User With SleepLogDate
4. Prompt User With SleepHours
5. Prompt User With SleepQuality
6. Prompt User With CaffeineIntake
7. Prompt User With SleepJournalEntryChoice
8. If Input == "Y", Prompt JournalEntryWindow, If Input == "N", Continue From Step11
9. Select <Enter> UponCompletion
10. Write InputasRow With DictWriter into CSVFile
11. Print ClosingGreeting
12. EndProgram

__Log Search Main Menu__

1. PromptLogSearch Request to User 
2. Prompt SearchOptions as: 
	a. 1DaySearch 
	b. 1WeekSearch
	c. EndApplication
3. Prompt Instructions To NavigateAroundMenu
4. If UserSelection = a, Run Feature2
5. If UserSelection = b, Run Feature3
6. If UserSelection = c, TermimateApplication

__Feature 2 - Display Previous Sleep Log (High Priority)__

1. Import PandasModule
2. Create ReadCSV object of User_Information using DataFrame Feature of Pandas Module. 
3. PromptUser To Enter InputDate (DD-MM-YYYY)
4. Convert InputDateFormat to pandas DateTime Format
5. Filter InputDate Using Pandas DataFrame For InputDate == ExistingUserInformation
6. If MatchFound, Print Output Onto UserTerminal
7. If NotMatchFound, Print NoInputError & Print EmptyLog
8. Return to MainMenuLogSearchOptions

__Feature 3 - Display Previous 7 Days Sleep Logs from Current Day (High Priority)__

1. Create ReadCSV object of User_Information using DataFrame Feature of Pandas Module. 
2. PromptUser To Enter StartDate (DD-MM-YYYY).
3. LimitSearchDate to 7ConsecutiveDates BeforeCurrentDate. 
	 End_date = dt.datetime.now() - time.delta(day=7)
4. PrintToUser(The StartDateSearch is {StartDate} and EndDateSearch is {EndDate}.)
5. Filter LogDates <= StartDate & LogDates >= EndDate using DataFrames.Mask Functionality In ExistingUserInformation.Csv
6. Locate / Read Rows With PandasDataFrame
7. Print Output of SleepLogs Onto UserTerminal 
8. Return to MainMenuLogSearchOptions

__Feature 4 - Display A Sleep Tip (High Priority)__

1. Create ListOfSleepTips on CsvFile
2. ReadFunction CSVModule To Read SleepingTip From Sleep_Tips.Csv File (SkippingFileHeader)
3. Randomise Row
4. After SleepInformationInput Made, Print Random SleepingTip onto UserTerminal 

## Help Instructions (For MacOS only)

To run this application, users can use any operating system they wish as long as it supports a Terminal or Command Line Interface.
If you are a Windows user, we recommend utilising the Ubuntu terminal by installing the Windows Subsystem for Linux (WSL).

The instructions below are just for Mac operating systems only.  

### Step 1: Open the system terminal

### Step 2: Check the version of Python installed in your computer and (as necessary) download/update Python.

On Mac, the recommended way to install python is to utilise the official Python.org installer. Instructions can be found [here](https://www.jcchouinard.com/install-python-on-macos/#:~:text=Install%20Python%20with%20Package%20Installer,-The%20best%20place&text=Go%20to%20Python.org%20and,through%20each%20of%20the%20prompts.).

__Step 3: Locate a folder where you would like to save the terminal application.__

__Step 4: Once inside the folder, clone the repository from Github using the following command:__

```
git clone https://github.com/jessicacliong/JessicaLiong_T1A3.git
```

This will clone the repository of the application from the following window on github:

![Github Repository](/docs/github_respository.png)

__Step 5: Navigate to the folder that contains the repository using the terminal window__

__Step 6: Once within the folder, type the following command and press enter:__

```
./run_application.sh
```

This will automatically run the bash script contained in the folder and automates the following actions:

- Ensure you have python version 3 installed on your system and prompts a warning message if not available
- Create a virtual environment using the standard name .venv.
- Activate the created virtual environment
- Install all dependencies of the application stored within a requirements.txt file for the user
- Run the python file
- Deactivation of the virtual environment upon completion of running the application.

__Note:__

If running Step 6 does not work, type the following command and retry Step 6 again.

```
chmod +x run_application.sh
```

## System Requirements

Snooze It is designed to run on Windows, Mac OS X and Linux.

__Minimum Specifications__

Snooze It is an application without any images, music, sound effects, or a GUI, so any modern computer made within the past 10 years should be able to execute this application. 

Snooze It has been developed and tested regularly on the following system:

2021 Retina 16-inch Macbook Pro, Apple M1 Pro Chip, 16GB Unified Memory, 512GB SSD

## Dependencies

numpy==1.24.3

pandas==2.0.1

python-dateutil==2.8.2

pytz==2023.3

simple-term-menu==1.6.1

six==1.16.0

tzdata==2023.3


## References

__Python Coding__

Automate the Boring Stuff with Python (n.d.). Chapter 16: Working with CSV Files. Retrieved from https://automatetheboringstuff.com/2e/chapter16/

Stack Overflow (n.d.). Inserting Input into CSV. Retrieved from https://stackoverflow.com/questions/55980027/building-a-csv-based-on-user-input

Harvard University, CS50 (2022). File Handling Lecture. Retrieved from https://cs50.harvard.edu/python/2022/notes/6/

Python Software Foundation (n.d.). PEP 8 -- Style Guide for Python Code. Retrieved from https://peps.python.org/pep-0008/

Stack Overflow (n.d.). Python Date String Testing. Retrieved from https://stackoverflow.com/questions/18610884/python-date-string-testing

Stack Overflow (n.d.). Writing & Reading CSV file Python. Retrieved from https://stackoverflow.com/questions/14978575/writing-reading-the-same-csv-file-in-python

Stack Overflow (n.d.). Printing data using DataFrames in Pandas. Retrieved from https://stackoverflow.com/questions/64817406/fetching-particular-rows-of-a-csv-file-where-date-matches-as-entered-by-user

Dataquest (2023). DateTime in Pandas: An Uncomplicated Guide. Retrieved from https://www.dataquest.io/blog/datetime-in-pandas/#:~:text=Now%2C%20the%20data%20type%20of,precision%20of%20the%20DateTime%20object.

Stack Overflow (n.d.). Searching Records between 2 dates in CSV File. Retrieved from https://stackoverflow.com/questions/62058695/searching-for-records-between-two-dates-and-two-times-in-csv-file-using-python-p


__Testing__

Python Software Foundation. (n.d.). Exceptions - Python 3.9.7 documentation. Retrieved from https://docs.python.org/3/library/exceptions.html#Exception

Python Software Foundation. (n.d.). CSV - Python 3.9.7 documentation. Retrieved from https://docs.python.org/3/library/csv.html#reader-objects


__Help Documentation__

cloudbytes.dev. (n.d.). Upgrade Python to Latest Version on Ubuntu/Linux. Retrieved from https://cloudbytes.dev/snippets/upgrade-python-to-latest-version-on-ubuntu-linux



## Further Development of Application

__Further Improvements of Feature 1__

Users are able to make duplicate entries of the same date within the csv file and the search 
ability will be able to identify these duplicates upon a week search prompt. Due to the time constraints and skill constraints of the project, this problem has not been solved and overcome. 
The best solution to overcome duplication is to check using the single date search if an entry of a certain date has been made in the system first and from there decide to write an entry for that date or not.

Another alternative solution to this is to further enhance the application by limiting the sleep log entry to just the day's date otherwise they miss out on the chance to submit a sleep log.

Would also like to implement a delete feature if possible for this system to enable users to append entries in the case mistakes are detected in any logs. 

__Extra Features__

If time permitted, the application could have a login feature where each user could have individual access to their own sleep information in separate accounts, allowing for separation of sleep logs to tailor an individual's search function and enhance privacy of an individual's sleep journals and logs. 

Pseudocode for Feature 5 - User Login Feature

 Login Feature (If Time Permiting)__  

Log In Menu, Prompts 2 Options:
	a. Create NewUser
	b. Login As Existing User

a. Creating NewUser

i. Creating NewUsername
    - UserInput To CreateNewUsername
    - CrossCheck Database 
      	If Exists, Enter DifferentUsername
      Loop Until inputisUnique
 When successful, Saveto Database

ii. Create NewPassword 
    - UserInput to CreateNewPassword
        - Length 6 - 10 Characters
        - Contain >= 1 LowerCase and >1 UpperCase Character
        - Contain >= 1 number
      - Loop Until Requirements Fulfilled
    - UserInput to ConfirmPassword
        - ConfirmPassword should match InitialPassword
      - Loop Until True

  When Successful, Prompt Username and Password Has Been Successfully Created

b. ExistingUser Login

i. Match Existing Username
	- UserInput for EnterUsername
	- CrossCheck Database
		- If NoMatch, Give AnotherChance
			- Loop 3 times
			- Each unsuccessful attempt, give Error message
		- If Matching, Continue to UserPassword Prompt

ii. Match Existing Password
	- UserInput for EnterPassword
	- CrossCheck Database
		- If Not Matching, 
			Loop 3 times, give Error Message every attempt
		If Matching, 
			Grant as success and return Password 

Welcome username