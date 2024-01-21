# This program is by Yoyo Liu 
# Completed in 2021 
# Uploaded to Github on 1/21/2024

day_number = {
  1 : 'Monday',
  2: 'Tuesday',
  3: 'Wednesday',
  4: 'Thursday',
  5: 'Friday',
  6: 'Saturday',
  7: 'Sunday'
}#days of the week

def ask_for_day():
  print("Today is ____ ")
  day = input("1: Monday\n2: Tuesday\n3: Wednesday\n4: Thursday\n5: Friday\n6: Saturday\n7: Sunday\n")#ask for the day
  return day

def ask_for_holiday():
  leave = input("Awesome! I will be leaving in ____ days. \n")#ask for leaving in
  return leave

def calculate(m, n):
  day = (m + n)% 7#calculate which day it's leaving
  return day

loop_num2 = True
while loop_num2:#user run again loop
  loop_num1 = 0#user input error checking loop
  while loop_num1 == 0: 
    try: 
      day = int(ask_for_day())
      if day in range(1, 8):
        leave = int(ask_for_holiday())#check if day is valid
        if leave < 0:
          y = 1/0#if day is invalid, make error
        else: 
          break
          loop_num1 = 1#break the loop is everything is fine
      else: 
        y = 1/0
    except: 
      print("Please enter a valid number.\n")#if the input is bad

  the_day = calculate(day, leave)#calculate the day

  print("Okay, so you will leave on a " + day_number[the_day] + "!")#output for user
  again = input("Having other time in mind? (press 'y' to try again, anything else to quit the program)\n")#ask the user if they want to do it again
  if again != 'y':
    loop_num2 = False

print("Thank you for using the program! Have a great day!")#thank you note