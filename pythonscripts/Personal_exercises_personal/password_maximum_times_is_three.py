#This script is source code that i wrote asking a user to input their password they are
#...asked thrice to rewrite the password if it's not correct,once the number of trials is over,
#...the program ends and are told how they've reached the maximum number of trials

#NOTE this code has a bug as it's not really giving me what i really want
i = 0
password = ""
while i < 3:
    while password != "kiima1234":
        password = input("Please insert your password dear customer : ")
        if password == "kiima1234":
            print("You have been granted access to the site")
            break
        else:
            break
    i+=1
if i == 3:
    print("You have reached the maximum number of trials")
else:
    print("You can now enjoy the feautures of our site")
