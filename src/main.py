import csv
import datetime
import random
import pandas

# class Input_Variables:
#   def __init__(self, date, hours_of_sleep, quality_of_sleep, caffeine, comments, other_comments):
#     self.date = date
#     self.hours_of_sleep = hours_of_sleep
#     self.quality_of_sleep = quality_of_sleep
#     self.caffeine = caffeine
#     self.comments = comments
#     self.other_comments = other_comments

# def user_input():
  # year = int(input('Enter a year of the log: '))
  # month = int(input('Enter a month of the log: '))
  # day = int(input('Enter a date of the log: '))
  # date = datetime.date(year, month, day)
  # hours_of_sleep = int(input("How many hours did you sleep? "))
  # quality_of_sleep = int(input("From a scale of 1 to 10 how would you rate your sleep? "))
  # caffeine = input("Did you have any coffee in the afternoon/evening? Enter: (Y/N) ")
  # comments = input("Do you want to enter any other comments? Enter: (Y/N) ")
  # if comments == 'N':
  #   other_comments = ('')
  #   print("Thank you for using Snooze It. Your data has been saved! ")
  # else:
  #   other_comments = input("Please enter comments: (Press <Enter> to Continue) ")
  #   print("Thank you for using Snooze It. Your data has been saved! ")

# def write_user_input(user_input):
#   with open('user_information.csv', 'a', newline='') as file:
#     headers = ['Date', 'Hours of Sleep', 'Quality of Sleep', 'Caffeine', 'Comments', 'Other Comments']
#     outputDictWriter.writerow({'Date': date, 'Hours of Sleep': hours_of_sleep, 'Quality of Sleep': quality_of_sleep, 'Caffeine': caffeine, 'Comments': comments, 'Other Comments': other_comments})

def sleep_tip():
  with open("sleep_tips.csv", "r") as f:
    csv_reader = csv.reader(f)
    sleep_tips = list(csv_reader)[1:]
    print(f'Fun Sleep Tip: {random.choice(sleep_tips)}')

def filtered_sleep_input():
  pass



# user_input()
# # write_user_input()
sleep_tip()
# filtered_sleep_input()