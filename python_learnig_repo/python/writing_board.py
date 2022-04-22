class Person:#creation of a class thats models a person characterised by a name,surname,age and residence
    def __init__(self,name):
        self.name = name
        self.surname = "samuel"
        self.age = 33
        self._residence = "kembedila"#attribute wont be accessed from outside of the class since it begins with an underscore
        #it is at the moment we are defining the class that we have to specify that attribute that wont be accessed from outside of the class,we shall then create an accessor and mutator to
        #access and mutate the attribute respectively within our class.
    def _get_residence(self):#the single undescore just before the method means that the method won't be accessed from outside of the class
        return self._residence#this means this is a method that will enable us have access to the attribute that wont be accessed from outside of the class
    def _set_residence(self,value):#the single undescore just before the method means that the method won't be accessed from outside of the class
        self._residence = value
    Residence = property(_get_residence,_set_residence)#properties are the most tranparent way of manipulating attributes that wont be accessed from outside of the class
    def __getattr__(self,value):
        print("Attribute does not exist!!!")
        """
this sm works in such a way that when an attribute that doesnot exist is attached to the object,the attribute is then passed to this special method as a string and from there
we can tell python what to do,e.g we can simply tell python to print out a message saying the attribute does not exist
or even return another attribute depending on what we are coding
"""
    def __repr__(self):#this sm enables to represent and display an object hence helping with debugging
        return "the object is composed of the attributes {},{},{},{}".format(self.name,self.surname,self.age,self._residence)
    def __del__(self):
        print("Ooh !!!,the object has been deleted")
    
