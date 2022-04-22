"""
special attributes in python are basically personnalised actions that are executed upon objects
these special methods are used to control the way objects create themselves as well as access to the attributes of an object
with the use of the __ini__ and __setattr__ special methods respectively,these special methods are known to python
 and knows what to do when it discoveres that the special methods have been applied.
"""
#python is an object related programmin languange that enables us to modelise as well as represent data that may tend to be
#more complex than strings and lists as well as dictionnary data types,this whole principle of OOPS gives us more
#potential to manipulate data flexibly.

#PROPERTIES ARE THE MOST TRANSPARENT WAY OF MANIPULATING ATTRIBUTES OF AN OBJECT and give us the ability to use the principles
#of encapsulation which consists of hiding some data of our objects. lets create our class
class Person:
    def __init__(self,name):
        self.name = name
        self.surname = "samuel"
        self.age = 33
        self._residence = "kembedila"#notice the underscore put before the attribute,it is a python convetion that means
                #that the attribute can't be accessed from outside of the class.
        """
        other programming languages such as java and c++ have rules put in place that deal with encapsulation,when an attribute
        or group of attributes is put in the public class,we can have direct access to it,but when a group of attributes or an attr
        ibute is in the private class,then we can not but have to use accessors and mutators to have access and also modify the
        attributes respectively,but python has no such principles since everything in python is public but to respect the priciples
        of encapsulation,properties come in to help us deal with such
        """
    def _get_residence(self):
        return self._residence
    def _set_residence(self,new_value):
        self._residence = new_value
    residence = property(_get_residence,_set_residence)
    
    
