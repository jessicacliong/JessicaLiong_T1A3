# Snooze It

GitHub Respository: https://github.com/jessicacliong/JessicaLiong_T1A3

Source Control of Respository: https://github.com/jessicacliong/JessicaLiong_T1A3/commits/main

Project Management Platform: https://trello.com/b/QnfB52xz/snooze-it-application

Video Presentation:


## Purpose & Scope
Snooze It is an application that allows users to store a range of sleep information. This will save a user's sleeping hours on a daily basis, quality of sleep in accordance with other factors contributing to quality of sleep. The application will also allow users to view a summary of their sleep information over periods of a week, a month and 3 months.

The purpose of this project is to demonstrate my current skills and ability in a range of developer tools encompassing the python programming language. 
This project will also stretch my ability to design, implement and test an application, where in this project it will be creating a terminal (command line) application. 

## Target Audience
The application is targeted for users of any age and gender who is able to run the application using the help documentation below on their computer terminal and log in inputs are welcome to utilise the application. 

## Features

### 1. Utilise an Account
The application allows users to register for an account and save their sleep information. 
Existing users can also log in using their credentials to access their personal information.  

### 1. Log Daily Sleep Times & Factors Affecting Sleep
Users are able to log in sleep time every day and keep track of the quality of their sleep, whether they had a goodnight's sleep or they didn't, rating it from 1-10.
The application allows users to write down comments and factors during the day or during the night before they slept that could impact the user's sleep.

### 2. Sleep Report (1 Day)
Gives user a report of their sleep time, quality, and other associated sleep information including a journal of a desired date. Users input a desired date and the information of their sleep conditions will be displayed on their terminal. 

### 3. Sleep Report before current date (Up to 7 consecutive days)
Gives users a report of their sleep time, quality and other relevant sleep information over a period of 1 week period before current date. The 1 week period can be specified through user inputs of the desired start date and end date. Available sleep logs saved in the system will be displayed to the user as a terminal output. 
Note: The 1 week period specified will include the start date and the end date defined by the user, if a log for those dates exist in record.   

### 3. Suggest Tips on better Sleep
Upon the completion of a sleep log entry, user's will be given a sleep tip on their terminal window to help them gain ample quantity and quality sleep for a more productive day.

## Implementation Plan

To implement the development steps of my application, I utilised Trello to keep note of all of my progress, the different features of my application and the to-do list for every feature to be completed. I listed every task that was required to do for each feature, categorised them accordingly and gave each task a deadline date to complete the task by.  

Every time a task is completed, the date deadline box can be clicked to give a green box with a tick, which marks the task as completed on trello. 

Figure 1 shows my trello board on the 6th of May

Figure 4 shows my trello board on the 22nd of May


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

__Feature 2 - Ouput Previous Sleep Log (High Priority)__

1. Import PandasModule
2. Create ReadCSV object of User_Information using DataFrame Feature of Pandas Module. 
3. PromptUser To Enter InputDate (DD-MM-YYYY)
4. Convert InputDateFormat to pandas DateTime Format
5. Filter InputDate Using Pandas DataFrame For InputDate == ExistingUserInformation
6. If MatchFound, Print Output Onto UserTerminal
7. If NotMatchFound, Print NoInputError & Print EmptyLog
8. Return to MainMenuLogSearchOptions

__Feature 3 - Output Previous 7 Days Sleep Logs from Current Day(High Priority)__

1. Create ReadCSV object of User_Information using DataFrame Feature of Pandas Module. 
2. PromptUser To Enter StartDate (DD-MM-YYYY)
3. PromptUser To Enter EndDate (DD-MM-YYYY)
4. Check if StartDate to EndDate = 7 Days, if not, PromptUser with LogPeriodError & Repeat From Step 2 Until CorrectPeriod Obtained
5. Filter StartDate <= LogDates In ExistingUserInformation.Csv <= EndDate with Pandas DataFrameFunctionality
6. Locate Rows Within PandasDataFrame
7. Print Output of SleepLogs Onto UserTerminal 
6. If NoMatchFound, Print EmptyDataFrameError & Print EmptyLog
7. Return to MainMenuLogSearchOptions

__Feature 4 - Ouput Sleep Tip (High Priority)__

1. Create ListOfSleepTips on CsvFile
2. ReadFunction CSVModule To Read SleepingTip From Sleep_Tips.Csv File (SkippingFileHeader)
3. Randomise Row
4. After SleepInformationInput Made, Print Random SleepingTip onto UserTerminal 

## Installation Instructions

## Dependencies

## References

__Python Coding__

https://automatetheboringstuff.com/2e/chapter16/

Inserting Input into CSV
https://stackoverflow.com/questions/55980027/building-a-csv-based-on-user-input

File Handling Lecture - Harvard University
https://cs50.harvard.edu/python/2022/notes/6/

PEP-8 Documentation
https://peps.python.org/pep-0008/

Python Date String Testing
https://stackoverflow.com/questions/18610884/python-date-string-testing

Writing & Reading CSV file Python
https://stackoverflow.com/questions/14978575/writing-reading-the-same-csv-file-in-python

Printing data using DataFrames in Pandas
https://stackoverflow.com/questions/64817406/fetching-particular-rows-of-a-csv-file-where-date-matches-as-entered-by-user

DateTime in Pandas: An Uncomplicated Guide (2023)
https://www.dataquest.io/blog/datetime-in-pandas/#:~:text=Now%2C%20the%20data%20type%20of,precision%20of%20the%20DateTime%20object.

Searching Records between 2 dates in CSV File
https://stackoverflow.com/questions/62058695/searching-for-records-between-two-dates-and-two-times-in-csv-file-using-python-p

__Testing__

Exceptions Documentation
https://docs.python.org/3/library/exceptions.html#Exception

CSV Documentation
https://docs.python.org/3/library/csv.html#reader-objects


## Further Development of Application

If time permitted, the application could have a login feature where each user could have individual access to their own sleep information in separate accounts, allowing for separation of sleep logs to tailor an individual's search function and enhance the privacy of an individual's sleep journals and logs. 

Pseudocode for Feature 5 - User Login Feature

 Login Feature (If Time Permiting)__  

1. Log In Menu, Prompts 2 Options:
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