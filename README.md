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


Figure 2 shows my trello board on the 11th of May


## Psuedocodes

As a part of my implementation plan, I decided to write pseudocodes to outline the workings of each application features, methods and functions that will be used to accomplish the set features with python coding.

__Feature 1 - Request User inputs on a range of sleep information (High Priority)__

1. Open NewCSV for file UniqueIndividual
2. Prompt User Range of SleepInformation
3. Write Input with DictWriter into CSVFile
4. Utilise pandas to output Data by Date

__Feature 2 - Filter Inputs to 1 week, 1 month and 3 months (High Priority)__

1. Utilise PandasModule to Filter User’sSleepInformation to 1Week, 1Month and 3Months


__Feature 3 - Helpful Sleeping Tips (High Priority)__

After SleepInformation SuccessfulEntries, Display SleepingTips for User

__Feature 4 - LogIn Feature (Low Priority)__  
1. Log In Menu, Prompts 2 Options:
	a. Create NewUser
	b. Login As Existing User

a. Creating NewUser

i. Creating NewUsername
    - UserInput To CreateNewUsername
    - CrossCheck Database 
      	If Exists, Enter Different Username
      Loop Until input is Unique
 When successful, Save to Database

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

Welcome {username}

## Installation Instructions

## Dependencies

## Sources
