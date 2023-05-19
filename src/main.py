import csv
import datetime
import random

def user_input():
  year = int(input('Enter the year of the log (YYYY): '))
  month = int(input('Enter the month of the log (MM): '))
  day = int(input('Enter the date of the log (DD): '))
  date = datetime.date(year, month, day)
  hours_of_sleep = int(input("How many hours did you sleep? "))
  quality_of_sleep = int(input("From a scale of 1 to 10 how would you rate your sleep? "))
  caffeine = input("Did you have any coffee in the afternoon/evening? Enter: (Y/N) ")
  journal = input("Would you like to enter a sleep journal? Enter: (Y/N) ")
  if journal == 'N':
    journal_entry = ('')
    print("Thank you for using Snooze It. Your data has been saved! ")
  else:
    journal_entry = input("Please enter an entry: (Press <Enter> to Continue) ")
    print("Thank you for using Snooze It. Your data has been saved! ")
  return date, hours_of_sleep, quality_of_sleep, caffeine, journal, journal_entry 

def write_user_input(date, hours_of_sleep, quality_of_sleep, caffeine, journal, journal_entry):
  with open('user_information.csv', 'a', newline='') as file:
    headers = ['Date', 'Hours of Sleep', 'Quality of Sleep (1-10)', 'Caffeine Intake', 'Journal', 'Journal Entry']
    outputDictWriter = csv.DictWriter(file, headers)
    outputDictWriter.writerow({'Date': date, 'Hours of Sleep': hours_of_sleep, 'Quality of Sleep (1-10)': quality_of_sleep, 'Caffeine Intake': caffeine, 'Journal': journal, 'Journal Entry': journal_entry})

def sleep_tip():
  with open("sleep_tips.csv", "r") as f:
    csv_reader = csv.reader(f)
    sleep_tips = list(csv_reader)[1:]
    print(f'Sleep Tip: {random.choice(sleep_tips)}')

def sleep_log_search():
  user_search = input("Would you like to view your previous sleep logs? Enter: (Y/N) ")
  if user_input == "Y":
    date_search = input("Please enter the date (YYYY-MM-DD) of the log you wish to view :")

  else:
    print("Thank you for using Snooze It. This program will now terminate. ")  
    
open csv File
read data from csv using pandas
print to terminal for user to read

# user_input()
# write_user_input()
sleep_tip()
# sleep_log_search()
write_user_input(user_input())
