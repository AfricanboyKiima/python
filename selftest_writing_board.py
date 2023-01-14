class Dog:# a class is a model a model being an informative representation of an object an object being a data type that becomes one owing to the class that instantiates it
    def __init__(self,breed,name,size,color):#constructor to enable us create the attributes of our object
        self.breed = breed
        self.name = name
        self.size = size
        self.color = color
        
    def get_breed(self):#accessor to access the value of our breed attribute for each instance or object 
        return self.breed
    
    def set_breed(self,val):
        self.breed = val

    def get_name(self):
        return self.name
    
    def set_name(self,val):
        self.name = val

    def get_size(self):
        return self.size

    def set_size(self,val):
        self.size = val

    def get_color(self):
        return self.size

    def set_color(self,val):
        self.size = val
    
    
    
