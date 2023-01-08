"""WE ARE LOOKING AT CLASS ATTRIBUTES HERE"""


class Item:#class is a model which simply means it represents an idea or theory 
    def __init__(self,name:str, price:float,quantity = 0):#constructor to create attributes of our object

        assert price >= 0, f"Price {price} is not greater than or equal to zero "
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero "

        #assign to self object
        self.name = name #attributes are characteristics of the object
        self.price = price
        self.quantity = quantity 
    
    def calculate_total_price(self):

        return self.price * self.quantity

    