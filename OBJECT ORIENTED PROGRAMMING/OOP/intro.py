class Item: # class is a model where model is an informative representation of an object

    #use of python constructor to create attributes of object which are basically its characteristics
    def __init__(self,name:str, price:float, quantity:0): #python constructor to enable us to create the attributes of object
        self.name = name
        self.price = price
        self.quantity = quantity

    """methods are actions or operations that can be performed on the object and in my case i have noticed
    that the operations or methods that can be performed on the object normally derived from the characteristics of 
    the object, earlier on when we were studyin OOP for the first time, we were looking at the board example
    where a board was basically characterised by a surface and it is basically on this surface that we 
    can write,read and rub stuff from, these three actions become the methods in OOP e.g
    
    class Board: #create board class or Data type
        def __init__(self):#constructor to enable us to create the attributes of our object
            self.surface = ""
        
        #create methods that can be performed on the object

        def Writer(self,words_to_write):
            if self.surface != "":#if there are words on the surface or if the surface is not empty
                self.surface += "\n"
            self.surface += words_to_write
        
        def Reader(self):
            return self.surface 
        
        def Rubber(self):
            self.surface = ""
     """
    #since object is composed of two attributes price and quantity, that means i can carry out an action
    #to provide me with the total price of items perhaps bought by buyer
    def calculate_total_price(self):

        return self.price * self.quantity