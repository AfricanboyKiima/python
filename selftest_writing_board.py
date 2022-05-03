#a class is a model from which we can create objects
#take for instance an artist, he needs for instance an object such as a tree for instance,this tree has to be drawn to create an image,
#in such a scenario,this means that from the tree(model),the artist can then create many images of that tree since he's got the model(tree)
"""
with OOP in python,a class in this case would be the tree as it is the model,therefore, a class is a model from which we can create objects
objects come from classes and when an object comes from a class, it is able to use the attributes as well as the methods of that class,
lets look at this more deeply
"""
#lets for instance look at our tree
"""
classes are models from which we can create objectsgg
"""
class Tree:#a class is a model from which we can create objects
    def __init__(self,height,weight):#a python constructor that enables us to create attributes contained in objects and without which we cant create attributes
        self.height = height
        self.weight = weight
    
    def height_(self):#this is a method of this class and it is an action that is performed on any object that comes from this clss
        return self.height
    
#a class is a model from which objects are created 
