#This is the optimized solution on the leap year algorithm or program
#I think it's a wrong algorithm or solution much as it has optimised,
#The issue is,according to the given information,a leap year can't be..
#..a multiple of four and hundred at the same time, 

year = input("Type a year : ")

year = int(year)

if year % 400 == 0 or(year % 4 == 0 and year % 100 != 0):
    print("The typed year is a leap year")
else:
    print("The typed year isn't a leap one")
