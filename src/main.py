import csv
import datetime as dt
from datetime import timedelta
import random
import pandas as pd
from simple_term_menu import TerminalMenu
from unique_exceptions import InvalidYearError, InvalidMonthError, InvalidDateError, RangeError
from unique_exceptions import NegativeError, NumberInputError, SleepTimeError, InvalidInputError, EmptyDataError, DateExistsError

def main_greeting():
  print("Welcome to Snooze It!")
main_greeting()

def user_input():
  year = int(input("Please enter the year of the log (YYYY): "))
  currentYear = dt.datetime.now().year

  if type(year) is not int:
    raise ValueError()
  if year > currentYear or year < 2023 or year > 9999:
    raise InvalidYearError()

  month = int(input("Please enter the month of the log (M / MM): "))
  currentMonth = dt.datetime.now().month

  if type(month) is not int:
    raise ValueError()
  if month > currentMonth or year > currentYear:
    raise InvalidMonthError()
  if month < 1:
    raise RangeError()

  day = int(input("Please enter the date of the log (D / DD): "))
  currentDate = dt.datetime.now().day

  if type(day) is not int:
    raise ValueError()
  if day > currentDate or month > currentMonth or year > currentYear:
    raise InvalidDateError()
  if day < 1:
    raise RangeError()

  date = dt.date(year, month, day)

  hours_of_sleep = float(input("How many hours did you sleep? (Press <Enter> to continue): "))

  if hours_of_sleep < 0:
    raise NegativeError()
  if type(hours_of_sleep) is not float:
    raise ValueError()
  if hours_of_sleep > 24:
    raise SleepTimeError()

  quality_of_sleep = int(input("On a scale of 0 (No Sleep) to 10 (Excellent), how would you rate your sleep? \n(Press <Enter> to continue):\n "))

  if quality_of_sleep > 10:
    raise NumberInputError()
  if quality_of_sleep < 0:
    raise NegativeError()
  if type(quality_of_sleep) is not int:
    raise ValueError()

  caffeine = input("Did you have any coffee in the afternoon/evening? \n(Enter (Y/N) & press <Enter> to continue):\n ")
  if caffeine.upper() != "Y" and caffeine.upper() != "N":
    raise InvalidInputError()

  journal = input("Would you like to enter a sleep journal? \n(Enter (Y/N) & press <Enter> to continue):\n ")
  if journal.upper() != "Y" and journal.upper() != "N":
      raise InvalidInputError()

  if journal == 'N':
    journal_entry = ('')
    print("Thank you for using Snooze It. Your data has been saved! ")
  elif journal == 'Y':
    journal_entry = input('Please write your entry \n(Press <Enter> to Continue):\n ')
  return date, hours_of_sleep, quality_of_sleep, caffeine, journal, journal_entry

def write_user_input(date, hours_of_sleep, quality_of_sleep, caffeine, journal, journal_entry):
  with open('user_information.csv', 'a', newline='') as file:
    headers = ['Log Date', 'Hours of Sleep', 'Quality of Sleep (1-10)', 'Caffeine Intake', 'Write Journal', 'Journal Entry']
    outputDictWriter = csv.DictWriter(file, headers)
    outputDictWriter.writerow({'Log Date': date, 'Hours of Sleep': hours_of_sleep, 'Quality of Sleep (1-10)': quality_of_sleep, 'Caffeine Intake': caffeine, 'Write Journal': journal, 'Journal Entry': journal_entry})
    print("Thank you for using Snooze It. Your data has been saved!")

def sleep_tip():
  with open("sleep_tips.csv", "r") as f:
    csv_reader = csv.reader(f)
    sleep_tips = list(csv_reader)[1:]
  print(f'\nSleep Tip: {random.choice(sleep_tips)}\n')

def log_search_day():
  df = pd.read_csv("user_information.csv")
  df2 = pd.to_datetime(df['Log Date'], format='%Y-%m-%d')
  date = input("Please enter the date of the log (YYYY-MM-DD), then press <Enter>: ")
  search_date = dt.datetime.strptime(date, "%Y-%m-%d")
  current_date = dt.datetime.now()
  if search_date > current_date:
    raise InvalidDateError()
  filtered_df = df[df2 == search_date]
  if filtered_df.empty == True:
    raise EmptyDataError()
  print(f'We have found the following log for the {search_date}:')
  print(filtered_df)
  return filtered_df

def log_search_week():
  df = pd.read_csv("user_information.csv")
  df2 = pd.to_datetime(df['Log Date'], format='%Y-%m-%d')
  start_date_raw = input("Please enter a date to backtrack from in (YYYY-MM-DD), then press <Enter> : ")
  start_date = dt.datetime.strptime(start_date_raw, '%Y-%m-%d')
  if start_date > dt.datetime.now():
    raise InvalidDateError()
  end_date = start_date - timedelta(days=7)
  mask = (df2 <= start_date) & (df2 > end_date)
  df3 = df.loc[mask]
  if df3.empty == True:
    raise EmptyDataError()
  print(f'We have found the following sleep logs ranging from {start_date} to {end_date}:')
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
  terminal_menu = TerminalMenu(search_options)
  search_entry_index = terminal_menu.show()
  search_choice = search_options[search_entry_index]
  return search_choice

while True:
  search_choice = main_menu()
  if search_choice == "Enter A New Sleep Log":
    print("You have chosen to enter a new sleep log")
    try:
      date, hours_of_sleep, quality_of_sleep, caffeine, journal, journal_entry = user_input()
      write_user_input(date, hours_of_sleep, quality_of_sleep, caffeine, journal, journal_entry)
    except ValueError as e:
      print(type(e))
      if('invalid literal for int()' in str(e)):
        print("An invalid character(s) has been entered. Please enter numbers only")
      if('day is out of range for month' in str(e)):
        print("Day is out of range for month. Please enter correct dates for the month")
      if('could not convert string to float' in str(e)):
        print("An invalid character(s) has been entered. Please enter numbers only.")
    except InvalidYearError as e:
      print(type(e))
      print(e)
    except RangeError as e:
      print(type(e))
      print(e)
    except NumberInputError as e:
      print(type(e))
      print(e)
    except NegativeError as e:
      print(type(e))
      print(e)
    except InvalidMonthError as e:
      print(type(e))
      print(e)
    except InvalidDateError as e:
      print(type(e))
      print(e)
    except SleepTimeError as e:
      print(type(e))
      print(e)
    except InvalidInputError as e:
      print(type(e))
      print(e)
    except DateExistsError as e:
      print(type(e))
      print(e)
    else:
      sleep_tip()
  elif search_choice == "View Previous Single Night Sleep Log":
    print("You have chosen to view a previous sleep log")
    try:
      log_period = log_search_day()
    except ValueError as e:
      if("does not match format '%Y-%m-%d'" in str(e)):
        print("Incorrect Date Format Entered. Please enter a date format within (YYYY-MM-DD) using numbers separated by '-' only.")
    except InvalidDateError as e:
      print(type(e))
      print(e)
    except EmptyDataError as e:
      print(type(e))
      print(e)
  elif search_choice == "View Previous 1 Week Sleep Log":
    print("You have chosen to view a week period of sleep logs")
    try:
      log_period = log_search_week()
    except InvalidDateError as e:
      print(type(e))
      print(e)
    except ValueError as e:
      print(type(e))
      if("does not match format '%Y-%m-%d'" in str(e)):
        print("Incorrect Date Format Entered. Please enter a date format within (YYYY-MM-DD) using numbers separated by '-' only.")
    except EmptyDataError as e:
      print(type(e))
      print(e)
  elif search_choice == 'End Application':
    print("You have chosen to End Application")
    log_period = end_application()
    break