#A script is a file that contains code meant to be executed as a program
#This is a python script on how to use the continue key word.
#Just like break,continue is used in loops too,it is used to continue a loop,
#what happens is that when the program execution reaches the continue statement,
#it immediately goes back to the start of the loop and reevaluates the loop's condition

#WE ARE WRITING A PROGRAM THAT ENABLES US TO ASK FOR THE PASSWORD AND NAME OF A PERSON USING THE CONTINUE KEYWORD

while True:
    print("Who are you?")
    name = input()
    if name != "Joe":
        continue
    print("Hello Joe,what is the password? (It is a fish)")
    password = input()
    if password == "swordfish":
        break
print("Access granted")

