#working with functions is vital for program,these are used to perform specific tasks in a program
#Functions have a collection of instructions that are put together then these are then stored into a file to make a module
#So,modules are a collection of functions that when put together with other modules form a full program
#IN THIS EXAMPLE,WE ARE GOING TO USE ONE OF THE PROGRAMS WE HAD CODED A PROGRAM THAT PRINTS OUT THE MULTIPLICATION TABLE OF 7
def table(number,max):
    i = 0
    while i < max:
        print(i,"*",number,"=",i * number)
        i += 4

        
"""
This function basically calculates and prints the multiplication table of any number that it gets into its parameter,however,the integer numbers that
multiply this number should not surpass 19,therefore they should strictly inferior to 20..
A user may want to specify the maximum number to calculate the desired number for instance when we are dealing with such cases,we may want increase the numbers
that multiply our specific number by one(1) at each iteration while maintaining our number,this is some sort of looking for the multiples of a number as well
multiples are the results we get by multiplying a number by integers,e.g 1 * 4,2 * 4,3 * 4.....In this case,as far as our subject of functions is concerned,
the integers are the ones that will be increamented but the maximum value that can be attained of this increamentation can also be specified using the
'max' key word within our functions parameters,so when dealing with loops we can specify the maximum value of an iteration.
"""
#####################################################
"""
def multiplication_table(number):
    i = 0
    while i < 20:
        print(i, "*" , number, "=", i * number)
        i += 1
"""
