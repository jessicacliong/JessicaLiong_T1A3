# SnoozeIt

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

### 1. Log Daily Sleep Times & factors contributing to Sleep
Users are able to log in sleep time every day and keep track of the quality of their sleep, whether they had a goodnight's sleep or they didn't, rating it from 1-10.
The application allows users to write down comments and factors during the day or during the night before they slept that could impact the user's sleep.

### 2. Sleep Reports
Gives user reports of their sleep time, quality and other factors or comments associated with that sleep within certain time perioeds. I have filtered them to 1 week, 1 month and 3 months.

### 3. Suggest Tips on better Sleep
Gives users useful tips to help them gain ample quantity and quality sleep for a more productive day

## Implementation Plan

To implement the development steps of my application, I utilised Trello to keep note of all of my progress, the different features of my application and the to-do list for every feature to be completed. I listed every task that was required to do for each feature, categorised them accordingly and gave each task a deadline date to complete the task by.  

Every time a task is completed, the date deadline box can be clicked to give a green box with a tick, which marks the task as completed on trello. 

Figure 1 shows my trello board on the 6th of May

Figure 3 shows my trello board on the 19th of May

Figure 4 shows my trello board on the 21st of May


## Psuedocodes

As a part of my implementation plan, I have written pseudocodes to outline the methods and functions that will be used to accomplish the features of my application utilising python code.

__Feature 1 - Request User inputs on a range of sleep information (High Priority)__

1. UserInformation CSV Created Prior to SleepInformationInput
2. Prompt User With SleepInformationInput
3. Write RowInputs With DictWriter into CSVFile

__Feature 2 - Ouput Previous Sleep Log Based on Date (High Priority)__

1. Import PandasModule
2. Filter UserSleepInformation to ReadDates
3. Obtain Date
4. Print Output onto CSVFile

or 

1. PromptUser To View A PreviousLog
2. PromptUser Enter InputDate (YYYY-MM-DD)
3. Read CSV File using DictReader using InputDate as Filter/Key
4. Print Output Onto UserTerminal 


__Feature 3 - Ouput Sleeping Tip (High Priority)__

1. After SleepInformationInput
2. Create ListOfSleepTips on CsvFile
3. ReadFunction CSVModule To Read SleepingTip From Sleep_Tips.Csv File
4. RandomModule 
5. Print SleepingTip

__Feature 4 - Login Feature (If Time Permiting)__  

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

## Installation Instructions

## Dependencies

## References

__Python Coding__

https://automatetheboringstuff.com/2e/chapter16/


https://stackoverflow.com/questions/55980027/building-a-csv-based-on-user-input

https://cs50.harvard.edu/python/2022/notes/6/

PEP8 Documentation
https://peps.python.org/pep-0008/

Python Date String Testing
https://stackoverflow.com/questions/18610884/python-date-string-testing

Writing & Reading CSV file Python
https://stackoverflow.com/questions/14978575/writing-reading-the-same-csv-file-in-python

__Testing__

Exceptions Documentation
https://docs.python.org/3/library/exceptions.html#Exception

Monkeypatch Documentation
https://docs.pytest.org/en/7.1.x/_modules/_pytest/monkeypatch.html

CSV Documentation
https://docs.python.org/3/library/csv.html#reader-objects

Pytest Documentation
https://docs.pytest.org/en/7.3.x/

