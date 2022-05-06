"""
EXAMPLE ONE
We are going to work on what is known as surcharge d'operateur.This basically involves telling python what to do when using this or that operator
That is what is referred to as surcharge d'operateur so we are basically telling python what to do when using different operators
And as we are looking at these,we are going to look at four special methods that intervenne when dealing with container objects.
which are __getitem__,__setitem__,__delitem__,these are called upon our object using the operators respectively in the following ways
object[index]#here __getitem__sm is called
object[index] = val#here __setitem__sm is called
del object[index] #here the __delitem__sm is called
To understand this,we are going to look at what we call envelloped classes which ae basically classes that look like other classes but are in
actual sense not classes.
"""
class ZDict:
    def __init__(self):#this sm is used to create the attributes of our class
        self._dictionary = {}#att can't be accessed from outside of the class
        """
python convention states attributes and methods beginning with underscores can't be accessed from out
side of the class. ie we can't say object.attribute nor can we say object.method()
"""
    #lets see how the __getitem__sm is used
    def __getitem__(self,index):
        """
this method is called when we type object[index]
"""
        return self._dictionary[index]
    def __setitem__(self,index,value):
        self._dictionary[index] = value
