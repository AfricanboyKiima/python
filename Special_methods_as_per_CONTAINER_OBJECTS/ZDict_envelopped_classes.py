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
        """
        for deep understanding of what happens behind the scenes,when we say object[index]
        the thing is it's actually the __getitem__ SM that is called and to it, the index or key that was passed to the operator is actually passed to
        this __getitem__ SM when it's passed to it,the SM then goes and does the verification of the index or key(depending on the datatype) from the
        container object,if the index passed to it exists in the container object from which it verified,it then returns the value that is at that
        index/key that was passed to it. That means it is actually the __getitem__ SM that is in charge of returning the values at the indexes passed
        to the container's operator. 
        Overloading of the operators therefore involves passing indexes to the operator,the __getitem__SM is called and when it is called the index passed
        to the operator is then passed to the SM which in turn goes and makes some verification of the index in the container object and returns the 
        value at that index of the container object that was passed to it.
        The SM returns the value at the index that was passed to it when it introspected the container object.
        To be more clear,the index/key is passed to the getitem SM,
        the SM on the otherhand introspects the container object to which the index/key was passed,it then returns the value at the index that
        was passed to it.
        """
    def __setitem__(self,index,val):
        """
        In this SM,when we type object[index] = val,this SM is actually the one that is called,when it is called,
        the index or key is passed to it except that since our attribute _dictionnaire is actually 
        """
        self._dictionnaire[index] = val
        
