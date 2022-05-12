"""
when looking at container objects(they contain other objects or elements within them i.e lists,dictionnaries,strings) we actually wanted to understand the special methods that are
called when we are accessing,modifying and deleting the elements within these container objects,the act of passing indexes/keys to the operators of our objects is called overloading of operators,
this process of overloading can be seen in three steps and there are special methods that are called respectively i.e __getitem__,__setitem__,__delitem__, let's look at samples of overloading,
by the way overloading of container consists of telling python what to do when using a specific operator in a specific way. we are looking at a class (name),this class contains a number of objects of names
of people
name = ["kiima","fadhil","samuel"]#list of names of people 
name[0]#'kiima' is returned as a value
name[1]#'fadhil' is returned as a value
name[2]#'samuel' is returned as a value
Lets look at an applied example
"""
#we are creating an envelopped class,envolopped classes are classes that actually resemble the
#normal classes that we create but are not actually classes in actual sense. we are going to create
#an envelopped class that will act like a dictionnary but won't be a dictionnary in actual sense,
#it will be composed of an attribute called,_dictionnary that wont be accessed from outside of the class
#python convention states that attributes and classes that begin with a single underscore wont be accessed from outside of that class
#when an object is created from this class and basically pass an index or key to its operator,self._dictionnary[index] is returned
class ZDict:
    def __init__(self):
        self._dictionnary = {}#attribute won't be accessed from outside of the class
    def __getitem__(self,index):#this SM is the one that is called when we are accessing an object from a container object
        """
it works in such a way
"""
        return self._dictionnary[index]
    def __setitem__(self,index,val):
        self._dictionnary[index] = val
