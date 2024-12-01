#!/usr/bin/env python
# python advent calendar (24 'doors')
import datetime
import time
import random

start_month_day = (12, 1) # 1st Dec
end_month_day = (12, 24)  # 24th Dec

# get current date
current_date = datetime.datetime.now()
current_month_day = (current_date.month, current_date.day)

# Current date in dd/mm
current_date = datetime.datetime.now()
current_month_day = (current_date.month, current_date.day)

# Check if current date is between 01/12 and 34/12 
if start_month_day <= current_month_day <= end_month_day:    
    print("Hello there. This is your advent calendar!")
    time.sleep(1.5)  # Wait 1.5 Sekunden
else:
    print("Hello there.")
    time.sleep(1.5)  # Wait 1.5 Sekunden
    print("Today is", current_date.strftime("%d/%m/%Y"))
    time.sleep(1.5)  # Wait 1.5 Sekunden
    print("Sorry, but today is not the day you are looking for.")
    print("Please come back again when the time has arrived.")
    exit()

# If date is between 01/12 and 31/12, then continue:
user_input = input("Would you like to open today's door? (y/n): ").strip().lower()

if user_input == 'n':
    print("Alright, then next time.")
    print("See you soon, my friend!")
    exit()
elif user_input == 'y':
    # Day and Christmas Text
    day_number = current_date.day
    print(f"Alright. Here is your door number {day_number}:")
    time.sleep(1)  # Wait 1sec

    # Dictionary with Chrstmas texts
    quotes = {
        1: "Merry Christmas! May your day be filled with joy and happiness.",
        2: "Ho Ho Ho! Santa is on his way!",
        3: "Wishing you a season of gladness and a New Year of hope.",
        4: "May your holidays be filled with warmth and love.",
        5: "Sending you warm wishes for a wonderful holiday season.",
        6: "May your days be merry and bright!",
        7: "Wishing you a holiday season filled with happiness and joy.",
        8: "May your holidays be filled with the magic of the season.",
        9: "Sending you warm wishes for a joyous holiday season.",
        10: "May your holidays be filled with love and laughter.",
        11: "Wishing you a holiday season filled with peace and joy.",
        12: "May your holidays be merry and bright!",
        13: "Sending you warm wishes for a wonderful holiday season.",
        14: "May your days be merry and bright!",
        15: "Wishing you a holiday season filled with happiness and joy.",
        16: "May your holidays be filled with the magic of the season.",
        17: "Sending you warm wishes for a joyous holiday season.",
        18: "May your holidays be filled with love and laughter.",
        19: "Wishing you a holiday season filled with peace and joy.",
        20: "May your holidays be merry and bright!",
        21: "Sending you warm wishes for a wonderful holiday season.",
        22: "May your days be merry and bright!",
        23: "Wishing you a holiday season filled with happiness and joy.",
        24: "Merry Christmas! May your day be filled with joy and happiness."
    }

    # A Christmas Text from Dictionary
    quote = quotes.get(day_number, "Happy Holidays!")
    print(" ")
    print(quote)
    time.sleep(3)
    print(" ")
    print("I hope you liked today's door.")
    print("See you tomorrow!")
    print(" ")
else:
    print("Invalid input. Please enter 'y' or 'n'.")
    exit()