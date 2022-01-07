#Insert year from user

year = input("Type a year : ")#Store year in variable

year = int(year)#int function converts the inserted number into an int data type

leapyear = False #had to create this variable called leapyear to enable me deal with True and False boolean values
#Initialised leapyear to False such that 
if year % 4 == 0:
    
    leapyear = True
    
elif year % 100 == 0:
    
    leapyear = False
    
elif year % 400 == 0:
    
    leapyear = True
    
else:
    
    leapyear = False

if leapyear:
    
    print("The typed year is a leap one")
    s
else:
    
    print("The typed year isn't a leap one")
    

