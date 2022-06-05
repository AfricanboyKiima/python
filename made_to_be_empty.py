"""
lets remind ourselves of python  as an object oriented programming language that allows us to
to model and represent data that is more complex than just strings,lists,dictionnaries and other data types
this simply means that it grants us the ability to create our own data types hence granting us more flexibility
Python's approach to OOP is a bit different from other programming languages such as c++ and java that contains public classes as well as private
classes. Python on the conntrary has no private classes as everything is actually public but python deals with privacy in form of what is known as
encapsulation which is term used to refer to hiding and protecting data of an object from being accessed or modified 
"""
class Person:
    def __init__(self,name,surname,age,residence):
        self.name = name
        self.surname = surname
        self.age = age
        self._residence = residence
        #encapsulation consists of protecting or hiding data of an object from being accessed or modified
     """
Different programming languages have a different approach to OOP,in java and c++,when an attribute of group of attributes is in the public class,we can have access to those attributes
from outside of the class,but when an attribute or group of attributes is in the private class,we have to use accessors and mutators to access those attributes
but with python,we do  not have private classes as everything is public but to respect the principles of encapsulation python uses properties which are the most transparent way
of manipulating attributes of python that won't be accessed from outside of the class, this is done by specifying inside the class the attributes that won't be accessed using what are known
as conventions,in python, it is at the time you are defining the class that we've got to define the attributes that won't be accessed from outside of the class by use of a single underscore as
seen in our attribute _residence
In python,when an attribute or method begins with a single underscore, then this means that we shall not access the attribute from outside of the class
The property function receives a number of parameters which are basically four methods i.e accessors,mutators,method to delete the object and a method informing us about an object
When created, this property function is equated to a variable through which we can access and mutate the values of our attributes 
"""
     def _get_residence(self):
         return self._residence
     def _set_residence(self,val):
         self._residence = val
     Residence = property(_get_residence,_set_residence)
     def __getattr__(self,attr_val):
         print("Alert!!! The attribute you're trying to access does not exist")
     def
