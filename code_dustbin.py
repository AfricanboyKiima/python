"""
age = input("Please insert your age dear citizen : " )
age = int(age)
majeur = False
if age >= 18:
    majeur = True
if majeur:
    print("Hello there,you are old enough to join the army")
else:
    print("Case not known")
    ####
    age = 25
while age < 50:
    print("You are still very young dear citizen")
    age += 1
    alpha = "abcdefghijklmnopqrstuvwxyz"
for letters in alpha:
    print(letters)
    ###
    age = input("Please insert your age : ")
amount = input("Please insert your amount : ")
age = int(age)
amount = int(amount)
if age >= 40 or amount >= 500000:
    print("Yes dear customer you can open a bank account with us")
else:
    print("You can't open a bank account here dear customer")
    ###
    fruits = ["banana","orange","pineapple","guava","watermelon","dungan"]
for each in fruits:
    if each in ["banana","mango","ginger","pawpaw","coconut","dungan","marakucha","watermelon","guava","date"]:
        print(each)
    else:
        print("Not in stock")

"""
#This is something that involves for loops and literally for loops are used when we are dealing with sequences
#what happens is that a variable is instanciated by the for instruction which successively takes each and every value of the sequence that is being
#covered
names = ['Kiima','Samy','john','james','mbale','kituta','Junior','Charles','Mumbere']
for name in names:
    if name in ['Kiima','Samy','Ariko','Bob','Kambale','Kituta','Hervine','Charles','Jack','Ruth','Chala','Mumbere','Glody','Osarafu']:
        print(name)
        
        
"""
import random
def multiply(number,max):
    """
#This is a function that prints out the multiplication table of any number
#and also prints out a list of twenty random numbers chosen from 10 to 1010 after each iteration
"""
    for i in range(max):
        print(i,"*",number,"=",i*number)
        print(random.randint(10,1010))
"""
