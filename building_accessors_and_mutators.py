class Person:
    def __init__(self,name:str,age:int,password):
        self.name = name
        self.age = age
        self.__password = password

    @property
    def Password(self):
        return self.__password   
    
    
    @Password.setter
    def Password(self,val):
        self.__password = val    


obj1 = Person("Kiima",45,"123b#")
obj1.Password = "kslhfdlfh"
print(obj1.Password)