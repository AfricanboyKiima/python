"""
We we able to understand something called overloading of operators(square brackets). These are basically operators
being used to respectively put in use the special methods __getitem__,__setitem__,__delitem__
overloading of containers involves telling python what to do when it's using an operator in
a specific way.
the use of operators corresponds to the special method calls we previously talked about respectively:
object[index] #__getitem__
object[index] = value#__setitem__
del object[index]#__delitem__
In this python script,we shall be looking at how an example just to get things clicking
"""
class ZDict:#class ZDict
    def __init__(self):#constructor without which we can't create attributes of this class
        self._dictionnaire = {}#att can't be accessed from outside of the class i.e object wont access it
    def __getitem__(self,index):#this SM is called when we type object[index]
        return self._dictionnaire[index]
        
