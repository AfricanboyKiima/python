#In this script,I am writing a function that prints out the multiplication table of any number
def table(number,max):#This function prints out the multiplication table of any number given to it as well as the maximum number of values to multiply it
    i = 0
    while i < max:
        print(i,"*",number,"=",i * number)
        i+=1
"""
This same function can be written using a for loop i.e
def table(number,max):
  for i in range(max):#here i can even decide the amount by which it should iterate as seen in the code that follows
        print(i,"*",number,"=",i * number)

        ###
        it can as well be written as follows
        def table(number,max):
          for i in range(1,max,2):
             print(i,"*",number,"=",i * number)
"""
