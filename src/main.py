import csv
import datetime as dt
import random
import pandas as pd
from simple_term_menu import TerminalMenu

def main_greeting():
  print( "Welcome to Snooze It!")

main_greeting()

def user_input():
  year = int(input("Please enter the year of the log (YYYY): "))
  month = int(input("Please enter the month of the log (MM): "))
  date = int(input("Please enter the date of the log (DD): "))
  date = dt.date(year, month, date)
  hours_of_sleep = int(input("How many hours did you sleep? "))
  quality_of_sleep = int(input("On a scale of 1 (Poor) to 10 (Excellent), how would you rate your sleep? "))
  caffeine = input("Did you have any coffee in the afternoon/evening? Enter: (Y/N) ")
  journal = input("Would you like to enter a sleep journal? Enter: (Y/N) ")
  if journal == 'N':
    journal_entry = ('')
    print("Thank you for using Snooze It. Your data has been saved! ")
  elif journal == 'Y':
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
    print(f'\nSleep Tip: {random.choice(sleep_tips)}\n')

def log_search_day():
    df = pd.read_csv("user_information.csv") 
    df['Log Date'] = pd.to_datetime(df['Log Date'], format='%Y-%m-%d') # converts data type into a datetime64[ns] object
    search_date = input("Please enter the date of the log (YYYY-MM-DD), then press <Enter> : ")
    filtered_df = df[df['Log Date'] == search_date]
    print(filtered_df)
    return filtered_df

def log_search_week():
  df = pd.read_csv("user_information.csv") 
  df['Log Date'] = pd.to_datetime(df['Log Date'], format='%Y-%m-%d') # converts data type into a datetime64[ns] object
  start_date = input("Please enter the start date of the log (YYYY-MM-DD), then press <Enter> : ")
  end_date = input("Please enter the last date of the log (YYYY-MM-DD), then press <Enter> : ")
  mask = (df['Log Date'] >= start_date) & (df['Log Date'] <= end_date) # greater than the start date and smaller than the end date
  df2 = df.loc[mask]
  print(df2)
  return df2

def end_application():
  print("Thank you for using Snooze It! Please come back again soon!")

def main_menu():
  print("\nPlease Choose From the Following Options:\n"
        "\n(Use the Up & Down Navigation keys to Navigate The Menu.)\n"
        "\n(Press <Enter> to Select an Option)\n")
  search_options = [
                    "Enter A New Sleep Log",
                    "View Previous Single Night Sleep Log",
                    "View Previous 1 Week Sleep Log",
                    "End Application",
                  ]
  while True:
    terminal_menu = TerminalMenu(search_options)
    search_entry_index = terminal_menu.show()
    search_choice = search_options[search_entry_index]
    return search_choice

while True:
  search_choice = main_menu()
  if search_choice == "Enter A New Sleep Log":
    print("You have chosen to enter a new sleep log")
    date, hours_of_sleep, quality_of_sleep, caffeine, journal, journal_entry = user_input()
    write_user_input(date, hours_of_sleep, quality_of_sleep, caffeine, journal, journal_entry)
    sleep_tip()
  elif search_choice == "View Previous Single Night Sleep Log":
    print("You have chosen to view a previous sleep log")
    log_period = log_search_day()
  elif search_choice == "View Previous 1 Week Sleep Log":
    print("You have chosen to search for a 1 week sleep log")
    log_period = log_search_week()
  elif search_choice == 'End Application':
    print("You have chosen to End Application")
    log_period = end_application()
    break