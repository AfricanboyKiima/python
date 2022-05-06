"""
so here we have a board on which we are going to write and read as well as rub from.
Boards are composed of surfaces on which we can basically perform the actions as seen above. so in this scenario we shall create
those actions as methods that will be performed on objects.
The issue here is that we shall create a class from which an object coming from it would basically be composed of a surface and would use the methods defined by the class
"""
class Board:
    def __init__(self):
        self.surface = ""
    def reader(self):
        return self.surface
    def writer(self,words):
        if self.surface != "":#this means if the surface is not empty
            self.surface += "\n"#then the surface will be equal to what exists already in the surface plus a key word argument
        self.surface += words
        
