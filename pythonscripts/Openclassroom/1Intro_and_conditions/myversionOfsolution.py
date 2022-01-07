#This code is my own review code of openclassroom's LEAPYEAR testing
#In other words,it's a python script that tests if a year can be a leap one or not.
#"Apprenez à programmer en python" is the title from openclassrooms.com
"""
NASA PERSONNAL RESEARCH
According to nasa's website,a year has approximately 365.25 days,however,in a calender year,a year is made of 365 days i.e Sollar year,
in order to make up for the remaing days,after four years,a day is added to one of the months of the year which is february,
we normally have 28 days in february but in other years,we find that it is made of 29 days i.e
Let's look at an example

2004 = leap year
2005 = Not leap year
2006 = Not leap year
2007 = Not leap year
2008 = Leap year
From the above,we notice that approximately after every four years,a day is added to a year making it 366 days instead of 365 days that we normally have

"""




"""
EXPLANATION
if it is a multiple of four,
then check if it is a multiple of four and a hundred,
else,check if it is a multiple of four hundred
if it is a multiple of four only,then it is a leap year
if it is a multiple of both four and one hundred ,
then it is not a leap year,
if it is a multiple of 400 too,then it is also a leap year.
"""
year = input("Please input year to be tested : ")#Asking user to input data using the input function that..
# receives data and returns that same data to be inserted into our variabel called "year".

year = int(year)#Since input variable returns values of string type regardless of the data type inserted
#...we use the int function to convert our value into an int data type.

leapyear = False #First initialised my variable to false such that it is converted..
#...into a true boolean value under certain conditions our case being testing if a year is leap,
#NOTE: A year is only leap if it a multiple of four except if it is a multiple of 100,it is also leap if it is a multiple of 400.

if year % 4 != 0:
    leapyear = False
elif year % 100 == 0:
    leapyear = False
elif year % 400 == 0:
    leapyear = True
else:
    leapyear = True

if leapyear:
    print("It's a leap year")
else:
    print("It's not a leap year")
    
#TO RUN THIS PROGRAM PRESS (WINDOWS + R)
    
