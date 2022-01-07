#USING THE CONTINUE KEYWORD
#This keyword is used when we want to continue with a given loop,
#This is done automatically by the loop returning to the while or for statements line
i = 1
while i < 20:#while i is less than 20
    if i % 3 == 0: #if "i" divide by 3 grants us a reminder equal to zero
        i += 4 #add four to i at each iteration NOTE:This sequence of instructions will only be executed if the condition is met
        print("We've added 4 to i therefore i is now equal to ",i)
        continue#this will return to the start of the loop therefore from our "while" statement 
    
    print("I is equal to ", i)
    i+=1#In a classical case we add 1 to i
"""
EXPLANATION
This program is about the use cases of a continue keyword which basically continues a loop by returning to the line of the while or for statement
In our use case,this means that it will execute the instruction in our loop then,when at end it will continue by returning to the instruction that starts
a loop i.e (while or for).
IN our example,we have a variable that is equated to one and a loop that repeats certain instructions as long as i is less than 20,
this is followed by a condition which states that if i is divided by three and gives a reminder that is equal to zero,then i will be increased by four or four
is added to i,this is followed by a print instruction,however,the latter and former instructions will be executed in this loop only if i divided by 3 gives
a reminder of zero.
Just after the loop,we have a print function that prints out the value of i,followed by an incrementor that increases i by 1,this values then replaces
i's initial value,this leads to i being equal to two,when i is divided by 3,it doesn't giver a reminder of 0 so the instructions after the condition are not
executed,the process continues by the continue keyword returning to the while statement,then going to the next instruction that print the value of i and
increases it by 1 again,this time i is equal to three,so i's initial value is replaced by three,we get into the loop,remember the loop continues as long as
i is less than 20,so in our condition three is then divided by three and actually gives us the desired results as three divided by three gives zero as a
reminder therefore the instructions are executed within our condition,this continues while i is less than 20.
"""
