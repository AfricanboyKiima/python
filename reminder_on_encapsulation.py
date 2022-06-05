"""
Encapsulation consists of hiding some data of an object from being accessed or
modified. We ought to know that encapsulation is dealt with differently depending on the
programming language,for instance encapsulaton in java and c++ is dealt with using private and public
classes,in these programming languages,when an attribute of group of attributes is in the
public class,the attributes can be accessed from outside of the class but when an attribute or group
of attributes is in the private class,we've got to use accessors and mutators to access those
attributes,however,when it comes to python everything is public but to respect the principles of
encapsulation,python brings is properties which are the most transparent way of manipulating
attributes of an object. Now,we may for instance not want one to be able to access the data of
a specific attribute of even change it,we can call in conventions given to us by python such as:
when an attribute or method begins with a single underscore,we can't have access to either from outside of the
class,it is basically at that time that we are creating the class that we have to specify the attribute or methods
and it is to the property function that we pass our methods,lets look at an example
"""
class Person:#names of classes begin with an uppercase letter as it is a python convention.
    def __init__(self,name,surname,age,residence):#python constructor to create the attributes and without which we can't create the attributes of our class
        self.name = name
        self.surname = surname
        self.age = age
        self._residence = residence#attributes beginning with single underscore can't be accessed from outside of the class
    def _get_residence(self):
        return self._residence
    def _set_residence(self,val):
        self._residence = val
    def __str__(self):
        return "this object is composed of many attributes name,surname,age,_residence"
    def __getattr__(self,att_val):
        """"
this SM is called only when we try to access an attribute that doesnot exist within our class and with it can we write code telling python what to do when a user is trying to access an attribute
that does not exist. SM in python serve many purposes such as controlling the way objects create themselves and controlling access to attributes there exist a number of SM 
""""
        print("Alert!!! The attribute you're trying to access does not exist")
        
