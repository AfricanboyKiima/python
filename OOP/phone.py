from items import *
#INHERITANCE EXPLAINED
class Phone(Item):#Here we go into detail on best practices on how to implement the super() to have acess to the attributes and methods of the parent class
   
    def __init__(self,name:str,price:float,qty=0,broken_phones= 0):#constructor special method to create attributes of object$*
        #The super() allows us to access the attributes and methods from the parent class in a child class
        super().__init__( 
            name, price, qty
        )
      
        assert broken_phones >= 0, f"broken_phones {broken_phones} is not greater than or equal to zero"
        #assign attributes to object
        
        self.broken_phones = broken_phones
        
    
    