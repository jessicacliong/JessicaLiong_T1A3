import csv
import time
import dateutil


def user_sleep_input():
  date = input("What is the date of your log? (Please format in MM/DD/YYYY): ")
  hours_of_sleep = int(input("How many hours did you sleep? "))
  quality_of_sleep = int(input("From a scale of 1 to 10 how would you rate your sleep? "))
  caffeine = input("Did you have any coffee in the afternoon/evening? Enter: (Y/N) ")
  comments = input("Do you want to enter any other comments? Enter: (Y/N) ")
  if comments == 'N':
    other_comments = ('')
    print("Thank you for using Snooze It. Your data has been saved! ")
  else:
    other_comments = input("Please enter comments: (Press <Enter> to Continue) ")
    print("Thank you for using Snooze It. Your data has been saved! ")


    file = open('user_information.csv', 'a', newline='')
    headers = ['Date', 'Hours of Sleep', 'Quality of Sleep', 'Caffeine', 'Comments', 'Other Comments']
    outputDictWriter = csv.DictWriter(file, headers)
    outputDictWriter.writeheader()
    outputDictWriter.writerow({'Date': date, 'Hours of Sleep': hours_of_sleep, 'Quality of Sleep': quality_of_sleep, 'Caffeine': caffeine, 'Comments': comments, 'Other Comments': other_comments})
    file.close()

# def sleep_tip():
  # write sleeping tips on a separate file
  # generate random sentence from file
  # print(tip)

user_sleep_input()
  # sleep_tip()
