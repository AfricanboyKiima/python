#Boolean data type is very important and it holds only two values ie True and False
#An example to follow or look at is testing if a user is above eighteen years of age and above
#In addition,boolean data types therefore are either true or false
age = input("Please insert your age for testing : ")

age =  int(age)

olderthan_18 = False


if age >= 18:
    olderthan_18 = True
else:
    olderthan_18 = False


if olderthan_18:
    print("You are an adult dear user")
else:
    print("You are not an adult")
