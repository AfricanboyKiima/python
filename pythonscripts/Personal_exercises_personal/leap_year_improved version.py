#I am writing this python program to test if a number is a leap year or not
#We have 365.25 days in a year but in our calender this is normally shortened to 365 days only, to make up for the missing .25 days,after approximately every four years,
#..a day is added to the years to make up for the .25years. One thing to note is that leap years are normally multiples of four but not of 100,meanwhile,
#leap years can also be multiples of 400 to.
"""
EXPLANATION
if the year is a multiple of four,check if it's a multiple of 100,
if it's amultiple of 4 but not 100,then it's a leap  year,
if it's a multiple of 4 and 100 at the same time,then it's not a leap year,
if it's a multiple of 400;it's also a leap year.
NOTE
Mutliples of a number are the results we get after multiplying a certain number by integers.
"""
#WE ARE TO USE A FUNCTION IN THIS WORK
def leap_year(year):
 leap_year = False
if year % 4 == 0:
    leap_year = True
elif year % 100 == 0:
    leap_year = False
elif year % 400 == 0:
    leap_year = True
else:
    leap_year = False
    if leap_year  == True:
        print("This is a leap year")
    else:
            print("This isn't a leap year")
