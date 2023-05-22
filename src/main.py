import csv
import datetime as dt
import random
import pandas as pd
from simple_term_menu import TerminalMenu

def user_input():
  date = int(input("Enter the date of the log (DD): "))
  month = int(input("Enter the month of the log (MM): "))
  year = int(input("Enter the year of the log (YYYY): "))
  date = dt.date(year, month, date)
  hours_of_sleep = int(input("How many hours did you sleep? "))
  quality_of_sleep = int(input("From a scale of 1 to 10 how would you rate your sleep? "))
  caffeine = input("Did you have any coffee in the afternoon/evening? Enter: (Y/N) ")
  journal = input("Would you like to enter a sleep journal? Enter: (Y/N) ")
  if journal == 'N':
    journal_entry = ('')
    print("Thank you for using Snooze It. Your data has been saved! ")
  if journal == 'Y':
    journal_entry = input('Please write your entry: (Press <Enter> to Continue) ')
    print("Thank you for using Snooze It. Your data has been saved! ")
  return date, hours_of_sleep, quality_of_sleep, caffeine, journal, journal_entry

def write_user_input(date, hours_of_sleep, quality_of_sleep, caffeine, journal, journal_entry):
  with open('user_information.csv', 'a', newline='') as file:
    headers = ['Log Date', 'Hours of Sleep', 'Quality of Sleep (1-10)', 'Caffeine Intake', 'Write Journal', 'Journal Entry']
    outputDictWriter = csv.DictWriter(file, headers)
    outputDictWriter.writerow({'Log Date': date, 'Hours of Sleep': hours_of_sleep, 'Quality of Sleep (1-10)': quality_of_sleep, 'Caffeine Intake': caffeine, 'Write Journal': journal, 'Journal Entry': journal_entry})

def sleep_tip():
  with open("sleep_tips.csv", "r") as f:
    csv_reader = csv.reader(f)
    sleep_tips = list(csv_reader)[1:]
    print(f'Sleep Tip: {random.choice(sleep_tips)}')

def log_search_day():
  df = pd.read_csv("user_information.csv") 
  df['Log Date'] = pd.to_datetime(df['Log Date']) # converts data type into a datetime64[ns] object
  search_date = input("Enter the date of the log (DD-MM-YYYY): ")
  filtered_df = df[df['Log Date'] == search_date] # both the csv file and user input format are in strings, so don't need to convert to datetime object to compare the two inputs
  print(filtered_df)

def log_search_week():
  df = pd.read_csv("user_information.csv") 
  df['Log Date'] = pd.to_datetime(df['Log Date']) # converts data type into a datetime64[ns] object
  start_date = input("Enter the start date of the log (YYYY-MM-DD): ")
  end_date = input("Enter the last date of the log (YYYY-MM-DD): ")
  mask = (df['Log Date'] >= start_date) & (df['Log Date'] <= end_date)
  df2 = df.loc[mask]
  print(df2)

def end_application():
  print("Thank you for using Snooze It! Please come back again soon!")

date, hours_of_sleep, quality_of_sleep, caffeine, journal, journal_entry = user_input()
write_user_input(date, hours_of_sleep, quality_of_sleep, caffeine, journal, journal_entry)
sleep_tip()
log_search_day()
log_search_week()
end_application()