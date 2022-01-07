#We are to use the "break" key word which is basically used to interrupt/stop an infinite loop
#This break keyword is normally used when dealing with infinite loops(these are loops that are normally repeatitive and therefore can't stop)
#...we therefore include the break key word to end this kind of loop
"""
This is the tutorial's example.
"""

#as seen in this example,upon removing the break statement,the loop prints out the required words but still...
#..asks us to insert the value wanted therefore making it an infinite loop,it will continue to ask us to insert the values even if we put the  wanted value
#..so to deal with this problem,upon a user inserting the value,the break keyword ensures that the loop doesn't continue when the desired results are achieved

"""
In the example given to us by OCR,we noticed that our loop was conditioned to 1 therefore it was always in a state of truthfulness,
therefore it is one that would basically continue to loop or repeat certain instructions since it is forever in that state.
To enable it to stop repeating those instructions,we use the break keyword to interrupt the repeation when a certain condition is met,where in our case,
a user is asked to insert the letter 'Q' so that the program stops to repeat the instructions ie,if the user inputs the required data,then text is diplayed
to message the user,this is followed by a break key word that will then end the infinite loop come what may(whether it wants or not it will stop)
###
The author suggests using boolean values instead of an infinite loop such that the boolean is true as the loop is iterating and false when the loop is to stop
as seen in the code below
"""
value = True
while value is True:
    letter = input("Please insert the letter Q : ")
    if letter == "Q" or letter == "q":
        value = False
        print("You have successfully inserted the right letter")


