class Person:
    def __init__(self,name,surname,age,residence):
        self.name = name
        self.surname = surname
        self.age = age
        self._residence = residence#this attribute won't be accessed from outside
        #of the class as it's a pyhon convention that all attributes that begin
        #with a single underscore cant be accessd from outside of the class
        """
In python OOP is used to model and represent data that may tend to be more complex than just lists,dictionnaries,tuples etc.
OOP is very fundamental as it allows us to create our own data types. As we look at OOP, we ought to understand a number of principles that are literally useful things such as variables are funcdamental,
attributes as well as methods,remember that these are actions that are performed on objects
"""
    def _get_residence(self):
        return self._residence
    def _set_residence(self,val):#this SM will literally enable to modify the attribute using a python function called property which receives a number of methods i.e
        self._residence = val#this method will be called when we want to modify an attribute's value
    Residence = property(_get_residence,_set_residence)
    def __repr__(self):
        return "The object from this class is composed of a name,surname,age,_residence with the last one being inaccessible from outside of the class"
    def __str__(self):
        return "Object has four attributes"
    
"""
the __str__ and __repr__ SM are used to display object as well as represent and display objects respectively 
"""
