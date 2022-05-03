"""
as we are looking at special methods,we are currently looking at container special methods
which are used to control the way objects create themselves as well as access to attributes
using what is known as a constructor and a getattr specila methods respectively  s),these
there are a number of special methods that are basically involved which are:
__getitem__,__setitem__,__delitem__ and these are assigned to the operatores as follows respectively
object[index] #here it's the __getitem__ special method that is called
object[index] = value#here it is the __setitem__ sm that is called
del object[index] the previous special methods are called respectively as we saw.
in such a case, we are going to create our own class called zdict which will be an envelopped class
that will behave like all other classes that we've been creating but will not exactly be a class.
we shall create an attribute _dictionnaire which won't be accessed from outside of the class
(this means we have to name it beginning with an underscore as that is a python convention that
says all attributes and methods beginning with underscores(single) wont be accessed from outside
of the class.
"""
 
