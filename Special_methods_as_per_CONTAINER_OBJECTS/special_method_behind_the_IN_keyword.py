"""
we previously looked at the special methods that are behind container objects and we precisely looked at the __getitem__,__setitem__and __delitem__SM
"""
class ZDict:
    def __init__(self):
        self._dictionnary = {}
    def __getitem__(self,index):
        return self._dictionnary[index]
    def __setitem__(self,index,val):
        self._dictionnary[index] = val
    def __contains__(self,element):
        if element in self._dictionnary:
            return True
        else:
            return False
    def __repr__(self):
        return "This object is composed of the attribute _dictionnary"
"""
We have been able to learn about SM in python and we are currently looking at
the __contains__()SM which is called if we want to know if an object is
found in a specific container object. It is basically the SM that is behind the
IN keyword for instance when we say
foo = ["kiima","samuel","john"]
"kiima" in foo#this is where the __contains__ SM is called.....
...it is called as foo.__contains__("kiima"),it then returns a boolean value
of True if indeed the object if found in the container object and False if
the boolean value is not in the container object.This simply means that
the __contains__ SM is the one that is called if we want to confirm the
absence of presence of an object within a container object.
When we say "kiima" in foo,python calls the __contains__SM and says foo.__contains__("kiima") and so it is in plain english and python indeed is able to know whether an object is within the specified
container object.
"""
