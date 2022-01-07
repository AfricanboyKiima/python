#Like we said earlier on,we use the break keyword when we want to interrupt a loop at a given time and
#..that this break keyword is normally used with infinite loops,it will interrrupt the infinite loop when a particular action/wanted results are achieved
#The key word stop a loop irrespective of the condition of the loop

letter = ""
boolean =  True
while boolean is True:
    letter =  input("Please insert the value 'Q' that is needed : ")
    if letter == "Q":
        boolean = False
        print("You inserted the required value,thanks.")
        continue
"""
In this case we are using boolean values,from OCR,the guy suggests that instead of using an infinite loop through use of 1,we can instead use a boolean
value that will be true as the loop loops,in otherwords,we created a boolean variable that contains True as its value,what happens is that,the while loop will
continue repeating the given instructions as long as our boolean variable is True,however,to be able to end the loop when the letter Q is inserted,we
first ensured that we got the values from a user using the input function which stores the gotten values into a variable,
we then put a condition such that if what the value our user inserts is equal to Q,the loop ends,this is achieved through using conditional statement where
boolean value is equated to False if the value is equal to Q
"""





#we did not use the break key word just to avoid it so used another method to solve the same problem 
"####################################################"
"""
In the example given to us by OCR,we noticed that our loop was conditioned to 1 therefore it was always in a state of truthfulness,
therefore it is one that would basically continue to loop or repeat certain instructions since it is forever in that state.
To enable it to stop repeating those instructions,we use the break keyword to interrupt the repetition when a certain condition is met,where in our case,
a user is asked to insert the letter 'Q' so that the program stops to repeat the instructions ie,if the user inputs the required data,then text is diplayed
to message the user,this is followed by a break key word that will then end the infinite loop come what may(whether it wants or not it will stop)
"""
"""
SOLUTION TO SAME PROBLEM
letter = ""
while letter != "Q":
 letter = input("Please insert 'Q' to stop this program : ")
 if letter == "Q":
    print("End of loop")

"""
a 
