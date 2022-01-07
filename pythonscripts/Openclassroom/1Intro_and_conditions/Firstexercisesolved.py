#My first python exercise from Open classroom's "LEARN TO PROGRAM IN PYTHON"
#Been introduced to python and learnt what it is and how one can use the interprete
#..to do stuff with it,indentation is a very important thing to consider when
#..dealing with python i.e spacing one's instructions
##############################################################################
#A year is considered as leap if it's a multiple of four unless it's a multiple
#of 100.....it's also considered as leap if it's a multiple of 400....

year = input("Please insert the year to be tested:  ")
type(year)
print(year)
year = int(year)
if year % 4 > 0 or year % 4 < 0:
    print("Year inserted is not a leap one.")
elif year % 4 == 0 and year % 100 == 0:
    print("Not a leap year.")
elif year % 4 == 0:
    print("Year inserted is a leap year.")
elif year % 400 == 0:
    print("Year is also a leap year.")
else:
    print("It is a leap  year.")
