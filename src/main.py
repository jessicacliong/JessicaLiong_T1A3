import csv

def user_sleep_input():
  date = input("What is the date of your log? (YYYY/MM/DD) ")
  hours_of_sleep = input("How many hours did you sleep? ")
  quality_of_sleep = input("From a scale of 1 to 10 how would you rate your sleep? ")
  caffeine = input("Did you have any coffee in the afternoon/evening? Enter: (Y/N) ")
  blue_screen = input("Did you have any screen time before sleeping? Enter: (Y/N) ")
  screen_time = input("How many hours? ")
  comments = input("Do you want to enter any other comments? Enter: (Y/N) ")
  if comments == 'N':
    other_comments = ('')
    print("Thank you for using Snooze It. Your data has been saved! ")
  else:
    other_comments = input("Please enter comments: (Press Enter to Continue) ")
    print("Thank you for using Snooze It. Your data has been saved! ")
 
  outputFile = open('user_information.csv', 'a', newline='')
  outputDictWriter = csv.DictWriter(outputFile, ['Date', 'Hours of Sleep', 'Quality of Sleep', 'Caffeine', 'Blue Screen', 'Screen Time', 'Comments', 'Other Comments'])
  outputDictWriter.writeheader()
  outputDictWriter.writerow({'Date': date, 'Hours of Sleep': hours_of_sleep, 'Quality of Sleep': quality_of_sleep, 'Caffeine': caffeine, 'Blue Screen': blue_screen, 'Screen Time': screen_time, 'Comments': comments, 'Other Comments': other_comments})

def sleep_tip():
  generate random tip from file 
  print(random tip)

user_sleep_input()