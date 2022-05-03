"""
We we able to understand something called overloading of containers. These are basically operators
being used to respectively put in use the special methods __getitem__,__setitem__,__delitem__
overloading of containers involves telling python what to do when it's using a an operator in
a specific way.
the use of operators corresponds to the special method calls we previously called respectively:
object[index] #__getitem__
object[index] = value#__setitem__
del object[index]#__delitem__
In this python script,we shall be looking at how an example just to get things clicking
"""
class ZDict:
    def __init___(self):#a python constructor used to create attributes of our class
        """envelopped class of a dictionary,these resemble the classes we create but are in actual
sense not classes"""
        self._dictionnaire = {}#attribute can't be accessed from outside of the class i.e can't say object.attribute
    def __getitem__(self,index):
        """this sm is called when we call object[index] and redirects us to
self._dictionnaire[index]"""
        return self._dictionnaire[index]
