#Here created for loop which will also have a conditional statement
#In this part,we are told to master the use of "in" when using conditional statements
#our for instruction instantiates the letters variable which will basically succesively take values of the sequence that's being covered

phrase = "I am a Muslim"
for letters in phrase:
    if letters in "AEIOUYaeiouy":
        print(letters)
    else:
        print("#")
"""
#This is something that involves for loops and literally for loops are used when we are dealing with sequences
sequences refer to a series of things that are following one another
#what happens is that a variable is instanciated by the for instruction which successively takes each and every value of the sequence that is being
#covered
names = ['Kiima','Samy','john','james','mbale','kituta','Junior','Charles','Mumbere']
for name in names:
    if name in ['Kiima','Samy','Ariko','Bob','Kambale','Kituta','Hervine','Charles','Jack','Ruth','Chala','Mumbere','Glody','Osarafu']:
        print(name)
"""
